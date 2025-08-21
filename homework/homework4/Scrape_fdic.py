from pathlib import Path
from dotenv import load_dotenv
import os
from typing import Dict, List
import datetime as dt
import requests
from bs4 import BeautifulSoup
import pandas as pd

DATA_RAW = Path("data/raw")
DATA_RAW.mkdir(parents=True, exist_ok=True)

def safe_stamp():
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")

def safe_filename(prefix: str, meta: Dict[str, str]) -> str:
    mid = "_".join([f"{k}-{str(v).replace(' ', '-')[:20]}" for k, v in meta.items()])
    return f"{prefix}_{mid}_{safe_stamp()}.csv"

def validate_df(df: pd.DataFrame, required_cols: List[str], dtypes_map: Dict[str, str]) -> Dict[str, str]:
    msgs = {}
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        msgs["missing_cols"] = f"Missing columns: {missing}"
    for col, dtype in dtypes_map.items():
        if col in df.columns:
            try:
                if dtype == "datetime64[ns]":
                    pd.to_datetime(df[col])
                elif dtype == "float":
                    pd.to_numeric(df[col])
            except Exception as e:
                msgs[f"dtype_{col}"] = f"Failed to coerce {col} to {dtype}: {e}"
    na_counts = df.isna().sum().sum()
    msgs["na_total"] = f"Total NA values: {na_counts}"
    return msgs

SCRAPE_URL = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
headers = {"User-Agent": "AFE-Course-Notebook/1.0 (contact: instructor@example.edu)"}
resp = requests.get(SCRAPE_URL, headers=headers, timeout=30)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, 'html.parser')
table = soup.find('table')
try:
    df_scrape = pd.read_html(str(table))[0]
except Exception as e:
    print("Scrape failed:", e)
    html = """
    <table>
        <tr><th>Ticker</th><th>Price</th></tr>
        <tr><td>AA</td><td>100</td></tr>
        <tr><td>BB</td><td>200</td></tr>
    </table>
    """
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    df_scrape = pd.read_html(str(table))[0]

if 'Fund' in df_scrape.columns:
    df_scrape['Fund'] = pd.to_numeric(df_scrape['Fund'], errors='coerce')

msgs2 = validate_df(df_scrape, required_cols=list(df_scrape.columns), dtypes_map={})
print(msgs2)

fname2 = safe_filename(prefix="scrape", meta={"site": "fdic", "table": "failed_banks"})
out_path2 = DATA_RAW / fname2
df_scrape.to_csv(out_path2, index=False)
print("Saved:", out_path2)
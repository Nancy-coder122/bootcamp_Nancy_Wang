from pathlib import Path
from dotenv import load_dotenv
import os
from typing import Dict, List
import datetime as dt
import requests
import pandas as pd

DATA_RAW = Path("data/raw")
DATA_RAW.mkdir(parents=True, exist_ok=True)

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

ALPHA_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
print("Loaded ALPHAVANTAGE_API_KEY?", bool(ALPHA_KEY))

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

SYMBOL = "AAPL"
use_alpha = bool(ALPHA_KEY)
print("Using Alpha Vantage:", use_alpha)

if use_alpha:
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": SYMBOL,
        "outputsize": "compact",
        "apikey": ALPHA_KEY,
        "datatype": "json"
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    js = r.json()
    key = [k for k in js.keys() if "Time Series" in k][0]
    series = js[key]
    df_api = (
        pd.DataFrame(series).T
        .rename_axis("date")
        .reset_index()
    )
    df_api = df_api[["date", "4. close"]].rename(columns={"4. close": "adj_close"})
    df_api["date"] = pd.to_datetime(df_api["date"])
    df_api["adj_close"] = pd.to_numeric(df_api["adj_close"])
else:
    import yfinance as yf
    df_api = yf.download(SYMBOL, period="6mo", interval="1d").reset_index()[["Date", "Adj Close"]]
    df_api.columns = ["date", "adj_close"]

df_api = df_api.sort_values("date").reset_index(drop=True)
msgs = validate_df(df_api, required_cols=["date", "adj_close"], dtypes_map={"date": "datetime64[ns]", "adj_close": "float"})

fname = safe_filename(prefix="api", meta={"source": "alpha" if use_alpha else "yfinance", "symbol": SYMBOL})
out_path = DATA_RAW / fname
df_api.to_csv(out_path, index=False)
print("Saved:", out_path)
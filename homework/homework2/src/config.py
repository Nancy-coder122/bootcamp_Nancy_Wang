from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

def get_key(key):
    return os.getenv(key)
    
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
MODEL_DIR = ROOT / "models"

FD_API_KEY = os.getenv("FD_API_KEY", "")

for d in (RAW_DIR, MODEL_DIR):
    d.mkdir(parents=True, exist_ok=True)

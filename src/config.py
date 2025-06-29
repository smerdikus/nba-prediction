from pathlib import Path, PurePath
from dotenv import load_dotenv
import os
load_dotenv()
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
MODEL_DIR = ROOT / "models"
FD_API_KEY = os.getenv("FD_API_KEY", "")
for d in (RAW, MODEL_DIR): d.mkdir(parents=True, exist_ok=True)

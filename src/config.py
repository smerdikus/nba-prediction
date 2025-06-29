"""Central project paths and global configuration."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # read variables from .env if present

ROOT_DIR: Path = Path(__file__).resolve().parents[1]
DATA_DIR: Path = Path(os.getenv("DATA_DIR", ROOT_DIR / "data"))
RAW_DIR: Path = DATA_DIR / "raw"
PROCESSED_DIR: Path = DATA_DIR / "processed"
MODEL_DIR: Path = ROOT_DIR / "models"

# Ensure directories exist
for _dir in (DATA_DIR, RAW_DIR, PROCESSED_DIR, MODEL_DIR):
    _dir.mkdir(parents=True, exist_ok=True)

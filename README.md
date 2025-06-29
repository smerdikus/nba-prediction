# Sports Predictor

A modular Python project that scrapes tennis match data, engineers features, trains machine‑learning models
to predict match outcomes, and evaluates betting value.

## Quick start

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate          # On Windows use: venv\Scripts\activate

# 2. Install requirements
pip install -r requirements.txt

# 3. Configure environment (optional)
cp .env.example .env               # Edit variables as needed

# 4. Run the end‑to‑end pipeline
python -m src.cli --help
```

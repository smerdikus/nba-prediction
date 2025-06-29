# Sports Predictor — Multi‑Sport (NBA 🏀, Football ⚽, Tennis 🎾)

End‑to‑end pipeline:

1. **Scrape** historical data (and basic live fixtures)  
2. **Engineer** sport‑specific features (Elo, rest‑days, etc.)  
3. **Train** a logistic‑regression baseline (swap in LightGBM easily)  
4. **Predict** the win probability for any upcoming match via CLI

```bash
# Quick start
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Train NBA model on 2019‑20 through 2023‑24 seasons
python -m src.cli train --sport nba --seasons 2019-20 2020-21 2021-22 2022-23 2023-24

# Predict Warriors vs Lakers today
python -m src.cli predict --sport nba --home GSW --away LAL
```

`src/` is a plain Python package. Either set `PYTHONPATH=.` before running,
or install in editable mode: `pip install -e .`.

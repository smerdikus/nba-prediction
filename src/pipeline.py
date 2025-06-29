"""End‑to‑end pipeline tying together data loading, feature engineering, and model training."""

from src.data.loader import load_all
from src.features.engineering import compute_elo
from src.models.train import train


def main(start_year: int = 2018, end_year: int = 2024):
    # 1. Load & concatenate seasons
    df = load_all(start_year=start_year, end_year=end_year)

    # 2. Feature engineering
    df = compute_elo(df)

    # 3. Train model
    train(df)


if __name__ == "__main__":
    main()

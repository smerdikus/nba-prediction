"""Feature engineering utilities (Elo rating, recent form, etc.)."""

import pandas as pd
import numpy as np

def compute_elo(df: pd.DataFrame, k: int = 32) -> pd.DataFrame:
    """Add pre‑match Elo columns for both players."""
    players: dict[str, float] = {}
    elo_winner_pre: list[float] = []
    elo_loser_pre: list[float] = []

    for _, row in df.iterrows():
        p1 = row["Winner"]
        p2 = row["Loser"]

        r1 = players.get(p1, 1500.0)
        r2 = players.get(p2, 1500.0)

        elo_winner_pre.append(r1)
        elo_loser_pre.append(r2)

        # Expected scores
        e1 = 1.0 / (1 + 10 ** ((r2 - r1) / 400))
        e2 = 1.0 - e1

        # Update after match
        players[p1] = r1 + k * (1 - e1)
        players[p2] = r2 + k * (0 - e2)

    df = df.copy()
    df["elo_winner_pre"] = elo_winner_pre
    df["elo_loser_pre"] = elo_loser_pre
    return df

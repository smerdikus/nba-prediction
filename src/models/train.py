"""Training logic for a simple logistic‑regression (baseline) model."""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split

from ..config import MODEL_DIR


def _prepare_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Return a two‑row‑per‑match DataFrame with *elo_diff* and *label*."""
    rows: list[dict] = []
    for _, row in df.iterrows():
        diff = row["elo_winner_pre"] - row["elo_loser_pre"]

        rows.append({"elo_diff": diff, "label": 1})
        rows.append({"elo_diff": -diff, "label": 0})
    return pd.DataFrame(rows)


def train(df: pd.DataFrame, out_path: Path | None = None):
    data = _prepare_dataset(df)
    X = data[["elo_diff"]]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    probs = clf.predict_proba(X_test)[:, 1]
    print("Accuracy:", accuracy_score(y_test, (probs > 0.5)))
    print("Log‑loss:", log_loss(y_test, probs))

    out_path = out_path or MODEL_DIR / "logreg.pkl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, out_path)

    return clf, out_path

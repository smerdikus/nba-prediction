"""Model‑related helper functions."""

def kelly_fraction(p: float, odds: float) -> float:
    """Return Kelly bet fraction given win probability *p* and decimal *odds*."""
    b = odds - 1.0
    return (b * p - (1 - p)) / b if b > 0 else 0.0

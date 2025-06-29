"""Simple CLI wrapper around the pipeline."""

import argparse
from .pipeline import main as run_pipeline


def get_args():
    parser = argparse.ArgumentParser(description="Run the sports‑prediction pipeline.")
    parser.add_argument("--start-year", type=int, default=2018, help="First season to include")
    parser.add_argument("--end-year", type=int, default=2024, help="Last season to include")
    return parser.parse_args()


def cli():
    args = get_args()
    run_pipeline(start_year=args.start_year, end_year=args.end_year)


if __name__ == "__main__":
    cli()

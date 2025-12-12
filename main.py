"""
A simple script that runs the full pipeline in order: fetch data → build features → train model → evaluate model, so you can redo experiments with one command
"""

from src import fetch_data, build_features, train_linear_model, evaluate_model

if __name__ == "__main__":
    fetch_data.fetch_goog_data(ticker="GOOG")
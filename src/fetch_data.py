"""
Functions to download or read raw GOOG price data, clean basic issues (sort by date, drop missing), 
and save to data/raw/goog_raw.csv
"""

import yfinance as yf
from datetime import date
import pandas as pd


def fetch_goog_data(ticker, start_date="2015-01-01", end_date=date.today().strftime("%Y-%m-%d")):
    try:
        dat = yf.Ticker(ticker)
        df = pd.DataFrame(dat.history(start=start_date, end=end_date))
        df.index = df.index.normalize() # remove time component

        # Check if data has a clean "date" column and drop them if not
        parsed = pd.to_datetime(df.index, errors='coerce', format="%Y-%m-%d")
        invalid_dates = parsed.isna()
        invalid_rows = df[invalid_dates]
        if not len(invalid_rows) == 0:
            print(f"Dropping rows with invalid dates:\n{invalid_rows}")
            df = df[~invalid_dates]

        # Check if datapoints are empty and remove them
        valrows_with_nan = df[df.isnull().any(axis=1)]
        if not valrows_with_nan.empty:
            print(f"Dropping rows with NaN values:\n{valrows_with_nan}")
            df = df.dropna()
        
        # Sort by date (ascending)
        df.sort_index(ascending=True, inplace=True)

        # Save to CSV
        df.to_csv("data/raw/goog_raw.csv")

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

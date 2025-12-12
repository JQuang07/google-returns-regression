"""
Loads goog_features.csv, splits by time into train/test, fits a LinearRegression to predict today's return from features, 
and optionally saves the fitted model (e.g., with joblib)
"""

# === run_pipeline.py ===
# Real-time pipeline: Load -> Feature Engineering -> Train or Load Model -> Predict

import pandas as pd
from modules import loader, feature_engineering, polygon_api
from modules import fred_api, google_trends, news_api, twitter_sentiment
from modules import loader
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib
import os

MODEL_PATH = "models/model.pkl"

def load_all_data(ticker):
    print("Loading market data...")
    market_df = loader.load_market_data(ticker)
    
    print("Loading FRED data...")
    fred_df = fred_api.get_fred_macro_features()
    
    print("Getting Google Trends...")
    trends_df = google_trends.get_trends(ticker)
    
    print("Getting news sentiment...")
    news_score = news_api.get_news_sentiment(ticker)
    
    print("Getting Twitter sentiment...")
    twitter_score = twitter_sentiment.get_sentiment_score(ticker)
    
    # Merge and enrich
    df = market_df.copy()
    df['news_sentiment'] = news_score
    df['twitter_sentiment'] = twitter_score
    df = pd.concat([df, fred_df, trends_df], axis=1)
    
    return df.dropna()

def process_and_predict(ticker="AAPL"):
    df = load_all_data(ticker)
    df_fe = feature_engineering.create_features(df)

    X = df_fe.drop(columns=["target"])
    y = df_fe["target"]

    if os.path.exists(MODEL_PATH):
        print("Loading existing model...")
        model = joblib.load(MODEL_PATH)
    else:
        print("Training new model...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, MODEL_PATH)

    print("Making predictions...")
    predictions = model.predict(X)
    df["prediction"] = predictions

    output_path = "output/signals.csv"
    os.makedirs("output", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Predictions saved to: {output_path}")

if __name__ == "__main__":
    process_and_predict("AAPL")

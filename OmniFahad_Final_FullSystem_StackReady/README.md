
# OmniFahad Final System

A harmonized real-time option prediction pipeline with integrated ML, financial APIs, sentiment analysis, dashboard UI, and automation.

---

## Features

- **Real-time Data Loader**
  - Market data via Polygon.io
  - Macro indicators via FRED
  - Google Trends
  - News & Twitter sentiment

- **Feature Engineering**
  - Merges multi-source indicators into ML-ready features

- **ML Pipeline**
  - Auto-trains or loads model
  - Predicts option price or directional signals

- **Dashboard (Streamlit)**
  - Run the pipeline
  - View predictions and charts
  - Clean, mobile-friendly interface

- **Scheduler**
  - Automatically retrains and predicts every 6 hours using `main.py`

---

## Structure

```
OmniFahad/
├── run_pipeline.py               # Full real-time ML pipeline
├── main.py                       # Scheduler (every 6 hours)
├── app/
│   └── app.py                    # Streamlit dashboard UI
├── output/
│   └── signals.csv               # Latest predictions
├── modules/
│   └── *.py                      # Data, sentiment, feature, and API modules
├── notebooks/
│   └── *.ipynb                   # Experiments & training
├── requirements.txt             # Install all deps
└── README.md
```

---

## How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run Prediction Pipeline

```bash
python run_pipeline.py
```

### 3. Launch Streamlit Dashboard

```bash
streamlit run app/app.py
```

### 4. Run Automated Scheduler

```bash
python main.py
```

---

## API Keys Required

- `Polygon.io API Key`
- `OpenAI API Key` (for sentiment)

Add them securely to:
- `modules/polygon_api.py`
- `modules/news_api.py`
- `modules/twitter_sentiment.py`

---

## Credits

Built by OmniFahad with real-time intelligence, machine learning, and automation at its core.

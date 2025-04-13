
# OmniFahad Unified Options + Macro Intelligence Platform

This is a harmonized system that combines:
- **OmniMarket**: options strategy simulation, prediction models, ML training
- **Fahad System**: macroeconomic data collection, feature engineering from trends and news

---

## Modules

- `app/app.py` — Streamlit frontend
- `notebooks/` — Jupyter notebooks for prediction, strategy, ML training
- `modules/` — Data collection + feature engineering modules (FRED, news, trends, etc.)

---

## Merged Features

### OmniMarket (Core)
# OmniMarket Options Platform

This project provides a complete toolset for analyzing and predicting options strategies using Python, Streamlit, and machine learning.

## Features

### 1. Streamlit Web App
- Search any stock
- Select available expiration dates
- Add multi-leg strategies (call/put, buy/sell)
- Simulate Profit & Loss (P&L) at expiry with interactive charts

### 2. Jupyter Notebooks
- `OmniMarket_Complete_With_Ticker_Expiry_Picker.ipynb`:
  - Accurate options prediction using Black-Scholes and Greeks
- `OmniMarket_Strategy_Builder.ipynb`:
  - Manual input for spreads, straddles, and condors
- `OmniMarket_ML_Trainer.ipynb`:
  - Train machine learning models to predict option premium, P&L, and IV

## Getting Started

### Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
```bash
streamlit run OmniMarket_Streamlit_App.py
```

Or deploy this repository directly on [Streamlit Cloud](https://streamlit.io/cloud).

## Project Structure
```
.
├── OmniMarket_Streamlit_App.py
├── requirements.txt
├── OmniMarket_Complete_With_Ticker_Expiry_Picker.ipynb
├── OmniMarket_Strategy_Builder.ipynb
└── OmniMarket_ML_Trainer.ipynb
```

## License
MIT

---

Built with passion by OmniMarket.

### Fahad System (Integrated)
# OmniMarket Prophet

OmniMarket Prophet هو نظام تنبؤ وتحليل ذكي للأسواق المالية يستخدم تقنيات التعلم الآلي العميق والكمي لتوقع أسعار الأصول (مثل الأسهم والعقود الآجلة) بدقة عالية مع واجهة تفاعلية عبر Streamlit.

---

## 🚀 الميزات الرئيسية

- **رفع ملفات CSV يدويًا** (Open, High, Low, Close, Volume)
- **تدريب نماذج XGBoost و LSTM تلقائيًا** عبر الواجهة
- **تقسيم البيانات 80% تدريب / 20% اختبار**
- **حساب MAE ودقة الاتجاه لكل نموذج**
- **تفسير التنبؤات باستخدام GPT**
- **مخططات تحليل تفاعلية عبر Plotly**
- **واجهة Streamlit جاهزة للاستخدام**

---

## 🗂️ هيكل المشروع

```
omni_project/
├── core/                      ← وحدات التنبؤ والتفسير والتوصية
├── data/historical/           ← مكان ملفات CSV المرفوعة
├── models/                    ← النماذج المدربة (XGBoost / LSTM)
├── training/                  ← trainer.py لتدريب النماذج
├── streamlit_ui/              ← واجهة Streamlit
├── OmniMarket_Colab_Trainer.ipynb  ← دفتر تدريب من Google Colab
└── README.md
```

---

## ⚙️ طريقة التشغيل

1. تثبيت الحزم:
```bash
pip install -r requirements.txt
```

2. تشغيل الواجهة:
```bash
streamlit run streamlit_ui/app.py
```

---

## 📈 التدريب اليدوي من الطرفية

```bash
python training/trainer.py --csv data/historical/AAPL.csv --model all
```

---

## 🧠 تكنولوجيا مستخدمة

- XGBoost
- LSTM (Keras / TensorFlow)
- Scikit-learn
- Streamlit
- Plotly
- GPT API (OpenAI)

---

## 🧪 قيد التطوير

- مقارنة رسومية بين النماذج
- نظام تنبيه ذكي للتغيرات الكبيرة
- دعم بيانات مباشرة (live API)

---

## 👨‍💻 فريق التطوير

تم التطوير بواسطة Autodev Code Hacker 2050 بإشراف فهد (lil-fahad)


---
### 🚀 شغّل المشروع مباشرة عبر Streamlit Cloud:
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

---

## Setup Instructions

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

---

## License

MIT

# SalesForecasting

# 📈 AI Sales Forecasting Dashboard

## 🚀 Project Overview

The AI Sales Forecasting Dashboard is an end-to-end data analytics and machine learning project that predicts future sales using historical sales data. The project combines Exploratory Data Analysis (EDA), Time Series Forecasting, Machine Learning, and an interactive Streamlit dashboard to help businesses make data-driven decisions.

The project evaluates multiple forecasting techniques including **SARIMA**, **Facebook Prophet**, and **XGBoost**, compares their performance, and identifies the best forecasting model based on evaluation metrics.

---

# 🎯 Problem Statement

Businesses require accurate sales forecasting to:

- Improve inventory management
- Optimize demand planning
- Reduce stock shortages
- Increase operational efficiency
- Support strategic business decisions

This project develops an intelligent forecasting system capable of predicting future monthly sales using historical sales records.

---

# 🎯 Objectives

- Clean and preprocess sales data
- Perform Exploratory Data Analysis (EDA)
- Analyze sales trends
- Build forecasting models
- Compare forecasting performance
- Develop an interactive dashboard
- Generate business insights

---

# 🗂 Dataset

Dataset Name:

**Superstore Sales Dataset**

Main Features:

- Order Date
- Ship Date
- Category
- Sub-Category
- Region
- Segment
- Sales

Dataset Size

- Rows: 9,800+
- Columns: 18

---

# 🛠 Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- Scikit-Learn
- Statsmodels
- Prophet
- XGBoost
- Joblib

---

# 📊 Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Forecasting Models
        │
        ▼
Model Comparison
        │
        ▼
Business Insights
        │
        ▼
Interactive Dashboard
```

---

# 📁 Project Structure

```
SalesForecasting_KetanMahakal/

│
├── app.py
├── analysis.ipynb
├── train.csv
├── README.md
├── requirements.txt
│
├── charts/
│   ├── task3_sarima.png
│   ├── task3_prophet_forecast.png
│   ├── task3_prophet_components.png
│   ├── task3_xgboost_forecast.png
│   ├── task4_category_sales.png
│   ├── task4_region_sales.png
│   └── task4_top_subcategory.png
│
├── outputs/
│   ├── best_xgboost_model.pkl
│   ├── category_sales.csv
│   ├── model_comparison.csv
│   ├── prophet_forecast.csv
│   ├── region_sales.csv
│   ├── subcategory_sales.csv
│   └── xgboost_predictions.csv
│
└── requirements.txt
```

---

# 📊 Exploratory Data Analysis

The project includes:

- Monthly Sales Trend
- Category-wise Sales Analysis
- Region-wise Sales Analysis
- Sub-Category Analysis
- Sales Distribution
- Business Insights

---

# 🤖 Forecasting Models

## 1. SARIMA

Seasonal Auto-Regressive Integrated Moving Average model used for monthly sales forecasting.

### Advantages

- Captures seasonality
- Good for time series forecasting

---

## 2. Prophet

Developed by Meta (Facebook).

### Features

- Trend Detection
- Seasonality
- Holiday Effects
- Easy to use

---

## 3. XGBoost

Extreme Gradient Boosting Regression Model.

### Advantages

- High prediction accuracy
- Handles nonlinear relationships
- Fast training
- Robust performance

---

# 📈 Model Evaluation

The models are evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

The best-performing model is selected based on the lowest error values.

---

# 💻 Streamlit Dashboard Features

The dashboard contains:

### 🏠 Home

- KPI Cards
- Monthly Sales Trend
- Dataset Preview

### 📊 Sales Analysis

- Sales Trend
- Monthly Sales
- Sales Distribution
- Box Plot

### 📦 Category Analysis

- Category Sales
- Sub-Category Sales
- Pie Charts

### 🌍 Region Analysis

- Region-wise Sales
- Regional Contribution

### 📈 Forecasting

- SARIMA Forecast
- Prophet Forecast
- XGBoost Forecast

### 📑 Model Comparison

- MAE
- RMSE
- MAPE
- Best Model Selection

### 💼 Business Insights

- Top Category
- Best Region
- Forecast Summary
- Recommendations

---

# 📊 Business Insights

Some important observations:

- Technology category generated the highest sales.
- West region contributed the maximum revenue.
- Monthly sales show seasonal patterns.
- XGBoost achieved the best forecasting accuracy.
- Forecasting can improve inventory planning and demand management.

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SalesForecasting_KetanMahakal.git
```

Go to project directory

```bash
cd SalesForecasting_KetanMahakal
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Dashboard

```bash
streamlit run app.py
```

---



# 📈 Future Improvements

- Deep Learning Forecasting (LSTM)
- Real-Time Sales Prediction
- Cloud Deployment
- Power BI Integration
- Customer Demand Forecasting
- Product Recommendation System

---

# 👨‍💻 Developer

**Ketan Mahakal**

B.E. Information Technology

L.D. College of Engineering

Ahmedabad, Gujarat

GitHub:
https://github.com/mahakal45x09


---

# 📄 License

This project is developed for educational and portfolio purposes.

---

# ⭐ Acknowledgements

- Streamlit
- Meta Prophet
- XGBoost
- Scikit-Learn
- Statsmodels
- Kaggle Superstore Dataset

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!

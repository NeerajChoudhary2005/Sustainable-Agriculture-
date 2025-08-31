=> Indian Crop Production Yield :-

This is an Python project designed to analyze and prepare agricultural datasets for predicting crop yields in India. The project provides a complete data pipeline including data cleaning, feature engineering, exploratory data analysis (EDA), and generation of model-ready datasets for machine learning applications.


=> Features :-

  Data Collection & Simulation: Reads real CSV datasets or generates synthetic data for crop yields, soil tests, weather, and market prices if data is missing.

  Data Cleaning: Handles missing values using median imputation, removes duplicates, filters invalid entries, and applies outlier clipping.

  Feature Engineering: Creates seasonal features, growing degree days (GDD), soil nutrient ratios (NPK), rainfall intensity categories, and interaction features like price    × rainfall.

  Time Alignment & Smart Merges: Aligns weekly weather data with crop yield dates and merges the most recent soil test and market price data.

  Exploratory Data Analysis (EDA): Automatically generates summary statistics, histograms, scatter plots, and correlation heatmaps to provide visual insights.

  Model-Ready Datasets: Produces cleaned and scaled datasets ready for regression models such as Random Forest, Linear Regression, or Gradient Boosting.


=> Folder Structure :-

  Sustainable-Agriculture/

  ├── Crop_Yield_Prediction.py                          # Main Python pipeline script

  ├── Indian_crop_production_yield_dataset/             # CSV datasets (crop, soil, weather, market prices)

  ├── README.md                                         # Project description


=> Technologies Used :-

  Python 3

  pandas, numpy

  matplotlib

  scikit-learn


=> Improvements / Enhancements :-

  The project includes synthetic data generation, advanced feature engineering (GDD, soil NPK ratios, rainfall categories), robust data cleaning, smart time-aligned merges,   automated EDA visualizations, and production of cleaned and scaled, model-ready datasets for predictive modeling.


=> Purpose :-

  This project is ideal for beginners and intermediate Python users interested in data science and agriculture, providing a foundation for crop yield prediction and           sustainable agriculture analytics in India.

Automobile Dataset - Exploratory Data Analysis (EDA)
    Project Overview
This project explores the Automobile dataset to analyze relationships between car attributes (engine size, horsepower, fuel type, body style, etc.) and price. The goal is to identify key patterns, detect anomalies, and understand correlations between features.
    Dataset
- Source: UCI Machine Learning Repository - Automobile Dataset
- Records:  205 rows
- Features: 26 columns (numeric + categorical)
    Key Steps in EDA
- Data cleaning (handling missing values, type conversions, rounding numeric features).
- Summary statistics & distributions.
- Barplots.
- Correlation analysis (heatmaps, scatter plots).
- Pairplots for visualizing price, horsepower, and engine size across body styles.
    Key Insights
- Price is strongly and positively correlated with horsepower and engine size.
- Vehicles with larger engines and higher horsepower tend to cost more, across all body styles.
- Outliers detected in price and horsepower suggest luxury or high-performance vehicles.
- Certain categorical features (e.g., fuel-type, aspiration) also show clear price differences.
    Project Structure
EDA_Automobile.ipynb   # Main notebook with analysis & plots
automobiles.csv        # Dataset
requirements.txt       # Python dependencies
README.md              # Project overview (this file)

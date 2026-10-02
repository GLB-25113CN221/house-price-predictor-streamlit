# 🏠 House Price Predictor

A machine learning web app that predicts the price of a house from its details.

## About the project

This is my first ML project. I trained regression models on a housing price dataset of 545 houses and built a Streamlit app where a user can enter house details and get a predicted price.

## Dataset

- 545 houses, 5 input features and 1 target
- **Features:** area, bedrooms, bathrooms, stories, parking
- **Target:** price

## Models trained

- Simple Linear Regression
- Multiple Linear Regression
- Polynomial Regression (degree 2 and 3)

All models were trained on 80% of the data and tested on the remaining 20%, then compared using MAE, MSE, RMSE, R² and Adjusted R².

## Result

The best model was **Multiple Linear Regression**, with a test R² of about 0.55 and an Adjusted R² of about 0.52.


## Built with

Python, pandas, scikit-learn, Streamlit

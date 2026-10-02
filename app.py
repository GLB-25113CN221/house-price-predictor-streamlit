import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")

st.title("🏠 House Price Predictor")
st.write("Enter the house details below:")

area = st.number_input("Area (sq ft)", min_value=500,
                       max_value=20000, value=5000, step=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=6, value=2)
stories = st.number_input("Stories", min_value=1, max_value=6, value=2)
parking = st.number_input("Parking spaces", min_value=0, max_value=5, value=1)

if st.button("Predict Price"):
    input_df = pd.DataFrame(
        [[area, bedrooms, bathrooms, stories, parking]],
        columns=["area", "bedrooms", "bathrooms", "stories", "parking"],
    )
    price = model.predict(input_df)[0]
    st.success(f"Estimated price: {price:,.0f}")

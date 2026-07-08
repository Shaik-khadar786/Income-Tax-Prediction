import streamlit as st
import joblib

# Load trained model
model = joblib.load("model/income_tax_model.pkl")

st.set_page_config(page_title="Income Tax Prediction", page_icon="💰")

st.title("💰 Income Tax Prediction")
st.write("Enter your details below to predict income tax.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

income = st.number_input("Annual Income (₹)", min_value=0, value=600000)

investment = st.number_input("Investments (₹)", min_value=0, value=120000)

deduction = st.number_input("Deductions (₹)", min_value=0, value=40000)

if st.button("Predict Tax"):
    sample = [[age, income, investment, deduction]]
    prediction = model.predict(sample)

    st.success(f"Predicted Tax: ₹ {prediction[0]:,.2f}")
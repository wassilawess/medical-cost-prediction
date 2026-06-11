import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("/ML-IA/medical-cost-prediction/models/medical_cost_model.pkl")

st.title("Medical Cost Prediction App")

age = st.number_input("Age", 18, 100)
bmi = st.number_input("BMI", 10.0, 50.0)
children = st.number_input("Children", 0, 10)

sex = st.selectbox("Sex", ["female", "male"])
smoker = st.selectbox("Smoker", ["no", "yes"])

region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

input_data = np.array([[
    age,
    bmi,
    children,
    sex_male,
    smoker_yes,
    region_northwest,
    region_southeast,
    region_southwest  
]])


prediction = model.predict(input_data)

st.success(f"Predicted Insurence Cost : ${prediction[0]:,.2f}")

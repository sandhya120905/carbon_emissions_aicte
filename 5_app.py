import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("forecasting_co2_emmision.pkl")

st.title("CO2 Emission Forecaster")
st.markdown("Enter vehicle specs to estimate CO₂ emissions (g/km)")

# Input fields for all 7 features
engine_size = st.number_input("Engine Size (liters)", min_value=0.5, max_value=8.0, step=0.1)
fuel_city = st.number_input("Fuel Consumption - City (L/100km)", min_value=1.0, max_value=30.0, step=0.1)
fuel_hwy = st.number_input("Fuel Consumption - Highway (L/100km)", min_value=1.0, max_value=30.0, step=0.1)
vehicle_weight = st.number_input("Vehicle Weight (kg)", min_value=500, max_value=3000, step=10)
cylinders = st.number_input("Number of Cylinders", min_value=2, max_value=16, step=1)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])

# Encode categorical features manually
fuel_type_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "Electric": 3}
transmission_map = {"Automatic": 1, "Manual": 0}

fuel_type_encoded = fuel_type_map[fuel_type]
transmission_encoded = transmission_map[transmission]

if st.button("Predict CO2 Emission"):
    input_data = np.array([[engine_size, fuel_city, fuel_hwy, vehicle_weight,
                            cylinders, fuel_type_encoded, transmission_encoded]])
    prediction = model.predict(input_data)
    st.success(f" Estimated CO₂ Emission: **{prediction[0]:.2f} g/km**")

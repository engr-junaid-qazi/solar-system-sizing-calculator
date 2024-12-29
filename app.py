
# Install required libraries
# !pip install streamlit

import streamlit as st
import numpy as np

# Constants
SOLAR_PANEL_WATTAGE = 600  # Mono-facial solar panel rating in Watts
INVERTER_EXTRA_FACTOR = 1.3

def calculate_solar_system(load_watts, battery_ah_rating, battery_voltage, backup_hours):
    # Calculate the number of solar panels
    num_solar_panels = np.ceil(load_watts / SOLAR_PANEL_WATTAGE)
    
    # Calculate inverter capacity
    inverter_capacity = load_watts * INVERTER_EXTRA_FACTOR

    # Battery calculations
    total_watt_hours_per_battery = battery_voltage * battery_ah_rating
    backup_time_per_battery = total_watt_hours_per_battery / load_watts
    num_batteries = np.ceil(backup_hours / backup_time_per_battery)

    return {
        "num_solar_panels": int(num_solar_panels),
        "inverter_capacity": round(inverter_capacity, 2),
        "num_batteries": int(num_batteries),
    }

# Streamlit app
st.title("Solar System Sizing Calculator")
st.header("Enter Your System Details")

# User inputs
load_watts = st.number_input("Enter total load in watts:", min_value=1, step=1, value=1000)
battery_ah_rating = st.number_input("Enter battery ampere-hours (Ah) rating:", min_value=1, step=1, value=200)
battery_voltage = st.selectbox("Select battery system voltage (V):", [12, 24, 48], index=1)
backup_hours = st.number_input("Enter desired backup time in hours:", min_value=1, step=1, value=4)

# Calculate and display results
if st.button("Calculate Solar Sizing"):
    result = calculate_solar_system(load_watts, battery_ah_rating, battery_voltage, backup_hours)

    st.subheader("Sizing Results")
    st.write(f"**Number of Solar Panels (600W each):** {result['num_solar_panels']}")
    st.write(f"**Inverter Capacity (W):** {result['inverter_capacity']}")
    st.write(f"**Number of Batteries:** {result['num_batteries']}")
st.caption("Designed for solar sizing in regions with seasonal sunlight variations.")

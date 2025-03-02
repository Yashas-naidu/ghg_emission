import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(page_title="Carbon Emissions Calculator", layout="wide")
st.title("Carbon Emissions Calculator")

# Backend API URL
BACKEND_URL = "http://localhost:5000/api/carbon/mobile"

# Form for customer information
st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    customer_id = st.text_input("Customer ID", "4914369288732672")
    company_id = st.text_input("Company ID", "1913649000087552")
    company_name = st.text_input("Company Name", "Clyde Patterson")
    department_id = st.text_input("Department ID", "4729605648809984")
    department_name = st.text_input("Department Name", "Belle Pearson")

with col2:
    request_type = st.selectbox("Request Type", ["ACTUAL", "PLANNED"])
    country = st.text_input("Country", "Zimbabwe")
    state_province = st.text_input("State/Province", "PE")
    zip_post_code = st.text_input("ZIP/Postal Code", "R0K 8C5")
    city = st.text_input("City", "Cowavode")

# Form for site information
st.header("Site Information")

col1, col2 = st.columns(2)

with col1:
    site_id = st.text_input("Site ID", "7671272286715904")
    site_name = st.text_input("Site Name", "Genevieve Sparks")
    
with col2:
    building_id = st.text_input("Building ID", "8395630766456832")
    building_name = st.text_input("Building Name", "Madge Guerrero")

# Form for time period
st.header("Time Period")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", min_value=2000, max_value=2030, value=2021)
    
with col2:
    month = st.number_input("Month", min_value=1, max_value=12, value=1)

# Form for activity data
st.header("Activity Data")

vehicle_types = [
    "Heavy Duty Vehicle – Rigid – Gasoline – Year 2005-present",
    "Heavy Duty Vehicle – Rigid – Diesel – Year 2005-present",
    "Passenger Car – Gasoline – Year 2005-present",
    "Passenger Car – Diesel – Year 2005-present"
]

fuel_types = ["Gasoline", "Diesel"]
fuel_units = ["US Gallon", "Liter", "UK Gallon"]

col1, col2 = st.columns(2)

with col1:
    vehicle_type = st.selectbox("Vehicle Type", vehicle_types)
    fuel_used = st.selectbox("Fuel Used", fuel_types)
    
with col2:
    fuel_amount = st.text_input("Fuel Amount", "20")
    unit_of_fuel_amount = st.selectbox("Unit of Fuel Amount", fuel_units)

# Calculate button
if st.button("Calculate Carbon Emissions"):
    # Construct request payload
    request_payload = {
        "customID": {
            "id": customer_id
        },
        "onBehalfOfClient": {
            "companyId": company_id,
            "companyName": company_name
        },
        "organisation": {
            "departmentId": department_id,
            "departmentName": department_name
        },
        "requestType": request_type,
        "location": {
            "country": country,
            "stateProvince": state_province,
            "zipPostCode": zip_post_code,
            "city": city
        },
        "site": {
            "siteId": site_id,
            "siteName": site_name,
            "buildingId": building_id,
            "buildingName": building_name
        },
        "timePeriod": {
            "year": int(year),
            "month": int(month)
        },
        "activityData": {
            "vehicleType": vehicle_type,
            "fuelUsed": fuel_used,
            "fuelAmount": fuel_amount,
            "unitOfFuelAmount": unit_of_fuel_amount
        }
    }
    
    st.subheader("Request Payload")
    st.json(request_payload)
    
    try:
        # Send request to backend
        response = requests.post(BACKEND_URL, json=request_payload)
        response.raise_for_status()
        
        # Display results
        result = response.json()
        st.subheader("Carbon Emissions Results")
        
        # Convert to DataFrame for display
        df_res = pd.json_normalize(result)
        st.dataframe(df_res)
        
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with backend: {str(e)}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
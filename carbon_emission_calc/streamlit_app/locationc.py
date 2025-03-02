import streamlit as st
import requests
import pandas as pd

st.title("🌍 Carbon Footprint Calculator")

# Backend API URL
API_URL = "http://127.0.0.1:5000/calculate_emission"

# User Inputs
st.header("Enter Energy Consumption Details")

company_id = st.text_input("Company ID", "877889877")
company_name = st.text_input("Company Name", "Retailer_A")
department_id = st.text_input("Department ID", "384834")
department_name = st.text_input("Department Name", "Acme_retail")
country = st.text_input("Country", "England")
city = st.text_input("City", "London")
commodity = st.selectbox("Energy Type", ["Electricity", "Natural Gas", "Coal"])
energy_consumed = st.number_input("Energy Consumed (MWh)", min_value=0.1, value=100.0)

if st.button("Calculate Carbon Emission"):
    request_payload = {
        "customID": {"id": "Retailer_A_mobile_31234"},
        "onBehalfOfClient": {"companyId": company_id, "companyName": company_name},
        "organisation": {"departmentId": department_id, "departmentName": department_name},
        "requestType": "ACTUAL",
        "location": {"country": country, "stateProvince": "", "zipPostCode": "", "city": city},
        "site": {"siteId": "T2383823", "siteName": "Retailer_A_South_Bank", "buildingId": "B38383", "buildingName": "Building_6"},
        "timePeriod": {"year": 2021, "month": 1},
        "activityData": {"commodity": commodity, "energyConsumedMWh": str(energy_consumed)}
    }

    response = requests.post(API_URL, json=request_payload)
    
    if response.status_code == 200:
        result = response.json()
        df = pd.json_normalize(result)
        st.subheader("Carbon Footprint Result")
        st.table(df)
    else:
        st.error("Error fetching data from API. Please check input values.")


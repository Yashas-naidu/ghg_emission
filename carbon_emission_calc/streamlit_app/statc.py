import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(page_title="Carbon Emissions Calculator", layout="wide")
st.title("Carbon Emissions Calculator")

# Create tabs for different calculators
tab1, tab2 = st.tabs(["Mobile Emissions", "Stationary Emissions"])

# Backend API URLs
BACKEND_URL_MOBILE = "http://localhost:5000/api/carbon/mobile"
BACKEND_URL_STATIONARY = "http://localhost:5000/api/carbon/stationary"

with tab1:
    st.header("Mobile Emissions Calculator")
    
    # Form for customer information
    st.subheader("Customer Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mobile_customer_id = st.text_input("Customer ID", "4914369288732672", key="mobile_cust_id")
        mobile_company_id = st.text_input("Company ID", "1913649000087552", key="mobile_comp_id")
        mobile_company_name = st.text_input("Company Name", "Clyde Patterson", key="mobile_comp_name")
        mobile_department_id = st.text_input("Department ID", "4729605648809984", key="mobile_dept_id")
        mobile_department_name = st.text_input("Department Name", "Belle Pearson", key="mobile_dept_name")
    
    with col2:
        mobile_request_type = st.selectbox("Request Type", ["ACTUAL", "PLANNED"], key="mobile_req_type")
        mobile_country = st.text_input("Country", "Zimbabwe", key="mobile_country")
        mobile_state_province = st.text_input("State/Province", "PE", key="mobile_state")
        mobile_zip_post_code = st.text_input("ZIP/Postal Code", "R0K 8C5", key="mobile_zip")
        mobile_city = st.text_input("City", "Cowavode", key="mobile_city")
    
    # Form for site information
    st.subheader("Site Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mobile_site_id = st.text_input("Site ID", "7671272286715904", key="mobile_site_id")
        mobile_site_name = st.text_input("Site Name", "Genevieve Sparks", key="mobile_site_name")
        
    with col2:
        mobile_building_id = st.text_input("Building ID", "8395630766456832", key="mobile_bldg_id")
        mobile_building_name = st.text_input("Building Name", "Madge Guerrero", key="mobile_bldg_name")
    
    # Form for time period
    st.subheader("Time Period")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mobile_year = st.number_input("Year", min_value=2000, max_value=2030, value=2021, key="mobile_year")
        
    with col2:
        mobile_month = st.number_input("Month", min_value=1, max_value=12, value=1, key="mobile_month")
    
    # Form for activity data
    st.subheader("Activity Data")
    
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
        vehicle_type = st.selectbox("Vehicle Type", vehicle_types, key="vehicle_type")
        fuel_used = st.selectbox("Fuel Used", fuel_types, key="fuel_used")
        
    with col2:
        fuel_amount = st.text_input("Fuel Amount", "20", key="mobile_fuel_amount")
        unit_of_fuel_amount = st.selectbox("Unit of Fuel Amount", fuel_units, key="mobile_fuel_unit")
    
    # Calculate button
    if st.button("Calculate Mobile Emissions"):
        # Construct request payload
        mobile_request_payload = {
            "customID": {
                "id": mobile_customer_id
            },
            "onBehalfOfClient": {
                "companyId": mobile_company_id,
                "companyName": mobile_company_name
            },
            "organisation": {
                "departmentId": mobile_department_id,
                "departmentName": mobile_department_name
            },
            "requestType": mobile_request_type,
            "location": {
                "country": mobile_country,
                "stateProvince": mobile_state_province,
                "zipPostCode": mobile_zip_post_code,
                "city": mobile_city
            },
            "site": {
                "siteId": mobile_site_id,
                "siteName": mobile_site_name,
                "buildingId": mobile_building_id,
                "buildingName": mobile_building_name
            },
            "timePeriod": {
                "year": int(mobile_year),
                "month": int(mobile_month)
            },
            "activityData": {
                "vehicleType": vehicle_type,
                "fuelUsed": fuel_used,
                "fuelAmount": fuel_amount,
                "unitOfFuelAmount": unit_of_fuel_amount
            }
        }
        
        st.subheader("Request Payload")
        st.json(mobile_request_payload)
        
        try:
            # Send request to backend
            response = requests.post(BACKEND_URL_MOBILE, json=mobile_request_payload)
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

with tab2:
    st.header("Stationary Emissions Calculator")
    
    # Form for customer information
    st.subheader("Customer Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        stationary_customer_id = st.text_input("Customer ID", "4610500776165376", key="stat_cust_id")
        stationary_company_id = st.text_input("Company ID", "5882719762382848", key="stat_comp_id")
        stationary_company_name = st.text_input("Company Name", "Eddie Clayton", key="stat_comp_name")
        stationary_department_id = st.text_input("Department ID", "7077695919751168", key="stat_dept_id")
        stationary_department_name = st.text_input("Department Name", "Lida Schmidt", key="stat_dept_name")
    
    with col2:
        stationary_request_type = st.selectbox("Request Type", ["ACTUAL", "PLANNED"], key="stat_req_type")
        stationary_country = st.text_input("Country", "Angola", key="stat_country")
        stationary_state_province = st.text_input("State/Province", "MB", key="stat_state")
        stationary_zip_post_code = st.text_input("ZIP/Postal Code", "G8L 7Y0", key="stat_zip")
        stationary_city = st.text_input("City", "Huemodu", key="stat_city")
    
    # Form for site information
    st.subheader("Site Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        stationary_site_id = st.text_input("Site ID", "5688215832887296", key="stat_site_id")
        stationary_site_name = st.text_input("Site Name", "Beulah Rivera", key="stat_site_name")
        
    with col2:
        stationary_building_id = st.text_input("Building ID", "1533911203053568", key="stat_bldg_id")
        stationary_building_name = st.text_input("Building Name", "Andrew Martin", key="stat_bldg_name")
    
    # Form for time period
    st.subheader("Time Period")
    
    col1, col2 = st.columns(2)
    
    with col1:
        stationary_year = st.number_input("Year", min_value=2000, max_value=2030, value=2021, key="stat_year")
        
    with col2:
        stationary_month = st.number_input("Month", min_value=1, max_value=12, value=1, key="stat_month")
    
    # Form for activity data
    st.subheader("Activity Data")
    
    sectors = ["Energy", "Manufacturing", "Commercial", "Residential"]
    fuel_names = ["Coal tar", "Natural gas", "Diesel", "Fuel oil", "LPG"]
    fuel_units = ["metric ton", "kg", "liter", "US gallon"]
    hv_basis_options = ["Not applicable", "HHV", "LHV"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        sector = st.selectbox("Sector", sectors, key="sector")
        fuel_name = st.selectbox("Fuel Name", fuel_names, key="fuel_name")
        
    with col2:
        stationary_fuel_amount = st.number_input("Fuel Amount", min_value=0.1, value=1.5, step=0.1, key="stat_fuel_amount")
        stationary_fuel_unit = st.selectbox("Fuel Unit", fuel_units, key="stat_fuel_unit")
        hv_basis = st.selectbox("HV Basis", hv_basis_options, key="hv_basis")
    
    # Calculate button
    if st.button("Calculate Stationary Emissions"):
        # Construct request payload
        stationary_request_payload = {
            "customID": {
                "id": stationary_customer_id
            },
            "onBehalfOfClient": {
                "companyId": stationary_company_id,
                "companyName": stationary_company_name
            },
            "organisation": {
                "departmentId": stationary_department_id,
                "departmentName": stationary_department_name
            },
            "requestType": stationary_request_type,
            "location": {
                "country": stationary_country,
                "stateProvince": stationary_state_province,
                "zipPostCode": stationary_zip_post_code,
                "city": stationary_city
            },
            "site": {
                "siteId": stationary_site_id,
                "siteName": stationary_site_name,
                "buildingId": stationary_building_id,
                "buildingName": stationary_building_name
            },
            "timePeriod": {
                "year": int(stationary_year),
                "month": int(stationary_month)
            },
            "activityData": {
                "sector": sector,
                "fuelName": fuel_name,
                "fuelAmount": float(stationary_fuel_amount),
                "fuelUnit": stationary_fuel_unit,
                "hvBasis": hv_basis
            }
        }
        
        st.subheader("Request Payload")
        st.json(stationary_request_payload)
        
        try:
            # Send request to backend
            response = requests.post(BACKEND_URL_STATIONARY, json=stationary_request_payload)
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
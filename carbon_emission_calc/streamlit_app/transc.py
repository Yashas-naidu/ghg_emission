# streamlit_app.py (Streamlit Frontend for Transportation and Distribution)
import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

# Set page title
st.set_page_config(page_title="Transportation & Distribution API Interface", layout="wide")
st.title("Transportation & Distribution Carbon API Interface")

# API endpoint configuration
FLASK_API_URL = "http://localhost:5000/transportation_api"  # Update this with your Flask API URL when deploying

# Create form sections
st.header("Request Parameters")

with st.expander("Customer Information", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        customer_id = st.text_input("Customer ID", "4475224896569344")
    
    st.subheader("On Behalf Of Client")
    client_col1, client_col2 = st.columns(2)
    with client_col1:
        company_id = st.text_input("Company ID", "3803802285113344")
    with client_col2:
        company_name = st.text_input("Company Name", "Cornelia Robinson")
    
    st.subheader("Organization")
    org_col1, org_col2 = st.columns(2)
    with org_col1:
        department_id = st.text_input("Department ID", "8401528882724864")
    with org_col2:
        department_name = st.text_input("Department Name", "Loretta Foster")
    
    request_type = st.selectbox("Request Type", ["ACTUAL", "FORECAST"])

with st.expander("Location Information", expanded=True):
    loc_col1, loc_col2 = st.columns(2)
    with loc_col1:
        country = st.text_input("Country", "Norway")
        state_province = st.text_input("State/Province", "NL")
    with loc_col2:
        zip_post_code = st.text_input("Zip/Post Code", "M7K 7O4")
        city = st.text_input("City", "Zaluwva")
    
    st.subheader("Site Details")
    site_col1, site_col2 = st.columns(2)
    with site_col1:
        site_id = st.text_input("Site ID", "1787113341190144")
        site_name = st.text_input("Site Name", "Ivan Thornton")
    with site_col2:
        building_id = st.text_input("Building ID", "7003629443612672")
        building_name = st.text_input("Building Name", "Vera Rhodes")
    
    st.subheader("Time Period")
    time_col1, time_col2 = st.columns(2)
    with time_col1:
        year = st.number_input("Year", min_value=2000, max_value=datetime.now().year, value=2021)
    with time_col2:
        month = st.number_input("Month", min_value=1, max_value=12, value=1)

with st.expander("Transportation & Distribution Data", expanded=True):
    activity_type = st.selectbox(
        "Type of Activity Data", 
        ["Weight Distance", "Distance Only", "Fuel Based"]
    )
    
    vehicle_types = [
        "Road Vehicle - HGV - Articulated - Engine Size 3.5 - 33 tonnes",
        "Road Vehicle - HGV - Rigid - Engine Size >3.5-7.5 tonnes",
        "Road Vehicle - HGV - Rigid - Engine Size >7.5-17 tonnes",
        "Road Vehicle - HGV - Rigid - Engine Size >17 tonnes",
        "Road Vehicle - LGV - Average",
        "Rail - Freight Train - Diesel",
        "Rail - Freight Train - Electric",
        "Sea Tanker - Bulk carrier",
        "Sea Tanker - Container Ship",
        "Sea Tanker - General cargo",
        "Sea Tanker - Refrigerated cargo",
        "Sea Tanker - Roll-on/roll-off ship",
        "Air Freight - Domestic"
    ]
    vehicle_type = st.selectbox("Vehicle Type", vehicle_types)
    
    col1, col2 = st.columns(2)
    with col1:
        distance_travelled = st.text_input("Distance Travelled", "2000")
        total_weight_of_freight = st.text_input("Total Weight of Freight", "100")
        number_of_passengers = st.number_input("Number of Passengers", value=15)
    
    with col2:
        unit_of_measurement = st.selectbox(
            "Unit of Measurement", 
            ["Tonne Mile", "Tonne Kilometer", "Kilometer", "Mile"]
        )
        fuel_used = st.text_input("Fuel Used", "kugitewimnimel")
        fuel_amount = st.text_input("Fuel Amount", "8858693217026048")
        unit_of_fuel_amount = st.text_input("Unit of Fuel Amount", "1451934150033408")

# Submit button
if st.button("Submit Request"):
    with st.spinner("Processing..."):
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
                "typeOfActivityData": activity_type,
                "vehicleType": vehicle_type,
                "distanceTravelled": distance_travelled,
                "totalWeightOfFreight": total_weight_of_freight,
                "numberOfPassengers": number_of_passengers,
                "unitOfMeasurement": unit_of_measurement,
                "fuelUsed": fuel_used,
                "fuelAmount": fuel_amount,
                "unitOfFuelAmount": unit_of_fuel_amount
            }
        }
        
        # Display request payload
        st.subheader("Request Payload")
        st.json(request_payload)
        
        try:
            # Send request to Flask backend
            response = requests.post(FLASK_API_URL, json=request_payload)
            response.raise_for_status()
            
            # Display response
            st.subheader("API Response")
            response_data = response.json()
            st.json(response_data)
            
            # Display as table if possible
            try:
                df_res = pd.json_normalize(response_data)
                st.subheader("Response as Table")
                st.dataframe(df_res)
            except Exception as e:
                st.warning(f"Could not display as table: {str(e)}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with API: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
# streamlit_app.py (Streamlit Frontend)
import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

# Set page title
st.set_page_config(page_title="Carbon API Interface", layout="wide")
st.title("Carbon Market API Interface")

# API endpoint configuration
FLASK_API_URL = "http://localhost:5000/carbon_api"  # Update this with your Flask API URL when deploying

# Create form sections
st.header("Request Parameters")

with st.expander("Customer Information", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        customer_id = st.text_input("Customer ID", "1170497970634752")
    
    st.subheader("On Behalf Of Client")
    client_col1, client_col2 = st.columns(2)
    with client_col1:
        company_id = st.text_input("Company ID", "2969842132975616")
    with client_col2:
        company_name = st.text_input("Company Name", "Lula Jefferson")
    
    st.subheader("Organization")
    org_col1, org_col2 = st.columns(2)
    with org_col1:
        department_id = st.text_input("Department ID", "3717370277265408")
    with org_col2:
        department_name = st.text_input("Department Name", "Mina Williams")
    
    request_type = st.selectbox("Request Type", ["ACTUAL", "FORECAST"])

with st.expander("Location Information", expanded=True):
    loc_col1, loc_col2 = st.columns(2)
    with loc_col1:
        country = st.text_input("Country", "Suriname")
        state_province = st.text_input("State/Province", "BC")
    with loc_col2:
        zip_post_code = st.text_input("Zip/Post Code", "J3M 3U2")
        city = st.text_input("City", "Cakompu")
    
    st.subheader("Site Details")
    site_col1, site_col2 = st.columns(2)
    with site_col1:
        site_id = st.text_input("Site ID", "562924481413120")
        site_name = st.text_input("Site Name", "Mildred Hoffman")
    with site_col2:
        building_id = st.text_input("Building ID", "933173693251584")
        building_name = st.text_input("Building Name", "Kenneth Roberts")
    
    st.subheader("Time Period")
    time_col1, time_col2 = st.columns(2)
    with time_col1:
        year = st.number_input("Year", min_value=2000, max_value=datetime.now().year, value=2021)
    with time_col2:
        month = st.number_input("Month", min_value=1, max_value=12, value=1)

with st.expander("Activity Data", expanded=True):
    commodity = st.selectbox("Commodity", ["electricity", "gas", "other"])
    energy_consumed = st.text_input("Energy Consumed (MWh)", "1000")
    energy_supplier_residual_ef = st.text_input("Energy Supplier Residual EF", "na")
    
    st.subheader("REC Information")
    rec_col1, rec_col2 = st.columns(2)
    with rec_col1:
        supplier_name_rec = st.text_input("Supplier Name (REC)", "XXX")
        energy_purchased_rec = st.text_input("Energy Purchased (MWh) (REC)", "20")
        emission_factor_rec = st.text_input("Emission Factor (REC)", "0.03")
        source_rec = st.text_input("Source (REC)", "solar")
        expiry_date_rec = st.text_input("Expiry Date (REC)", "12-31-2020")
    with rec_col2:
        instrument_type_rec = st.text_input("Instrument Type (REC)", "bundled")
        tracking_system_rec = st.text_input("Tracking System (REC)", "ERCOT")
        certificate_number_rec = st.text_input("Certificate Number (REC)", "1168")
    
    st.subheader("REDI Information")
    redi_col1, redi_col2 = st.columns(2)
    with redi_col1:
        supplier_name_redi = st.text_input("Supplier Name (REDI)", "Apex Clean Energy")
        energy_purchased_redi = st.text_input("Energy Purchased (MWh) (REDI)", "10")
        emission_factor_redi = st.text_input("Emission Factor (REDI)", "na")
    with redi_col2:
        source_redi = st.text_input("Source (REDI)", "wind")
        expiry_date_redi = st.text_input("Expiry Date (REDI)", "12-31-2020")
        certificate_number_redi = st.text_input("Certificate Number (REDI)", "1078")
    
    st.subheader("DEPC Information")
    depc_col1, depc_col2 = st.columns(2)
    with depc_col1:
        supplier_name_depc = st.text_input("Supplier Name (DEPC)", "Invenergy")
        energy_purchased_depc = st.text_input("Energy Purchased (MWh) (DEPC)", "10")
        supplied_emission_factor_depc = st.text_input("Supplied Emission Factor (DEPC)", "0.25")
    with depc_col2:
        expiry_date_depc = st.text_input("Expiry Date (DEPC)", "12-31-2020")
        certificate_number_depc = st.text_input("Certificate Number (DEPC)", "2089")

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
                "commodity": commodity,
                "energyConsumedMWh": energy_consumed,
                "energySupplierResidualEF": energy_supplier_residual_ef,
                "supplierNameREC": supplier_name_rec,
                "energyPurchasedMWhREC": energy_purchased_rec,
                "emissionFactorREC": emission_factor_rec,
                "sourceREC": source_rec,
                "expiryDateREC": expiry_date_rec,
                "instrumentTypeREC": instrument_type_rec,
                "trackingSystemREC": tracking_system_rec,
                "certificateNumberREC": certificate_number_rec,
                "supplierNameREDI": supplier_name_redi,
                "energyPurchasedMWhREDI": energy_purchased_redi,
                "emissionFactorREDI": emission_factor_redi,
                "sourceREDI": source_redi,
                "expiryDateREDI": expiry_date_redi,
                "certificateNumberREDI": certificate_number_redi,
                "supplierNameDEPC": supplier_name_depc,
                "energyPurchasedMWhDEPC": energy_purchased_depc,
                "suppliedEmissionFactorDEPC": supplied_emission_factor_depc,
                "expiryDateDEPC": expiry_date_depc,
                "certificateNumberDEPC": certificate_number_depc
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
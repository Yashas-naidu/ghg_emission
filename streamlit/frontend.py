import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

st.set_page_config(page_title="Carbon Emissions Calculator", layout="wide")
st.title("Carbon Emissions Calculator")

# Create tabs for different calculators
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Mobile Emissions", "Stationary Emissions","Fugitive Emissions","Location Emissions","Market Emissions","Transport Emissions"])

# Backend API URLs
BACKEND_URL_MOBILE = "http://localhost:5000/api/carbon/mobile"
BACKEND_URL_STATIONARY = "http://localhost:5000/api/carbon/stationary"
BACKEND_URL_FUGITIVE = "http://localhost:5000/api/carbon/fugitive"
BACKEND_URL_LOCATION = "http://localhost:5000/api/carbon/location"
BACKEND_URL_MARKET = "http://localhost:5000/api/carbon/market"
BACKEND_URL_TRANSPORT = "http://localhost:5000/api/carbon/transport"

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
        with st.spinner("Processing..."):
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
        
        # st.subheader("Request Payload")
        # st.json(mobile_request_payload)
        
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
        
        # st.subheader("Request Payload")
        # st.json(stationary_request_payload)
        
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

with tab3:
    st.header("Fugitive Emissions Calcualtor")
    st.subheader("Customer Information")

    col1,col2 = st.columns(2)

    with col1:
        fugitive_customer_id = st.text_input("Customer ID", "4914369288732672", key="fug_cust_id")
        fugitive_company_id = st.text_input("Company ID", "1913649000087552", key="fug_comp_id")
        fugitive_company_name = st.text_input("Company Name", "Clydefeld", key="fug_comp_name")
        fugitive_department_id = st.text_input("Department ID", "4729605648809984", key="fug_dept_id")
        fugitive_department_name = st.text_input("Department Name", "Belle Pearson", key="fug_dept_name")

    with col2:
        fugitive_request_type = st.selectbox("Request Type", ["ACTUAL", "PLANNED"], key="fug_req_type")
        fugitive_country = st.text_input("Country", "Zimbabwe", key="fug_country")
        fugitive_state_province = st.text_input("State/Province", "PE", key="fug_state")
        fugitive_zip_post_code = st.text_input("ZIP/Postal Code", "R0K 8C5", key="fug_zip")
        fugitive_city = st.text_input("City", "Cowavode", key="fug_city")

    st.subheader("Site Information")

    col1, col2 = st.columns(2)

    with col1:
        fugitive_site_id = st.text_input("Site ID", "T2383823", key="fug_site_id")
        fugitive_site_name = st.text_input("Site Name", "Retailer_A_South_Bank", key="fug_site_name")

    with col2:
        fugitive_building_id = st.text_input("Building ID", "B38383", key="fug_building_id")
        fugitive_building_name = st.text_input("Building Name", "Building_6", key="fug_building_name")

    st.subheader("Time Period")

    col1, col2 = st.columns(2)

    with col1:
        fugitive_year = st.number_input("Year", 2021, key="fug_year")

    with col2:
        fugitive_month = st.number_input("Month", 1, key="fug_month")
        
    st.subheader("Refrigerant Activity Data")

    col1, col2 = st.columns(2)

    with col1:
        refrigerant_name = st.text_input("Refrigerant Name", "R-404A", key="refrigerant_name")
        refrigerant_inventory_beginning = st.text_input("Refrigerant Inventory Beginning", "10", key="inventory_begin")
        refrigerants_purchased_from_producers = st.text_input("Refrigerants Purchased From Producers", "6", key="purchased_producers")
        refrigerants_added_to_equipment = st.text_input("Refrigerants Added To Equipment", "3", key="added_equipment")
        refrigerant_sales = st.text_input("Refrigerant Sales", "3", key="sales")
        refrigerant_returned_to_suppliers = st.text_input("Refrigerant Returned To Suppliers", "1", key="returned_suppliers")
        total_charge_new_equipment = st.text_input("Total Charge New Equipment", "0", key="total_charge_new")
        original_charge_equipment = st.text_input("Original Charge Equipment", "0", key="original_charge")
        unit_of_measurement = st.text_input("Unit Of Measurement", "kilogram", key="unit_measurement")

    with col2:
        refrigerant_inventory_end = st.text_input("Refrigerant Inventory End", "2", key="inventory_end")
        refrigerants_provided_by_manufacturers = st.text_input("Refrigerants Provided By Manufacturers", "2", key="provided_manufacturers")
        refrigerant_returned_after_recycling = st.text_input("Refrigerant Returned After Recycling", "0", key="returned_recycling")
        refrigerant_left_in_equipment = st.text_input("Refrigerant Left In Equipment", "4", key="left_equipment")
        refrigerant_for_recycling = st.text_input("Refrigerant For Recycling", "0", key="for_recycling")
        refrigerant_for_destruction = st.text_input("Refrigerant For Destruction", "0", key="for_destruction")
        total_charge_retrofitted = st.text_input("Total Charge Retrofitted", "0", key="total_charge_retro")
        total_charge_equipment_retro_away = st.text_input("Total Charge Equipment Retro Away", "0", key="charge_retro_away")

    if st.button("Calculate Carbon Footprint"):
        fugitive_request_payload = {
        "customID": {"id": fugitive_company_id},
        "onBehalfOfClient": {"companyId": fugitive_company_id, "companyName": fugitive_company_name},
        "organisation": {"departmentId": fugitive_department_id, "departmentName": fugitive_department_name},
        "requestType": fugitive_request_type,
        "location": {
            "country": fugitive_country, "stateProvince": fugitive_state_province, "zipPostCode": fugitive_zip_post_code, "city": fugitive_city
        },
        "site": {
            "siteId": fugitive_site_id, "siteName": fugitive_site_name, "buildingId": fugitive_building_id, "buildingName": fugitive_building_name
        },
        "timePeriod": {"year": fugitive_year, "month": fugitive_month},
        "activityData": {
            "refrigerantName": refrigerant_name,
            "refrigerantInventoryBeginning": refrigerant_inventory_beginning,
            "refrigerantInventoryEnd": refrigerant_inventory_end,
            "refrigerantsPurchasedFromProducers": refrigerants_purchased_from_producers,
            "refrigerantsProvidedByManufacturers": refrigerants_provided_by_manufacturers,
            "refrigerantsAddedToEquipment": refrigerants_added_to_equipment,
            "refrigerantReturnedAfterRecycling": refrigerant_returned_after_recycling,
            "refrigerantSales": refrigerant_sales,
            "refrigerantLeftInEquipment": refrigerant_left_in_equipment,
            "refrigerantReturnedToSuppliers": refrigerant_returned_to_suppliers,
            "refrigerantForRecycling": refrigerant_for_recycling,
            "refrigerantForDestruction": refrigerant_for_destruction,
            "totalChargeNewEquipment": total_charge_new_equipment,
            "totalChargeRetrofitted": total_charge_retrofitted,
            "originalChargeEquipment": original_charge_equipment,
            "totalChargeEquipmentRetroAway": total_charge_equipment_retro_away,
            "unitOfMeasurement": unit_of_measurement
        }
    }
        # st.subheader("Request Payload")
        # st.json(fugitive_request_payload)
    
        try:
        # Send request to backend
            response = requests.post(BACKEND_URL_FUGITIVE, json=fugitive_request_payload)
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

with tab4:
    st.header("Location Emission Calculator")

    st.subheader("Customer Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        location_customer_id = st.text_input("Customer ID", "4610500776165376", key="loc_cust_id")
        location_company_id = st.text_input("Company ID", "5882719762382848", key="loc_comp_id")
        location_company_name = st.text_input("Company Name", "Eddie Clayton", key="loc_comp_name")
        location_department_id = st.text_input("Department ID", "7077695919751168", key="loc_dept_id")
        location_department_name = st.text_input("Department Name", "Lida Schmidt", key="loc_dept_name")
    
    with col2:
        location_country = st.text_input("Country", "England", key="loc_country")
        location_city = st.text_input("City", "London", key="loc_city")
        location_commodity = st.selectbox("Energy Type", ["Electricity", "Natural Gas", "Coal"], key="loc_commodity")
        location_energy_consumed = st.number_input("Energy Consumed (MWh)", min_value=0.1, value=100.0, key="loc_energy")

    if st.button("Calculate Carbon Emission"):
        location_request_payload = {
            "customID": {"id": location_customer_id},
            "onBehalfOfClient": {"companyId": location_company_id, "companyName": location_company_name},
            "organisation": {"departmentId": location_department_id, "departmentName": location_department_name},
            "requestType": "ACTUAL",
            "location": {"country": location_country, "stateProvince": "", "zipPostCode": "", "city": location_city},
            "site": {"siteId": "T2383823", "siteName": "Retailer_A_South_Bank", "buildingId": "B38383", "buildingName": "Building_6"},
            "timePeriod": {"year": 2021, "month": 1},
            "activityData": {"commodity": location_commodity, "energyConsumedMWh": str(location_energy_consumed)}
        }

        # st.subheader("Request Payload")
        # st.json(location_request_payload)

        try:
        # Send request to backend
           response = requests.post(BACKEND_URL_LOCATION, json=location_request_payload)
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

with tab5:
    st.header("Market Emission Calculator")
    st.subheader("Customer Information")

    col1, col2 = st.columns(2)

    with col1:
        market_customer_id = st.text_input("Customer ID", "4610500776165376", key="mar_cust_id")
        market_company_id = st.text_input("Company ID", "5882719762382848", key="mar_comp_id")
        market_company_name = st.text_input("Company Name", "Eddie Clayton", key="mar_comp_name")
        market_department_id = st.text_input("Department ID", "7077695919751168", key="mar_dept_id")
        market_department_name = st.text_input("Department Name", "Lida Schmidt", key="mar_dept_name")

    with col2:
        market_request_type = st.selectbox("Request Type", ["ACTUAL", "FUTURE"], key="mar_request_type")
        market_country = st.text_input("Country", "Suriname", key="mar_country")
        market_state_province = st.text_input("State/Province", "BC", key="mar_state")
        market_zip_post_code = st.text_input("Zip/Post Code", "V0R 1B0", key="mar_zip")
        market_city = st.text_input("City", "Paramaribo", key="mar_city")

    st.subheader("Site Details")

    col1, col2 = st.columns(2)

    with col1:
        market_site_id = st.text_input("Site ID", "T2383823", key="mar_site_id")
        market_site_name = st.text_input("Site Name", "Retailer_A_South_Bank", key="mar_site_name")

    with col2:
        market_building_id = st.text_input("Building ID", "B38383", key="mar_building_id")
        market_building_name = st.text_input("Building Name", "Building_6", key="mar_building_name")

    st.subheader("Time Period")

    col1, col2 = st.columns(2)

    with col1:
        market_year = st.number_input("Year", 2021, key="mar_year")
        market_month = st.number_input("Month", 1, key="mar_month")

    st.subheader("Activity Data")

    commodities = ["Electricity", "Gas", "Other"]
    instrument_types = ["Bundled", "Unbundled"]
    tracking_systems = ["ERCOT", "M-RETS", "PJM-GATS"]

    col1, col2 = st.columns(2)

    with col1:
        commodity = st.selectbox("Commodity", commodities, key="commodity")
        energy_consumed = st.text_input("Energy Consumed (MWh)", "1000", key="energy_consumed")
        energy_supplier_residual_ef = st.text_input("Energy Supplier Residual EF", "na", key="energy_supplier_residual_ef")

    with col2:
        instrument_type_rec = st.selectbox("Instrument Type (REC)", instrument_types, key="instrument_type_rec")
        tracking_system_rec = st.selectbox("Tracking System (REC)", tracking_systems, key="tracking_system_rec")
        certificate_number_rec = st.text_input("Certificate Number (REC)", "1168", key="certificate_number_rec")

    st.subheader("REC Information")
    rec_col1, rec_col2 = st.columns(2)

    with rec_col1:
        supplier_name_rec = st.text_input("Supplier Name (REC)", "XXX", key="supplier_name_rec")
        energy_purchased_rec = st.text_input("Energy Purchased (MWh) (REC)", "20", key="energy_purchased_rec")
        emission_factor_rec = st.text_input("Emission Factor (REC)", "0.03", key="emission_factor_rec")
        source_rec = st.text_input("Source (REC)", "Solar", key="source_rec")
        expiry_date_rec = st.text_input("Expiry Date (REC)", "12-31-2020", key="expiry_date_rec")
    
    st.subheader("REDI Information")
    redi_col1, redi_col2 = st.columns(2)

    with redi_col1:
        supplier_name_redi = st.text_input("Supplier Name (REDI)", "Apex Clean Energy", key="supplier_name_redi")
        energy_purchased_redi = st.text_input("Energy Purchased (MWh) (REDI)", "10", key="energy_purchased_redi")
        emission_factor_redi = st.text_input("Emission Factor (REDI)", "na", key="emission_factor_redi")

    with redi_col2:
        source_redi = st.text_input("Source (REDI)", "Wind", key="source_redi")
        expiry_date_redi = st.text_input("Expiry Date (REDI)", "12-31-2020", key="expiry_date_redi")
        certificate_number_redi = st.text_input("Certificate Number (REDI)", "1078", key="certificate_number_redi")

    st.subheader("DEPC Information")
    depc_col1, depc_col2 = st.columns(2)

    with depc_col1: 
        supplier_name_depc = st.text_input("Supplier Name (DEPC)", "Invenergy", key="supplier_name_depc")
        energy_purchased_depc = st.text_input("Energy Purchased (MWh) (DEPC)", "10", key="energy_purchased_depc")
        supplied_emission_factor_depc = st.text_input("Supplied Emission Factor (DEPC)", "0.25", key="supplied_emission_factor_depc")

    with depc_col2:
        expiry_date_depc = st.text_input("Expiry Date (DEPC)", "12-31-2020", key="expiry_date_depc")
        certificate_number_depc = st.text_input("Certificate Number (DEPC)", "2089", key="certificate_number_depc")

# Submit button
    if st.button("Calculate market emission"):
       
        # Construct request payload
        market_request_payload = {
            "customID": {"id": market_customer_id},
            "onBehalfOfClient": {"companyId": market_company_id, "companyName": market_company_name},
            "organisation": {"departmentId": market_department_id, "departmentName": market_department_name},
            "requestType": market_request_type,
            "location": {"country": market_country, "stateProvince": market_state_province, "zipPostCode": market_zip_post_code, "city": market_city},
            "site": {"siteId": market_site_id, "siteName": market_site_name, "buildingId": market_building_id, "buildingName": market_building_name},
            "timePeriod": {"year": int(market_year), "month": int(market_month)},
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

        # st.subheader("Request Payload")
        # st.json(market_request_payload)

        try:
            market_response = requests.post(BACKEND_URL_MARKET, json=market_request_payload)
            market_response.raise_for_status()
            
            market_response_data = market_response.json()
            # st.subheader("API Response")
            # st.json(market_response_data)
            
            # Display as table if possible
            
            market_df_res = pd.json_normalize(market_response_data)
            st.subheader("Response as Table")
            st.dataframe(market_df_res)
           

        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with API: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

with tab6:
    st.header("Transport Emissions Calculator")
    
    # Form for customer information
    
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
        # st.subheader("Request Payload")
        # st.json(request_payload)
        
        try:
            # Send request to Flask backend
            response = requests.post(BACKEND_URL_TRANSPORT, json=request_payload)
            response.raise_for_status()
            
            # Display response
            # st.subheader("API Response")
            response_data = response.json()
            # st.json(response_data)
            
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

# frontend/app.py
import streamlit as st
import requests
import json
import pandas as pd

# Backend URL
BACKEND_URL = "http://127.0.0.1:5000/calculate-carbon"

def main():
    st.title("Carbon Footprint Calculator")

    # Input fields
    customer_id = st.text_input("Customer ID", "7263266537472000")
    company_id = st.text_input("Company ID", "6135759864070144")
    company_name = st.text_input("Company Name", "Larry Porter")
    department_id = st.text_input("Department ID", "1140899148988416")
    department_name = st.text_input("Department Name", "Christina McGuire")
    request_type = st.selectbox("Request Type", ["ACTUAL", "ESTIMATE"])
    country = st.text_input("Country", "Serbia")
    state_province = st.text_input("State/Province", "PE")
    zip_post_code = st.text_input("Zip/Post Code", "K9V 9P9")
    city = st.text_input("City", "Ocomuzez")
    site_id = st.text_input("Site ID", "6807305840492544")
    site_name = st.text_input("Site Name", "Allie Johnson")
    building_id = st.text_input("Building ID", "1033695748161536")
    building_name = st.text_input("Building Name", "Adelaide Robinson")
    year = st.number_input("Year", 2021)
    month = st.number_input("Month", 1)
    refrigerant_name = st.text_input("Refrigerant Name", "R-404A")
    refrigerant_inventory_beginning = st.text_input("Refrigerant Inventory Beginning", "10")
    refrigerant_inventory_end = st.text_input("Refrigerant Inventory End", "2")
    refrigerants_purchased_from_producers = st.text_input("Refrigerants Purchased From Producers", "6")
    refrigerants_provided_by_manufacturers = st.text_input("Refrigerants Provided By Manufacturers", "2")
    refrigerants_added_to_equipment = st.text_input("Refrigerants Added To Equipment", "3")
    refrigerant_returned_after_recycling = st.text_input("Refrigerant Returned After Recycling", "0")
    refrigerant_sales = st.text_input("Refrigerant Sales", "3")
    refrigerant_left_in_equipment = st.text_input("Refrigerant Left In Equipment", "4")
    refrigerant_returned_to_suppliers = st.text_input("Refrigerant Returned To Suppliers", "1")
    refrigerant_for_recycling = st.text_input("Refrigerant For Recycling", "0")
    refrigerant_for_destruction = st.text_input("Refrigerant For Destruction", "0")
    total_charge_new_equipment = st.text_input("Total Charge New Equipment", "0")
    total_charge_retrofitted = st.text_input("Total Charge Retrofitted", "0")
    original_charge_equipment = st.text_input("Original Charge Equipment", "0")
    total_charge_equipment_retro_away = st.text_input("Total Charge Equipment Retro Away", "0")
    unit_of_measurement = st.text_input("Unit Of Measurement", "kilogram")

    if st.button("Calculate Carbon Footprint"):
        request_payload = {
            "customID": {"id": customer_id},
            "onBehalfOfClient": {"companyId": company_id, "companyName": company_name},
            "organisation": {"departmentId": department_id, "departmentName": department_name},
            "requestType": request_type,
            "location": {"country": country, "stateProvince": state_province, "zipPostCode": zip_post_code, "city": city},
            "site": {"siteId": site_id, "siteName": site_name, "buildingId": building_id, "buildingName": building_name},
            "timePeriod": {"year": year, "month": month},
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

        response = requests.post(BACKEND_URL, json=request_payload)
        if response.status_code == 200:
            result = response.json()
            df_res = pd.json_normalize(result)
            st.write(df_res)
        else:
            st.error("Error in calculating carbon footprint")

if __name__ == '__main__':
    main()
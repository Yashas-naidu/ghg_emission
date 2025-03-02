# app.py (Flask Backend)
from flask import Flask, request, jsonify
import pandas as pd
import configparser
import requests
import json
import os

app = Flask(__name__)

# Load configuration
config = configparser.RawConfigParser()
config.read(['../../auth/secrets.ini','../../auth/config.ini'])

EI_API_KEY = config.get('EI', 'api.api_key')
EI_CLIENT_ID = config.get('EI', 'api.client_id')
EI_AUTH_ENPOINT = config.get('EI', 'api.auth_endpoint')
EI_BASE_URL = config.get('EI', 'api.base_url')

def get_bearer_token(token):
    headers = {
        'Content-Type': 'application/json',
        'cache-control': 'no-cache',
    }
    data = {"apiKey":token, "clientId":EI_CLIENT_ID}
    bearer_token_req = requests.post(EI_AUTH_ENPOINT, headers=headers, data=json.dumps(data))
    if bearer_token_req.status_code != 200:
        print("Error in getting Bearer token. Error code : ", bearer_token_req.status_code)
    return bearer_token_req.json()['access_token']

def Call_Carbon_API(CO2API, Co2Data, token):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer '+token,
        'Content-Type': 'application/json',
    }

    CO2response_req = requests.post(CO2API, headers=headers, data=json.dumps(Co2Data))
    if CO2response_req.status_code != 200:
        print("Problem! Error in generating response. Error code : ", CO2response_req.status_code)
    return CO2response_req.json()

@app.route('/carbon_api', methods=['POST'])
def carbon_api():
    try:
        # Get request payload from frontend
        request_payload = request.json
        
        # Get bearer token
        mybearer_token = get_bearer_token(EI_API_KEY)
        
        # Call Carbon API
        EI_API_ENDPOINT = f"{EI_BASE_URL}/v2/carbon/market"
        CO2Response = Call_Carbon_API(EI_API_ENDPOINT, request_payload, mybearer_token)
        
        return jsonify(CO2Response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
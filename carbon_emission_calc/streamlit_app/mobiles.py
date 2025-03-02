from flask import Flask, request, jsonify
import pandas as pd
import configparser
import requests
import json

app = Flask(__name__)

# Load configuration
def load_config():
    config = configparser.RawConfigParser()
    config.read(['../../auth/secrets.ini', '../../auth/config.ini'])
    
    return {
        'EI_API_KEY': config.get('EI', 'api.api_key'),
        'EI_CLIENT_ID': config.get('EI', 'api.client_id'),
        'EI_AUTH_ENPOINT': config.get('EI', 'api.auth_endpoint'),
        'EI_BASE_URL': config.get('EI', 'api.base_url')
    }

# Get bearer token
def get_bearer_token(token, client_id, auth_endpoint):
    headers = {
        'Content-Type': 'application/json',
        'cache-control': 'no-cache',
    }
    data = {"apiKey": token, "clientId": client_id}
    bearer_token_req = requests.post(auth_endpoint, headers=headers, data=json.dumps(data))
    
    if bearer_token_req.status_code != 200:
        raise Exception(f"Error in getting Bearer token. Error code: {bearer_token_req.status_code}")
    
    return bearer_token_req.json()['access_token']

# Call Carbon API
def call_carbon_api(co2_api, co2_data, token):
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    co2_response_req = requests.post(co2_api, headers=headers, data=json.dumps(co2_data))
    
    if co2_response_req.status_code != 200:
        raise Exception(f"Problem! Error in generating response. Error code: {co2_response_req.status_code}")
    
    return co2_response_req.json()

@app.route('/api/carbon/mobile', methods=['POST'])
def carbon_mobile():
    try:
        # Get request data
        request_data = request.json
        
        # Load configuration
        config_data = load_config()
        
        # Get bearer token
        bearer_token = get_bearer_token(
            config_data['EI_API_KEY'], 
            config_data['EI_CLIENT_ID'], 
            config_data['EI_AUTH_ENPOINT']
        )
        
        # Set API endpoint
        ei_api_endpoint = f"{config_data['EI_BASE_URL']}/v2/carbon/mobile"
        
        # Call Carbon API
        co2_response = call_carbon_api(ei_api_endpoint, request_data, bearer_token)
        
        return jsonify(co2_response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
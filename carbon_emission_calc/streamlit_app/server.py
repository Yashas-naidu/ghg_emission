from flask import Flask, request, jsonify
import pandas as pd
import configparser
import requests
import json

app = Flask(__name__)
config = configparser.RawConfigParser()
config.read(['../../auth/secrets.ini','../../auth/config.ini'])

EI_API_KEY = config.get('EI', 'api.api_key')
EI_CLIENT_ID = config.get('EI', 'api.client_id')
EI_AUTH_ENDPOINT = config.get('EI', 'api.auth_endpoint')
EI_BASE_URL = config.get('EI', 'api.base_url')


# Function to get Bearer Token
def get_bearer_token():
    headers = {'Content-Type': 'application/json'}
    data = {"apiKey": EI_API_KEY, "clientId": EI_CLIENT_ID}
    response = requests.post(EI_AUTH_ENDPOINT, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None


# Function to call IBM GHG API
def call_carbon_api(request_payload, token):
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    url = f"{EI_BASE_URL}/v2/carbon/location"
    response = requests.post(url, headers=headers, json=request_payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API call failed with status code {response.status_code}"}


@app.route('/calculate_emission', methods=['POST'])
def calculate_emission():
    data = request.json
    token = get_bearer_token()

    if not token:
        return jsonify({"error": "Failed to authenticate API"}), 401

    response = call_carbon_api(data, token)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

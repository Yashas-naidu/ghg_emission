# backend/app.py
from flask import Flask, request, jsonify
import configparser
import requests
import json

app = Flask(__name__)

# Load configuration
config = configparser.RawConfigParser()
config.read(['../../auth/secrets.ini', '../../auth/config.ini'])

EI_API_KEY = config.get('EI', 'api.api_key')
EI_CLIENT_ID = config.get('EI', 'api.client_id')
EI_AUTH_ENPOINT = config.get('EI', 'api.auth_endpoint')
EI_BASE_URL = config.get('EI', 'api.base_url')

def get_bearer_token(token):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {"apiKey": EI_API_KEY, "clientId": EI_CLIENT_ID}
    bearer_token_req = requests.post(EI_AUTH_ENPOINT, headers=headers, data=json.dumps(data))
    if bearer_token_req.status_code != 200:
        print("Error in getting Bearer token. Error code : ", bearer_token_req.status_code)
    return bearer_token_req.json()['access_token']

@app.route('/calculate-carbon', methods=['POST'])
def calculate_carbon():
    data = request.json
    mybearer_token = get_bearer_token(EI_API_KEY)
    EI_API_ENDPOINT = f"{EI_BASE_URL}/v2/carbon/fugitive"
    response = Call_Carbon_API(EI_API_ENDPOINT, data, mybearer_token)
    return jsonify(response)

def Call_Carbon_API(CO2API, Co2Data, token):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    CO2response_req = requests.post(CO2API, headers=headers, data=json.dumps(Co2Data))
    if CO2response_req.status_code != 200:
        print("Problem! Error in generating response. Error code : ", CO2response_req.status_code)
    return CO2response_req.json()

if __name__ == '__main__':
    app.run(debug=True)
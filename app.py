import os
import io
import json
import requests
import base64
from flask import Flask, request, render_template, redirect, url_for, send_file

project_root = os.path.dirname(os.path.realpath('__file__'))
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder= 'templates')
context_set = ""

@app.route('/')
def hello_world():
    return render_template('index.html')

appId = "03220c91-5fd8-4431-b644-21f3782aa1c5"
appKey = "76939d91-4de1-4794-9e13-04429a5dcc3a"

# Define the API endpoint you want to access
api_endpoint_lse = "https://api.genability.com/rest/public/lses"
api_endpoint_tariff = "https://api.genability.com/rest/public/tariffs/512"
api_endpoint_default = "https://api.genability.com/rest/public/tariffs/81587/history"

# Format the Basic Authentication header as specified
auth_string = f"{appId}:{appKey}"
base64_auth_string = base64.b64encode(auth_string.encode()).decode()
headers = {'Authorization': f'Basic {base64_auth_string}'}

@app.route('/api_response', methods=['GET', 'POST'])
def api_response():
    service = request.form.get("service")

    # Format the Basic Authentication header as specified
    auth_string = f"{appId}:{appKey}"
    base64_auth_string = base64.b64encode(auth_string.encode()).decode()
    headers = {'Authorization': f'Basic {base64_auth_string}'}

    if service == 'Load Serving Entity':
        response = requests.get(api_endpoint_lse, headers=headers)
        response_data = response.json()
        return render_template('response_lse.html', response=response_data)
    elif service == 'Tariff':
        response = requests.get(api_endpoint_tariff, headers=headers)
        response_data = response.json()
        return render_template('response_tariff.html', response=response_data)
    else:
        response = requests.get(api_endpoint_default, headers=headers)
        response_data = response.json()
        return render_template('response_default.html', response=response_data)


if __name__ == '__main__':
    app.run(debug=True)
    


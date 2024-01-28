from flask import Flask, render_template, request, jsonify, make_response, url_for
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import warnings
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/potential')
def potential():
    return render_template('potential.html')

@app.route('/current')
def current():
    return render_template('current.html')

@app.route('/potential', methods=['POST'])
def process_button():
    # Call your Python function here
    result = your_python_function()
    
    # You can do something with the result, e.g., pass it to the template
    return render_template('potential.html', result=result)

def your_python_function():
    url = "https://app.scrapeak.com/v1/scrapers/zillow/listing"

    querystring = {
        "api_key": "a83eaaf4-9c4f-40bc-8160-6eb101a6c58d",
        "url":"https://www.zillow.com/ann-arbor-mi/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A42.389183%2C%22south%22%3A42.183445%2C%22east%22%3A-83.605304%2C%22west%22%3A-83.954037%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A8097%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
    }

    listing_response = requests.request("GET", url, params=querystring)
    print(listing_response.json()["data"])
    return listing_response.json()["data"]

@app.route('/api/store_data', methods=['POST'])
def store_data():
    data = request.json
    # Process and store data in the database (you can use SQLAlchemy or any other preferred database library)
    # Example: data_processing_function(data)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
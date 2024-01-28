from flask import Flask, render_template, request, jsonify, make_response, url_for
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import warnings
import json
import statistics

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



@app.route('/handle_form_submission', methods=['POST'])
def handle_form_submission():
    # Get the selected answer from the form data
    answer_value = request.form.get('resign')

    # Perform any necessary server-side processing

    # Redirect based on the answer
    if answer_value == 'YES':
        f = open('output.json')
        # returns JSON object as
        # a dictionary
        data = json.load(f)


        prices = [item["unformattedPrice"] for item in data["cat1"]["searchResults"]["listResults"]]
        print(prices)
        # Calculate the mean
    if answer_value == 'YES':
        mean_price = sum(prices) / len(prices)
        return render_template('statistics.html', result = mean_price)  # Redirect to the "statistics" route
    elif answer_value in ['NO', 'UNDECIDED']:
        return render_template('main.html')  # Redirect to the "main" route

def fetch_json():
    url = "https://app.scrapeak.com/v1/scrapers/zillow/listing"

    querystring = {
        "api_key": "a83eaaf4-9c4f-40bc-8160-6eb101a6c58d",
        "url":"https://www.zillow.com/ann-arbor-mi/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A42.389183%2C%22south%22%3A42.183445%2C%22east%22%3A-83.605304%2C%22west%22%3A-83.954037%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A8097%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
    }

    listing_response = requests.request("GET", url, params=querystring)
    print(listing_response.json()["data"])

    return listing_response.json()["data"]


if __name__ == '__main__':
    app.run(debug=True)
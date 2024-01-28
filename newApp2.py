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

@app.route('/potential/getdata')
def process_button():
    # Call your Python function here
    result = fetch_json()

    listings = []
    print(len(result["cat1"]["searchResults"]["mapResults"]))
    for data in result["cat1"]["searchResults"]["mapResults"]:
        if(data["statusType"] == "FOR_RENT"):
            currList = [data["address"], data["price"]]
            if "beds" in data:
                currList.append(data["beds"])
            else:
                currList.append(data["minBeds"])
            if "baths" in data:
                currList.append(data["baths"])
            else:
                currList.append(data["minBaths"])
            if "area" in data:
                currList.append(data["area"])
            else:
                currList.append(data["minArea"])
            listings.append(currList)

    # You can do something with the result, e.g., pass it to the template
    return listings

@app.route('/form_submission', methods=['POST'])
def form_submission():
    # Get the selected answer from the form data
    answer_value = request.form.get('resign')

    # Perform any necessary server-side processing
    form_data_dict = request.form.to_dict()
    # Redirect based on the answer
    form_data_dict = {key: value for key, value in list(form_data_dict.items())[:-1]}

    # Convert the form data to JSON
    print(form_data_dict)

    # Save the JSON data to a file
    
    
    if answer_value == 'YES':
        f = open('output.json')
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        prices = [item["unformattedPrice"] for item in data["cat1"]["searchResults"]["listResults"]]
        # Calculate the mean
        mean_price = sum(prices) / len(prices)
        
        my_values = [mean_price, list(form_data_dict.values())[-1]]
        return render_template('statistics.html', my_values = my_values)  # Redirect to the "statistics" route
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

import pandas as pd
import numpy as np
import plotly.express as px
import requests
import warnings

def get_listings(api_key, listing_url):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/listing"

    querystring = {
        "api_key": api_key,
        "url":listing_url
    }

    return requests.request("GET", url, params=querystring)




api_key = "a83eaaf4-9c4f-40bc-8160-6eb101a6c58d"

listing_url = "https://www.zillow.com/ann-arbor-mi/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A42.389183%2C%22south%22%3A42.183445%2C%22east%22%3A-83.605304%2C%22west%22%3A-83.954037%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A8097%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"

# get listings
listing_response = get_listings(api_key, listing_url)

listing_response.json().keys()

if not listing_response.json()["is_success"]:
    print("Error Scraping")

num_of_properties = listing_response.json()["data"]["categoryTotals"]["cat1"]["totalResultCount"]
print("Count of properties:", num_of_properties)

df_listings = pd.json_normalize(listing_response.json()["data"]["cat1"]["searchResults"]["mapResults"])
print("Number of rows:", len(df_listings))
print("Number of columns:", len(df_listings.columns))
print(df_listings)
print(listing_response.json()["data"])

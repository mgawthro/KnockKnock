# Python program to read
# json file
import json
import statistics
# Opening JSON file
f = open('output.json')
# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
prices = [item["unformattedPrice"] for item in data["cat1"]["searchResults"]["listResults"]]
print(prices)
# Calculate the mean
mean_price = sum(prices) / len(prices)
# if(data["statusType"] == "FOR_RENT"):
#     print(data["address"])
#     print(data["price"])
#     print(data["beds"])
#     print(data["baths"])
#     print(data["area"])
print(statistics.median(prices))
print(mean_price)
# Closing file
f.close()
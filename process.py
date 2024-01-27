# Python program to read
# json file
import json
# Opening JSON file
f = open('example.json')
# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
if(data["statusType"] == "FOR_RENT"):
    print(data["address"])
    print(data["price"])
    print(data["beds"])
    print(data["baths"])
    print(data["area"])

print(data["availabilityDate"])
# Closing file
f.close()
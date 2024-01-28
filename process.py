from dataclasses import dataclass
import json


def sendJson():
    f = open('output.json')
    datum = json.load(f)
    listings = []
    print(len(datum["cat1"]["searchResults"]["mapResults"]))
    for data in datum["cat1"]["searchResults"]["mapResults"]:
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
            print(listings[-1])
    # Closing file
    f.close()

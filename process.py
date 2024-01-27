from dataclasses import dataclass

@dataclass
class Listing:
    address: str
    price: float = None
    beds: float = None
    bath: float = None
    area: float = None

def sendJson():
    # Python program to read
    # json file
    import json
    # Opening JSON file
    f = open('output.json')
    # returns JSON object as
    # a dictionary
    datum = json.load(f)
    # Iterating through the json
    listings = []
    print(len(datum["cat1"]["searchResults"]["mapResults"]))
    for data in datum["cat1"]["searchResults"]["mapResults"]:
        if(data["statusType"] == "FOR_RENT"):
            listings.append(Listing(address = data["address"], price = data["price"]))
            if "beds" in data:
                listings[-1].beds = data["beds"]
            else:
                listings[-1].beds  = data["minBeds"]
            if "baths" in data:
                listings[-1].bath = data["baths"]
            else:
                listings[-1].bath = data["minBaths"]
            if "area" in data:
                listings[-1].area = data["area"]
            else:
                listings[-1].area = data["minArea"]
            print(listings[-1])
    # Closing file
    f.close()

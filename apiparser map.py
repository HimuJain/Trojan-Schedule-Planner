import requests
import json
from dotenv import load_dotenv
import os
import re

load_dotenv()

MAP_API_KEY = os.getenv("NODE_MAP_API_KEY")

url = "https://api.concept3d.com/categories/53722?map=1928&children&key=0001085cc708b9cef47080f064612ca5"
response = (requests.get(url)).json()
# print(response.status_code) 
print(len(response["children"]["locations"]))
for location in response["children"]["locations"]:
    clean = re.sub(r"\s*\([^()]*\)$", "", location["name"])
    print(clean)
    if location.get("reference"):
        print("\t", location["reference"][0])
        print("\t", location["lng"], location["lat"])
        # url = f"https://geocode.maps.co/reverse?lat={location['lat']}&lon={location['lng']}&api_key={MAP_API_KEY}"
        # address = (requests.get(url))
        # if address.status_code == 200:
        #     address = address.json()
        # else:
        #     print("error")
        #     address = {}
        # print(address.get("display_name"))
    

    # print(location.keys())

# print(response["children"]["locations"][0])
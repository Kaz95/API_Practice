# Prints Equipment name
# Use pprint module if you ever need to check what data is stored in response.text
import json  # JSON module handles API language translation
import requests  # requests module handles fetching urls

url = "http://www.dnd5eapi.co/api/equipment/1"  # Storing API url as var
response = requests.get(url)    # stores response from .get ping as response
response.raise_for_status()     # Checks response for errors
equipment = json.loads(response.text)   # json.load turns json data to a python dictionary
print(equipment['name'])    # Accessing that dictionary via key

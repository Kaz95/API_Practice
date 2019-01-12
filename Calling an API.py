# Prints Equipment name
# Use pprint module if you ever need to check what data is stored in response.text
import json  # JSON module handles API language translation
import requests  # requests module handles fetching urls
import pprint
# url = "http://www.dnd5eapi.co/api/equipment/1"  # Storing API url as var
# response = requests.get(url)    # stores response from .get ping as response
# response.raise_for_status()     # Checks response for errors
# equipment = json.loads(response.text)   # json.load turns json data to a python dictionary
# print(equipment['name'])    # Accessing that dictionary via key

# Search for equipment and return item info.

url = "http://www.dnd5eapi.co/api/equipment/"  # Storing API url as var
response = requests.get(url)    # stores response from .get ping as response
response.raise_for_status()     # Checks response for errors
equipment = json.loads(response.text)   # json.load turns json data to a python dictionary
list_of_dic = equipment['results']  # Dictionary containing Name/url: Values
print('What are you looking for?')
item = input()  # Asks for item to search for
for i in list_of_dic:   # For dic in list of dics
    if i['name'] == item:   # If dic[name] == item searched for
        url = i['url']  # Change API from general category to item specific url

response = requests.get(url)    # stores response from .get ping as response
response.raise_for_status()     # Checks response for errors
item_info = json.loads(response.text)
pprint.pprint(item_info)

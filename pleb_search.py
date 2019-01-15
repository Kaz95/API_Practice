# !/usr/bin/python
import json  # JSON module handles API language translation
import requests  # requests module handles fetching urls

# Core functionality of search
# def search_equipment():
#     url = "http://www.dnd5eapi.co/api/equipment/"  # Storing API url as var
#     response = requests.get(url)    # stores response from .get ping as response
#     response.raise_for_status()     # Checks response for errors
#     equipment = json.loads(response.text)   # json.load turns json data to a python dictionary
#     list_of_dic = equipment['results']  # Dictionary containing Name/url: Values
#     print('What are you looking for?')
#     item = input()  # Asks for item to search for
#     for i in list_of_dic:   # For dic in list of dics
#         if i['name'] == item:   # If dic[name] == item searched for


def pleb_search():
    url = "http://www.dnd5eapi.co/api/equipment/"  # Storing API url as var
    response = requests.get(url)    # stores response from .get ping as response
    response.raise_for_status()     # Checks response for errors
    equipment = json.loads(response.text)   # json.load turns json data to a python dictionary
    list_of_dic = equipment['results']  # Dictionary containing Name/url: Values
    print('What are you looking for?')
    item = input()  # Asks for item to search for
    for i in list_of_dic:   # For dic in list of dics
        if i['name'] == item:   # If dic[name] == item searched for
            api_info = list([i['name']] + [i['url']])  # Double bracket to make sure string isn't slice by character.
            print(api_info)
            return api_info


if __name__ == '__main__':
    pleb_search()

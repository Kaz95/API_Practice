def get_dic():
    info = {
                "count": 256,
                "results": [
                    {
                        "name": "Club",
                        "url": "http://www.dnd5eapi.co/api/equipment/1"
                    },
                    {
                        "name": "Dagger",
                        "url": "http://www.dnd5eapi.co/api/equipment/2"
                    },
                    {
                        "name": "Greatclub",
                        "url": "http://www.dnd5eapi.co/api/equipment/3"
                    },
                ]
            }
    return info


def get_item_api_info():
        api = get_dic()['results']
        list_of_dic = api  # Dictionary containing Name/url: Values
        print('What are you looking for?')
        item = 'Club'  # Asks for item to search for
        for i in list_of_dic:  # For dic in list of dics
            if i['name'] == item:  # If dic[name] == item searched for
                api_info = list(
                    [i['name']] + [i['url']])  # Double bracket to make sure string isn't slice by character.
                print(api_info)
                return api_info



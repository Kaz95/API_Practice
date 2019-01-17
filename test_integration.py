import unittest
from test_setup import get_item_api_info
# class TestBasic(unittest.TestCase):
#     API = {
# 	"count": 256,
# 	"results": [
# 		{
# 			"name": "Club",
# 			"url": "http://www.dnd5eapi.co/api/equipment/1"
# 		},
# 		{
# 			"name": "Dagger",
# 			"url": "http://www.dnd5eapi.co/api/equipment/2"
# 		},
# 		{
# 			"name": "Greatclub",
# 			"url": "http://www.dnd5eapi.co/api/equipment/3"
# 		},
# 	]
# }
#
#     def test_item_api_info(self):
#         url = TestBasic.API
#         list_of_dic = url  # Dictionary containing Name/url: Values
#         print('What are you looking for?')
#         item = 'Club'  # Asks for item to search for
#         for i in list_of_dic:  # For dic in list of dics
#             if i['name'] == item:  # If dic[name] == item searched for
#                 api_info = list(
#                     [i['name']] + [i['url']])  # Double bracket to make sure string isn't slice by character.
#                 print(api_info)
#                 self.assertEqual(api_info, ['Club', 'http://www.dnd5eapi.co/api/equipment/1'])


class TestApiInfo(unittest.TestCase):
    def test_item_api_info(self):
        self.assertEqual(get_item_api_info(), ['Club', 'http://www.dnd5eapi.co/api/equipment/1'])


if __name__ == '__main__':
    unittest.main()

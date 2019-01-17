# !/usr/bin/python
from psycopg2 import sql
import psycopg2
from config import config
import json  # JSON module handles API language translation
import requests  # requests module handles fetching urls
from quantity import plus
from quantity import minus
from quantity import check_quantity
from quantity import delete_zero
from quantity import delete


class Item:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        self.quantity = 1

    # Working model for item rows
    def add_item(self, table_name):
        # Add a new item
        k = sql.SQL("""INSERT INTO {}(name, api, quantity)
                 VALUES
                 (%s, %s, 1);""").format(sql.Identifier(table_name))
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.name, self.api,))  # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    # Search for equipment and return item info.
    def get_info(self):
        url = "http://www.dnd5eapi.co/api/equipment/"  # Storing API url as var
        response = requests.get(url)  # stores response from .get ping as response
        response.raise_for_status()  # Checks response for errors
        equipment = json.loads(response.text)  # json.load turns json data to a python dictionary
        list_of_dic = equipment['results']  # Dictionary containing Name/url: Values
        for i in list_of_dic:  # For dictionary in list of dictionaries
            if i['name'] == self.name:  # If dic[name] == item searched for
                url = i['url']  # Change API from general category to item specific url

        response = requests.get(url)  # stores response from .get ping as response
        response.raise_for_status()  # Checks response for errors
        item_info = json.loads(response.text)  # Assigns detailed item info to a var in form of nested dictionary.
        return item_info

    # the following methods handle quantity. Including the deletion of 0 quantity items. Will be reworked to its own mod
    def plus(self, table_name):
        plus(self.name, table_name)

    def check_quantity(self, some_table):
        check_quantity(self.name, some_table)

    def delete_zero(self, some_table):
        delete_zero(self.name, some_table)

    def minus(self, some_table):
        minus(self.name, some_table)

    def delete(self, some_table):
        delete(self.name, some_table)




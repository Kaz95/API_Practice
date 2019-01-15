# !/usr/bin/python
from psycopg2 import sql
import psycopg2
from config import config
import json  # JSON module handles API language translation
import requests  # requests module handles fetching urls
from pleb_delete import delete


class Item:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        self.quantity = 1

    # Working model for inserting rows
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

    def delete(self, some_table):
        k = sql.SQL("""DELETE FROM {}
                       WHERE name = %s;""").format(sql.Identifier(some_table))
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.name,))  # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def get_info(self):
        # Search for equipment and return item info.

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

    def add_one(self, some_table):
        k = sql.SQL("""UPDATE {}
                SET quantity = quantity + 1
                WHERE name = %s;""").format(sql.Identifier(some_table))
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.name,))  # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def check_quantity(self, some_table):
        k = sql.SQL("""SELECT name, quantity
                       FROM {}
                       WHERE name=%s;""").format(sql.Identifier(some_table))
        conn = None
        quantity = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.name,))  # The second set of () and , are completely necessary.
            quantity = cur.fetchone()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return quantity[1]

    def delete_zero(self, some_table):
        quantity = self.check_quantity(some_table)
        if quantity == 0:
            delete(some_table, self.name)

    def minus_one(self, some_table):
        k = sql.SQL("""UPDATE {}
                SET quantity = quantity - 1
                WHERE name = %s;""").format(sql.Identifier(some_table))
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.name,))  # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        self.delete_zero(some_table)




class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self, other):
        print('Hello ' + other + ', my name is', self.name)


p = Person('Swaroop')
p.say_hi('Bob')

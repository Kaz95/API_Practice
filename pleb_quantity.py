# !/usr/bin/python
from psycopg2 import sql
import psycopg2
from config import config
from pleb_delete import delete


class Item:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        self.quantity = 1

    def add(self, some_table):
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
            cur.execute(k, (self.name,))    # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def minus(self, some_table):
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
            cur.execute(k, (self.name,))    # The second set of () and , are completely necessary.
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




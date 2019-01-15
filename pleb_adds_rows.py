#!/usr/bin/python
from psycopg2 import sql
import psycopg2
from config import config


# Working model for inserting rows
def pleb_adds_rows(table_name, some_name, some_api):
    """ insert a new vendor into the vendors table """
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
        cur.execute(k, (some_name, some_api,))  # The second set of () and , are completely necessary.
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



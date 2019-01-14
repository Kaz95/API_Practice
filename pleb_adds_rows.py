#!/usr/bin/python

import psycopg2
from config import config


# Working model for inserting rows
def pleb_adds_rows(some, shits):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO store(name, api)
             VALUES
             (%s, %s);"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (some, shits,))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




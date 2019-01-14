# !/usr/bin/python
import psycopg2
from psycopg2 import sql    # Normal import psycopg2 didn't import sql for some reason.
from config import config


def create_tables(some_shit):
    # create tables in the PostgreSQL database with pass value as name.
    k = sql.SQL("""CREATE TABLE {} (
          name VARCHAR,
          api VARCHAR);""").format(sql.Identifier(some_shit))

    conn = None  # Sets a connection var which is currently None(Disconnected)
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)  # Variable holding connection parameters. Pulled from database.ini via config
        cur = conn.cursor()  # Creates a cursor object. Used to execute commands. This is the actual connection.
        # create table with var passed
        cur.execute(k)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:    # Note the 'not'. So if connection was open; close connection.
            conn.close()


print('Type some shit')
shit = input()

if __name__ == '__main__':
    create_tables(shit)

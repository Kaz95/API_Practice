# !/usr/bin/python
import psycopg2
from psycopg2 import sql    # Normal import psycopg2 didn't import sql for some reason.
from config import config


def create_inventory(table_name):
    # create tables in the PostgreSQL database with pass value as name.
    k = sql.SQL("""CREATE TABLE {} (
          name VARCHAR,
          api VARCHAR,
          quantity INTEGER);""").format(sql.Identifier(table_name))

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


def create_bank():
    # create tables in the PostgreSQL database with pass value as name.
    k = sql.SQL("""CREATE TABLE currency (
          name VARCHAR,
          gp INTEGER,
          sp INTEGER,
          cp INTEGER);""")

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


def create_account_archive():
    # create tables in the PostgreSQL database with pass value as name.
    k = sql.SQL("""CREATE TABLE account (
              name VARCHAR,
              password VARCHAR,
              role VARCHAR);""")

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
        if conn is not None:  # Note the 'not'. So if connection was open; close connection.
            conn.close()


if __name__ == '__main__':
    create_account_archive()

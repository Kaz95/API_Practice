#!/usr/bin/python
from psycopg2 import sql
import psycopg2
from config import config


# # Working model for item rows. Handled by item method at the moment.
# def item_row(table_name, some_name, some_api):
#     # Defaults quantity value to 1
#     k = sql.SQL("""INSERT INTO {}(name, api, quantity)
#              VALUES
#              (%s, %s, 1);""").format(sql.Identifier(table_name))
#     conn = None
#
#     try:
#         # read database
#         params = config()
#         # connect to the PostgreSQL database
#         conn = psycopg2.connect(**params)
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.execute(k, (some_name, some_api,))  # The second set of () and , are completely necessary.
#         # commit the changes to the database
#         conn.commit()
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()


# Working model for bank rows
def bank_row(name):
    # sets all units of currency to 0 value.
    k = sql.SQL("""INSERT INTO currency(name, gp, sp, cp) 
             VALUES
             (%s, 0, 0, 0);""")
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(k, (name,))  # The second set of () and , are completely necessary.
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Working model for account rows
def account_row(name, password, role):

    k = sql.SQL("""INSERT INTO account(name, password, role) 
                 VALUES
                 (%s, %s, %s);""")
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(k, (name, password, role,))  # The second set of () and , are completely necessary.
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    bank_row('bob')
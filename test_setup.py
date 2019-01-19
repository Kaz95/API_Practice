import psycopg2
from psycopg2 import sql
from config import config
from table import create_account_archive
from table import create_bank
from table import create_inventory
from row import account_row
from row import bank_row
from account import get_password
from currency import GP
from currency import SP
from currency import CP


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


def test_get_item_api_info():
        api = get_dic()['results']
        list_of_dic = api  # Dictionary containing Name/url: Values
        test_item = 'Club'  # Asks for item to search for
        for i in list_of_dic:  # For dic in list of dics
            if i['name'] == test_item:  # If dic[name] == item searched for
                api_info = list(
                    [i['name']] + [i['url']])  # Double bracket to make sure string isn't slice by character.
                print(api_info)
                return api_info


# Working model for checking if table exists. Should return True if exists.
def check_table_exists(name):
    conn = None
    k = ("""SELECT EXISTS (
         SELECT 1
         FROM   information_schema.tables
         WHERE  table_schema = 'public'
         AND    table_name = %s );""")
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(k, (name,))
        row = cur.fetchone()
        row = row[0]
        cur.close()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def query_row(table, name):
    conn = None
    k = sql.SQL("""SELECT * FROM {} WHERE name = %s;""").format(sql.Identifier(table))
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(k, (name,))
        row = cur.fetchone()
        cur.close()
        info = []
        for i in row:
            info.append(i)
        return info
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Returns pass word of given name from DB
def test_get_password():
    conn = None
    k = """SELECT password
               FROM account
               WHERE name = 'bob';"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(k)
        role_tup = cur.fetchone()
        password = role_tup[0]
        cur.close()
        return password
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Authenticates given password based on DB info tied to given name.
def test_authenticate():
    if get_password('bob') == 'tree53':
        return True
    else:
        return False


def sample_bank_rows():
    # sets all units of currency to 0 value.
    k = sql.SQL("""INSERT INTO currency(name, gp, sp, cp) 
             VALUES
             ('bob', 0, 0, 0),
             ('currency test', 0, 0, 0);""")
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(k)  # The second set of () and , are completely necessary.
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def drop_tables(table_name):
    k = sql.SQL("""DROP TABLE {}""").format(sql.Identifier(table_name))

    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(k)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def test_currency():
    GP(5, None).add('currency test')
    SP(99, None).add('currency test')
    CP(99, None).add('currency test')


def add_test_item(table_name):
    sample_item = test_get_item_api_info()
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
        cur.execute(k, (sample_item[0], sample_item[1],))  # The second set of () and , are completely necessary.
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
    # drop_tables('account')
    # drop_tables('currency')
    # drop_tables('bob')
    # create_bank()
    # create_inventory('bob')
    # create_account_archive()
    # account_row('bob', 'tree53', 'DM')
    # sample_bank_rows()
    # test_currency()
    # add_test_item('bob')
    print(query_row('bob', 'Club'))
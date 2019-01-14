from psycopg2 import sql
import psycopg2
from config import config


def add_one(some_table, some_name):
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
        cur.execute(k, (some_name,))    # The second set of () and , are completely necessary.
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

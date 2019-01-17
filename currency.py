# !/usr/bin/python
from psycopg2 import sql
import psycopg2
from config import config


# Superclass
class Currency:
    def __init__(self, quantity):
        self.quantity = quantity


# Subclasses for specific units of currency
# TODO Unit field currently unused. Hoping to use to cut back on redundant code.
class GP(Currency):
    def __init__(self, quantity, unit):
        Currency.__init__(self, quantity)
        self.unit = unit

    def add(self, name):
        k = sql.SQL("""UPDATE currency
                SET gp = gp + %s
                WHERE name = %s;""")
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.quantity, name,))    # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


class SP(Currency):
    def __init__(self, quantity, unit):
        Currency.__init__(self, quantity)
        self.unit = unit

    def add(self, name):
        k = sql.SQL("""UPDATE {}
                SET sp = sp + %s
                WHERE name = %s;""")
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.quantity, name,))    # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


class CP(Currency):
    def __init__(self, quantity, unit):
        Currency.__init__(self, quantity)
        self.unit = unit

    def add(self, name):
        k = sql.SQL("""UPDATE {}
                SET cp = cp + %s
                WHERE name = %s;""")
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(k, (self.quantity, name,))    # The second set of () and , are completely necessary.
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()




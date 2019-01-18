#! /usr/bin/python
import psycopg2
from config import config
# TODO Error handling on inputs where applicable.


# Creates new account.
def get_info():
    print('create name')
    name = input()
    print('create password')
    password = input()
    print('DM or player?')
    role = input()
    info = list([name] + [password] + [role])
    return info


# Asks for log-in information.
def log_in():
    print('type name')
    name = input()
    print('type password')
    password = input()
    info = list([name] + [password])
    return info


# Returns role of given name from DB
def get_role(name):
    conn = None
    k = """SELECT role
           FROM account
           WHERE name = %s"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(k, (name,))
        role_tup = cur.fetchone()
        role = role_tup[0]
        cur.close()
        return role
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Returns pass word of given name from DB
def get_password(name):
    conn = None
    k = """SELECT password
               FROM account
               WHERE name = %s"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(k, (name,))
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
def authenticate(name, password):
    if get_password(name) == password:
        return True
    else:
        return False


# Creates user account object
class Account:
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def authenticate(self):
        if get_password(self.name) != self.password:
            return 'Invalid password'
        else:
            return 'Welcome ' + self.name + ' !'

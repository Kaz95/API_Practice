import unittest
from test_setup import get_item_api_info
from test_setup import check_table_exists
from test_setup import query_row
from test_setup import test_get_password
from test_setup import test_authenticate
import psycopg2
from psycopg2 import sql
from config import config
# TODO Make get_vendors into a reusable test class for checking if tables exist.


# # Working model for checking if table exists. Should return True if exists.
# def get_vendors():
#     conn = None
#     k = sql.SQL("""SELECT EXISTS (
#          SELECT 1
#          FROM   information_schema.tables
#          WHERE  table_schema = 'public'
#          AND    table_name = 'bob');""")
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(k)
#         row = cur.fetchone()
#         row = row[0]
#         cur.close()
#         return row
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()


class TestApiInfo(unittest.TestCase):
    def test_tables_exist(self):
        self.assertTrue(check_table_exists('bob'))
        self.assertTrue(check_table_exists('currency'))
        self.assertTrue(check_table_exists('account'))

    def test_rows_exist(self):
        self.assertEqual(query_row('account'), ['bob', 'tree53', 'DM'])
        self.assertTrue(test_get_password())
        self.assertTrue(test_authenticate)
        self.assertEqual(query_row('currency'), ['bob', 0, 0, 0])

    def test_item_api_info(self):
        self.assertEqual(get_item_api_info(), ['Club', 'http://www.dnd5eapi.co/api/equipment/1'])


if __name__ == '__main__':
    unittest.main()

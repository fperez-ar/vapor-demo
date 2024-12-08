from sqlite3 import connect
from os import getenv

def executemany(query: str, args: list):
    db_name: str = getenv('DB_NAME')
    with connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.executemany(query, args)

def execute(query: str, *args: list):
    db_name: str = getenv('DB_NAME')
    with connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)

def fetchall(query: str, *args: list):
    db_name: str = getenv('DB_NAME')
    result: str = ''
    with connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        result = cursor.fetchall()
    return result
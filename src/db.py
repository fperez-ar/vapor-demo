#!/usr/bin/env python
from sqlite3 import connect
from os import getenv

def executemany(exec_sentence: str, args: list):
    db_name: str = getenv('DB_NAME')
    with connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.executemany(exec_sentence, args)

def execute(exec_sentence: str, *args: list):
    db_name: str = getenv('DB_NAME')
    with connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(exec_sentence, args)

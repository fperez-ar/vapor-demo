#!/usr/bin/env python
import os
import sqlite3
from get_apps import get_apps
from dotenv import load_dotenv

# load all env vars
load_dotenv()
# create db if it doesnt exist
connection = sqlite3.connect(os.getenv('DB_NAME'))
cursor = connection.cursor() 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS apps (
        appid INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')
connection.close()
get_apps()

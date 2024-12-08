#!/usr/bin/env python
from utils.db_utils import executemany, execute
from dotenv import load_dotenv
from os import getenv
from requests import get
from utils.request_utils import status_validation, path_validation
load_dotenv()

"""
    populates the db (lazily by default) with all the records 
    from getapplist json
"""
def _insert_into_db(apps: list):
    # only apps where name is not empty
    apps = [item for item in apps if item['name']]
    # prepare tuple for insertion into db
    many = [(item['appid'], item['name']) for item in apps]
    # default behaviour will ignore existing appids
    exec_sentence: str = 'INSERT OR IGNORE INTO apps (appid, name) VALUES(?, ?);'
    if getenv('DB_FORCE_REPLACE', False):
        exec_sentence = 'INSERT OR REPLACE INTO apps (appid, name) VALUES(?, ?);'
    executemany(exec_sentence, many)

def populate_db():
    base_url: str = getenv('BASE_URL')
    endpoint: str = 'ISteamApps/GetAppList/v2/'
    response = get(f'{base_url}/{endpoint}')
    status_validation(response)
    json = response.json()
    path_validation(json, ['applist','apps'])
    apps = response.json()['applist']['apps']
    _insert_into_db(apps)

"""
    run as a cron job to populate db 
    suggested frequency: once a day
"""
execute('''CREATE TABLE IF NOT EXISTS apps (
        appid INTEGER PRIMARY KEY,
        name TEXT NOT NULL
)''')
populate_db()

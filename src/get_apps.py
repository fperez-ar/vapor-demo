#!/usr/bin/env python
from db import executemany
from dotenv import load_dotenv
import requests, json, os

def populate_db(apps: list):
    # only apps where name is not empty
    apps = [item for item in apps if item['name']]
    # prepare tuple for insertion into db
    many = [(item['appid'], item['name']) for item in apps]
    executemany('INSERT OR REPLACE INTO apps (appid, name) VALUES(?, ?)', many)

def get_apps():
    base_url: str = os.getenv('BASE_URL')
    endpoint: str = 'ISteamApps/GetAppList/v2/'
    response = requests.get(f'{base_url}/{endpoint}')

    if response.status_code == 200:
        json = response.json()
        if not 'applist' in json:
            raise Exception('Malformed json response, did not include key:\'applist\'!')
        if not 'apps' in json['applist']:
            raise Exception('Malformed json[\'applist\'] response, did not include key:\'apps\'!')
        apps = response.json()['applist']['apps']
        populate_db(apps)
        
    else:
        print('Request failed with status code:', response.text)
        print('Request failed with status code:', response.status_code)

#!/usr/bin/env python
from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv
load_dotenv()

app = Flask(__name__)
@app.route('/web/search', methods=['GET'])
def search():
    user_name = getenv('USER', 'user')
    _url = getenv('FETCH_API_URL')
    _port = getenv('FETCH_API_PORT')
    _endp = getenv('FETCH_API_ENDPOINT')
    steam_base_url = getenv('STORE_URL')
    api_url = f'{_url}:{_port}{_endp}';
    kwargs = {
        'user': user_name,
        'api_url': api_url,
        'steam_base_url': steam_base_url
    }
    return render_template('example.html', **kwargs)

if __name__ == '__main__':
    app.run(debug=getenv('WEB_DEBUG', False))
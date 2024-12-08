#!/usr/bin/env python
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from ..utils.db_utils import fetchall
from os import getenv

load_dotenv()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# need params page, pagesize for limit, offset
@app.route('/api/query', methods=['GET']) 
def query():
    name: str = request.args.get('name', '')
    limit: int = request.args.get('size', 100)
    offset: int = request.args.get('page', 0)

    q: str = 'SELECT appid, name FROM apps WHERE name LIKE ? LIMIT ? OFFSET ?'
    result = fetchall(q, f'%{name}%', limit, offset)
    # transform tuples into easily digestible dicts
    result = [{'appid':item[0], 'name':item[1]} for item in result]
    return result

if __name__ == '__main__':
    app.run(debug=getenv('WEB_DEBUG', False), port=getenv('FETCH_API_PORT'))
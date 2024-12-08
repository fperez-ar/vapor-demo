#! /bin/bash
# read -p "Please create .env file in root directory"
blink=$(tput blink)
bold=$(tput bold)
normal=$(tput sgr0)
echo -e $blink"Welcome $USER$normal"
echo -e "Normally you wouldn't commit the env file to .git\nbut as an example I will create one for you"
echo -e "$bold creating .env files$normal"
echo "BASE_URL=http://api.steampowered.com
STORE_API=https://store.steampowered.com/api
STORE_URL=https://store.steampowered.com/app/
DB_NAME=apps.db
# True to activate file watching
WEB_DEBUG=False
# api used to fetch from db
FETCH_API_URL=http://127.0.0.1
FETCH_API_PORT=33333
FETCH_API_ENDPOINT=/api/query
" > .env
echo -e "$bold creating virtual env$normal"
python3 -m venv .virtualenv
echo -e "$bold activate virtual env$normal"
source .venv/bin/activate
echo -e "$bold installing deps$normal"
/usr/bin/env pip install -r requirements.txt > /dev/null
echo -e "$bold populating db, this might take some minutes depending on network...$normal"
/usr/bin/env python src/populate_db.py
# web and api will run detached, so terminal will have to be killed 
# or the python processed will have to be identified and killed 
# run web as to use proper db dependency from utils
/usr/bin/env python src/web/main.py &
/usr/bin/env python -m src.api.get_apps &
echo "should be running in http://127.0.0.1:5000/web/search"

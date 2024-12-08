from os import getenv
from requests import get
from request_utils import status_validation, path_validation

def get_app_info(appid: int):
    # get any apps info by the id (using store api)
    store_api: str = getenv('STORE_API')
    response = get(f'{store_api}/appdetails?appids={appid}')
    status_validation(response)
    json = response.json()
    path_validation(json, [str(appid),'data','categories'])
        tags = response.json()[str(appid)]['data']['categories']
    print(tags)

import dotenv
dotenv.load_dotenv()
get_app_info(107410)
"""
    validate response object status code is in provided valid_list
    raise exception if not
""" 
def status_validation(response: object, valid_codes: list = [200]):
    if response.status_code in valid_codes:
        return True
    else:
        raise Exception(f'Request failed with status code: {response.status_code}')

"""
    validate a list of keys (['person', 'name']) 
    which describes a path exists in dict, 
    in the provided order
    return True if it does
    raise Exception if it doesn't
"""
def path_validation(target: dict, keys: list):
    for key in keys:
        if key in target and isinstance(target, dict):
            target = target[key]
        else:
            raise Exception(f'Key: {key} not found in {target}')
    return True
import requests
def yield_results(basic_params):
        result = requests.get(endpoint, params=basic_params)
        while True:
            if (result.status_code != 200):
                yield (None, result.json())
                break
            else:
                result_obj = result.json()
                yield (result_obj, None)
                cursor = result_obj.get('cursor', None)
                if cursor is None:
                    break
                else:
                    params = basic_params.copy()
                    params['cursor'] = cursor
                    result = requests.get(endpoint, params=params)
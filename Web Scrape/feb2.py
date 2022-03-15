import requests
import sys
endpoint = "https://archive.org/details/pastpages"
result = requests.get(endpoint)
sys.stdout = open("onfeb2.txt", "w")
print(result.text)
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
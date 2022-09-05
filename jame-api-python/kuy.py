from urllib import response
import requests
import json
import jsonpath
from jsonschema import validate


url = 'https://auth.dev.cryptoknights.games/guest/register'

response = requests.post(url)
# print(response.content)

assert response.status_code == 200

print(response.status_code)

# response_json = json.loads(response.text)
response_json = json.loads(response.text)
# id = jsonpath.jsonpath(response_json,'jwt') #### select which key you want to get the value
print(response_json)

schema = {
    "type":"object",
    "required": [
        "jwt"
    ],
    "properties": {
        "jwt": {
            "type":"string"
        }
    }
}

# validate(instance=response_json, schema=schema)
# print(id)
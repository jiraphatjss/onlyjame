from urllib import response
import requests
import json
import jsonpath
import random
from jsonschema import validate

request_url = 'https://auth.dev.cryptoknights.games/email/request-register-otp'
request_body = {'email':""}
response = requests.post(request_url,json = request_body)
    # response = requests.post(request_url,json = used_email)
global status_code
status_code = response.status_code
global response_json
response_json = json.loads(response.text)
print(response_json)
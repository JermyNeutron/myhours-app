import json
import sys

import requests

sys.path.append('.')

from src.timer_class import sessionCurrent


url = "https://api2.myhours.com/api/Logs?date=2024-02-28&step=100"


with open("temp/test_credentials.txt", "r") as file:
    # LIVE: temp/credentials.txt
    json_data = file.read()
mydictionary = json.loads(json_data)
# print(mydictionary)
# atok = mydictionary["accessToken"]

# print(atok)

payload = {}
headers = {
    "Accept": "application/json",
    "api-version": "1.0",
    "Authorization": f'Bearer {mydictionary["accessToken"]}',
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(type(response.json())) # list
for dictionary in response.json():
    print(sessionCurrent(dictionary))

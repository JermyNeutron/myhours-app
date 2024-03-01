import requests
import json
from timer_class import MyHour_Session_Current


url = "https://api2.myhours.com/api/Logs?date=2024-02-28&step=100"


with open("test_credentials.txt", "r") as file:
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
    print(MyHour_Session_Current(dictionary))

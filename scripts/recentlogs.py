from datetime import datetime
import pytz
import json
import sys

import requests

sys.path.append('.')

from src.timer_class import sessionCurrent

current_time_iso = ''

def timestamp():
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    global current_time_iso
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    # print(f"timestamp func returns: {current_time_iso}") # OPTIONAL
    current_time_iso = current_time_iso[:10]
    print(current_time_iso)
    return current_time_iso

def requestlog():
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

if __name__ == '__main__':
    timestamp()

    url = f"https://api2.myhours.com/api/Logs?date={current_time_iso}&step=100"
    print(url)

    requestlog()
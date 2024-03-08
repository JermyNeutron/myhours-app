from datetime import datetime
import pytz
import json
import sys

import requests

sys.path.append('.')

from src.timer_class import sessionCurrent


def timestamp():
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    # print(f"timestamp func returns: {current_time_iso}") # OPTIONAL
    current_time_iso = current_time_iso[:10]
    return current_time_iso


def requestlog(url, test=False):
    # Paths
    credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"
    with open(credentials_path, "r") as file:
        json_data = file.read()
    mydictionary = json.loads(json_data)

    payload = {}
    headers = {
        "Accept": "application/json",
        "api-version": "1.0",
        "Authorization": f'Bearer {mydictionary["accessToken"]}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(type(response.json())) # list
    for dictionary in response.json():
        print(f"\n{sessionCurrent(dictionary)}\n")


def main(test=False):
    current_date = timestamp()
    url = f"https://api2.myhours.com/api/Logs?date={current_date}&step=100"
    requestlog(url, test)


if __name__ == '__main__':
    main(test=True)

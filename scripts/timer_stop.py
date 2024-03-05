from datetime import datetime
import json
import sys

import pytz
import requests

sys.path.append('.')

from src.timer_class import sessionCurrent


# # oai suggestion
def timestamp():
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    print(current_time_iso) # optional
    return current_time_iso

def main():
    current_time = timestamp()

    user_credfile = "temp/test_credentials.txt"
    # LIVE: credentials.txt
    with open(user_credfile, "r") as user_cred:
        json_data = user_cred.read()
    credentials = json.loads(json_data)

    current_session_info_text = "temp/test_log_current.txt"
    with open(current_session_info_text, 'r') as session_info:
        json_info = session_info.read()
    current_log = sessionCurrent(json.loads(json_info))

    url = "https://api2.myhours.com/api/Logs/stoptimer"

    payload = json.dumps({"logId": current_log.log_id, "time": f"{current_time}"})
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials['accessToken']}",
    }

    pre_response = requests.request("POST", url, headers=headers, data=payload)
    response = pre_response.json()
    cl_response = sessionCurrent(response)

    print(cl_response)

if __name__ == '__main__':
    main()
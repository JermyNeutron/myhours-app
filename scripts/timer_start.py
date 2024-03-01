import json
import requests
import time
import pytz
from datetime import datetime
from src.timer_class import MyHour_Session_Current

# retrieve current local time in ISO 8601 format
def timestamp():
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    # print(f"timestamp func returns: {current_time_iso}") # OPTIONAL
    return current_time_iso

# ACCESS user credentials
def readfile():
    filename = "temp/test_credentials.txt"
    # LIVE: credentials.txt
    with open(filename, "r") as file:
        json_data = file.read()
    accessed_credentials = json.loads(json_data)
    # print(f"readfile() return: {accessed_credentials}") # OPTIONAL
    return accessed_credentials

# POST timer START
def timer_start():
    current_time = timestamp()
    credentials = readfile()

    url = "https://api2.myhours.com/api/Logs/startNewLog"

    payload = json.dumps(
        {
            "projectId": None,
            "taskId": None,
            "note": "Started via API",
            "date": f"{current_time}",
            "start": f"{current_time}",
            "billable": False,
            "expense": 0,
            "customField1": 0,
            "customField2": 0,
            "customField3": 0,
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials['accessToken']}",
    }

    pre_response = requests.request("POST", url, headers=headers, data=payload)

    # convert request into type(dict)
    response = pre_response.json()
    cl_response = MyHour_Session_Current(response)

    print(cl_response) # OPTIONAL

    # UPDATE file path
    with open('temp/test_log_current.txt', 'w') as file:
        js_response = json.dumps(response)
        file.write(js_response)

    return current_time

if __name__ == '__main__':

    time_clock_start = time.time()
    current_time = timer_start()
    
    time_clock_stop = time.time()
    clock_duration = time_clock_stop - time_clock_start
    # convert iso to military HHMM
    dt_obj = datetime.fromisoformat(current_time[:-1])
    hour = dt_obj.hour
    minute = dt_obj.minute

    print(f'We started a new MyHours timer at {hour:02d}{minute:02d} in {clock_duration}s')
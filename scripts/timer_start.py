from datetime import datetime
import json
import sys
import time

import pytz
import requests

sys.path.append('.')

from src.timer_class import sessionCurrent


# retrieve current local time in ISO 8601 format
def timestamp():
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    return current_time_iso


# ACCESS user credentials
def r_credentials(test=False):
    # Paths
    credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"

    with open(credentials_path, "r") as file:
        json_data = file.read()
    accessed_credentials = json.loads(json_data)
    return accessed_credentials


def r_projects(test=False):
    # Paths
    project_path = "temp/projects.txt" if not test else "temp/test_projects.txt"

    with open(project_path, "r") as file:
        json_data = file.read()
    accessed_projects = json.loads(json_data)
    return accessed_projects


# POST timer START
def main(test=False, projectId=None, taskId=None):
    # Paths
    log_path = "temp/log_current.txt" if not test else "temp/test_log_current.txt"
    time_path = "temp/log_time.txt" if not test else "temp/test_log_time.txt"

    current_time = timestamp()
    credentials = r_credentials(test)

    url = "https://api2.myhours.com/api/Logs/startNewLog"

    payload = json.dumps(
        {
            "projectId": projectId,
            "taskId": taskId,
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
    cl_response = sessionCurrent(response)
    if test:
        print(cl_response)

    # UPDATE file path
    with open(log_path, 'w') as file:
        js_response = json.dumps(response)
        file.write(js_response)
        
		
    with open(time_path, 'w') as file:
        file.write(current_time)
	
    return current_time
    
if __name__ == '__main__':
    # OPTIONAL START duration timer
    time_clock_start = time.time()

    # main func
    current_time = main(test=True)
    
    # OPTIONAL STOP duration timer
    time_clock_stop = time.time()
    clock_duration = time_clock_stop - time_clock_start
    # OPTIONAL convert iso to military HHMM
    dt_obj = datetime.fromisoformat(current_time[:-1])
    hour = dt_obj.hour
    minute = dt_obj.minute

    print(f'We started a new MyHours timer at {hour:02d}{minute:02d} in {clock_duration}s')
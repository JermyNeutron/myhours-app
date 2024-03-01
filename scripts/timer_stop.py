# 83745937
import requests
import json
from timer_class import MyHour_Session_Current
from datetime import datetime, timezone, timedelta
import pytz

# original; creates 7 logs simultaneously
# def timestamp():
#     current_time_utc = datetime.now(timezone.utc)
#     pst_offset = timedelta(hours=-8)
#     current_time_local = current_time_utc + pst_offset
#     current_time_iso = current_time_local.strftimez("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
#     print(current_time_iso) # OPTIONAL
#     return(current_time_iso)

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

    user_credfile = "test_credentials.txt"
    with open(user_credfile, "r") as user_cred:
        json_data = user_cred.read()
    credentials = json.loads(json_data)

    current_session_info_text = "log_current.txt"
    with open(current_session_info_text, 'r') as session_info:
        json_info = session_info.read()
    current_log = MyHour_Session_Current(json.loads(json_info))

    url = "https://api2.myhours.com/api/Logs/stoptimer"

    payload = json.dumps({"logId": current_log.log_id, "time": f"{current_time}"})
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials['accessToken']}",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    main()
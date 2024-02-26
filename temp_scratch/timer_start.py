import json
import requests


def readfile():
    filename = "test_credentials.txt"
    with open(filename, "r") as file:
        json_data = file.read()
    accessed_credentials = json.loads(json_data)
    return accessed_credentials


credentials = readfile()

url = "https://api2.myhours.com/api/Logs/startNewLog"

payload = json.dumps(
    {
        "projectId": None,
        "taskId": None,
        "note": "Started via API",
        "date": "2023-03-16T13:08:00.899Z",
        "start": "2023-03-16T12:08:00.899Z",
        "billable": True,
        "expense": 0,
        "customField1": 0,
        "customField2": 0,
        "customField3": 0,
    }
)
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {credentials["accessToken"]}",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

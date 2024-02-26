# 83745937
import requests
import json

filename = "test_credentials.txt"
with open(filename, "r") as file:
    json_data = file.read()
credentials = json.loads(json_data)

url = "https://api2.myhours.com/api/Logs/stoptimer"

payload = json.dumps({"logId": 68908595, "time": "2024-02-25T16:10:02.139508-08:00"})
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {credentials['accessToken']}",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

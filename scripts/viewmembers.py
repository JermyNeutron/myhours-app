import json
import requests

def main(test=False):
    credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"
    url = "https://api2.myhours.com/api/Users/getAll"

    with open(credentials_path, "r") as file:
        json_data = file.read()
    credentials = json.loads(json_data)

    payload={}
    headers = {
    'Accept': 'application/json',
    'api-version': '1.0',
    'Authorization': f"Bearer {credentials['accessToken']}"
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()

    if test:
        print(response)
        filepath = "temp/test_viewmember.txt"
        with open(filepath, "w") as file:
            json.dump(response, file)
    return(response)


if __name__ == '__main__':
    main(test=True)
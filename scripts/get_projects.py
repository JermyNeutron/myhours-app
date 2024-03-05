import json
import sys

import requests

sys.path.append('.')

from src.timer_class import userProjects

url = "https://api2.myhours.com/api/Projects/getAll"

def main():
  with open("temp/test_credentials.txt", 'r') as file:
  # LIVE: temp/credentials.txt
      json_data = file.read()
  data_proj = json.loads(json_data)

  payload={}
  headers = {
    'Accept': 'application/json',
    'api-version': '1.0',
    'Authorization': f'Bearer {data_proj["accessToken"]}'
  }

  response = requests.request("GET", url, headers=headers, data=payload).json()

  return response

def test():
   response = main()
   for proj in response:
      print(userProjects(proj))

def display_list():
  response = main()
  # sort response based on key and case-insensitive ASCII
  sorted_resp = sorted(response, key= lambda x: x['name'].lower())

# print "name" key
  for proj in sorted_resp:
     print(userProjects(proj).project_name)

if __name__ == '__main__':
    main()
    test()
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

  with open("temp/test_projects.txt", 'w') as file:
    #  LIVE: temp/projects.txt
     json.dump(response, file)
    #  print('writing complete') # OPTIONAL

  return response

# prints project names only
def display_list():
  with open("temp/test_projects.txt", "r") as file:
     pre_response = file.read()
     response = json.loads(pre_response)
  # sort response based on key and case-insensitive ASCII
  sorted_resp = sorted(response, key= lambda x: x['name'].lower())

  # print "name" key
  for proj in sorted_resp:
     print(userProjects(proj).name, end=', ')

# updates projects.txt and reads user projects
if __name__ == '__main__':
  main()
  with open("temp/test_projects.txt", "r") as file:
    pre_response = file.read()
    response = json.loads(pre_response)
    # print(response)
    for proj in response:
        print(userProjects(proj))
  
  # display_list()
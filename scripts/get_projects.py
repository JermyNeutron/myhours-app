import json
import sys

import requests

sys.path.append('.')

from src.timer_class import userProjects

import authenticate

def rtrvproj(test=False):
  # Paths
  credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"
  project_path = "temp/projects.txt" if not test else "temp/test_projects.txt"
  
  with open(credentials_path, 'r') as file:
      json_data = file.read()
  data_proj = json.loads(json_data)

  payload={}
  headers = {
    'Accept': 'application/json',
    'api-version': '1.0',
    'Authorization': f'Bearer {data_proj["accessToken"]}'
  }
  url = "https://api2.myhours.com/api/Projects/getAll"

  response = requests.request("GET", url, headers=headers, data=payload).json()

  with open(project_path, 'w') as file:
     json.dump(response, file)
    #  print('writing complete') # OPTIONAL

  return response


# prints project names only
def display_list(test=False):
  # Paths
  project_path = "temp/projects.txt" if not test else "temp/test_projects.txt"

  with open(project_path, "r") as file:
    pre_response = file.read()
    response = json.loads(pre_response)
  # sort response based on key and case-insensitive ASCII
  sorted_resp = sorted(response, key= lambda x: x['name'].lower())

  # print "name" key
  print("Your current projects include:\n")
  for proj in sorted_resp:
     print(userProjects(proj).name, end=', ')
  print('')

  return sorted_resp
# updates projects.txt and reads user projects

def main(test=False):
  maxatmp = 3
  exatmp = 0
  while exatmp < maxatmp:
    try:
      rtrvproj(test)
      break
    except json.decoder.JSONDecodeError as e:
      authenticate.main(test)
      exatmp += 1
    except Exception as e:
      print(f"An error occurred while retrieving projects: {e}")
      break
    except:
      rtrvproj(test)
      exatmp += 1
  else:
    print('Max attempts reached while retrieving projects.')

if __name__ == '__main__':
  test = True
  maxatmp = 3
  exatmp = 0
  while exatmp < maxatmp:
    try:
      rtrvproj(test)
      display_list(test)
      exatmp += 1
      break
    except json.decoder.JSONDecodeError as e:
      authenticate.main(test)
      exatmp += 1
    except Exception as e:
      print(f"An error occurred while retrieving projects: {e}")
      break
    except:
      rtrvproj(test)
      exatmp += 1
  else:
    print('Max attempts reached while retrieving projects.')
  print(f"{exatmp} of {maxatmp} attempts used.")
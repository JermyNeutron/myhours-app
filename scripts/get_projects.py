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
	cred_data = json.loads(json_data)

	payload={}
	headers = {
	'Accept': 'application/json',
	'api-version': '1.0',
	'Authorization': f'Bearer {cred_data["accessToken"]}'
	}
	url = "https://api2.myhours.com/api/Projects/getAll"

	response = requests.request("GET", url, headers=headers, data=payload).json()

	with open(project_path, 'w') as file:
		json.dump(response, file)
	if test:
		print('writing complete') # OPTIONAL

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

	# returns user projects
	return sorted_resp


def main_rtrvproj(test=False):
	maxatmp = 3
	exatmp = 0
	while exatmp < maxatmp:
		try:
			rtrvproj(test)
			break
		except json.decoder.JSONDecodeError as e:
			authenticate.main(test)
			exatmp += 1
			print("Credentials refreshed.")
		except Exception as e:
			print(f"An error occurred while retrieving projects: {e}")
			break
	else:
		print('Max attempts reached while retrieving projects.')


def main_displist(test=False):
	maxatmp = 3
	exatmp = 0
	while exatmp < maxatmp:
		try:
			proj_list = display_list(test)
			return proj_list
		except json.decoder.JSONDecodeError as e:
			authenticate.main(test)
			exatmp += 1
			print("Credentials refreshed.")
		except Exception as e:
			print(f"An error occurred while retrieving projects: {e}")
			break
	else:
		print('Max attempts reached while retrieving projects.')
	return proj_list


def genproj(test=False):
	# Paths
	credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"

	with open(credentials_path, "r") as file:
		cred_data = json.loads(file.read())

	url = "https://api2.myhours.com/api/Projects"

	# input project name
	new_projname = input("New project name: ")
	
	# check with project return to make sure project does not already exist

	payload = json.dumps({
	"name": f"{new_projname}",
	# "clientId": None,
	# "invoiceMethod": 2,
	# "notes": "Project description",
	# "approved": False,
	# "customId": "xyz-0392432",
	# "rate": 100
	})
	headers = {
	'Content-Type': 'application/json',
	'Authorization': f"Bearer {cred_data['accessToken']}"
	}

	pre_response = requests.request("POST", url, headers=headers, data=payload)
	response = pre_response.json()
	
	return response


if __name__ == '__main__':
	main_rtrvproj(test=True)
	main_displist(test=True)
	genproj(test=True)
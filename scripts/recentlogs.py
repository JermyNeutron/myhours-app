from datetime import datetime as dt_time
from time import sleep
import datetime
import pytz
import json
import sys

import requests

sys.path.append('.')

from src.timer_class import sessionCurrent, userProjects, userLogs

import authenticate
import timestamp
import editlog


def requestlog(test=False):
	# Paths
	credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"
	log_history_path = "temp/log_history.txt" if not test else "temp/test_log_history.txt"

	current_date, current_time_iso = timestamp.main()
	url = f"https://api2.myhours.com/api/Logs?date={current_date}&step=100"

	with open(credentials_path, "r") as file:
		json_data = file.read()
	mydictionary = json.loads(json_data)

	payload = {}
	headers = {
		"Accept": "application/json",
		"api-version": "1.0",
		"Authorization": f'Bearer {mydictionary["accessToken"]}',
	}

	response = requests.request("GET", url, headers=headers, data=payload).json()

	with open(log_history_path, 'w') as file:
		json.dump(response, file)

	return response


def pseutime(test=False):
	# Paths
	log_path = "temp/log_time.txt" if not test else "temp/test_log_time.txt"

	current_date, current_time_iso = timestamp.main()
	with open(log_path, "r") as file:
		log_time = file.read()
	current_time_iso = dt_time.strptime(current_time_iso, "%Y-%m-%dT%H:%M:%S.%f%z")
	log_time = dt_time.strptime(log_time, "%Y-%m-%dT%H:%M:%S.%f%z")
	return str(current_time_iso - log_time)


def main(test=False):
	current_date, current_time_iso = timestamp.main()
	maxatmp = 3
	exatmp = 0
	while exatmp < maxatmp:
		try:
			response = requestlog(test)
			if response == []:
				print(f'No logs recorded for today, {current_date}\n')
				input("Press any key to return: ")
			else:
				for index, dictionary in enumerate(response):
					print(f"{index+1}. ", end="")
					print(f"{str(userLogs(dictionary))}\n")
				choice = input("Type E to EDIT: ")
				if choice.lower() != "e":
					pass
				else:
					editlog.main(test)
			break
		except json.decoder.JSONDecodeError as e:
			authenticate.main(test)
			exatmp += 1
			print("Credentials refreshed.")
		except Exception as e:
			print(f"An error occurred while retrieving logs: {e}")
			exatmp += 1
	else:
		print('Max attempts reached while retrieving logs')


if __name__ == '__main__':
	while True:
		choice = input("select a test:\n1) main\n2) requestlog\n3) pseutime\n4) timestamp\n\n: ")
		if choice == '1':
			main(test=True)
			break
		elif choice == '2':
			requestlog(test=True)
			break
		elif choice == '3':	
			print(pseutime(test=True))
			break
		elif choice == '4':	
			print(timestamp.main())
			break
		elif choice.lower() == 'q':
			break
		else:
			print('Invalid test choice')
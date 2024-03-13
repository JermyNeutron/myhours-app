from datetime import datetime, timedelta
import pytz
import json
import sys

import requests

sys.path.append('.')

from src.timer_class import sessionCurrent, userProjects, userLogs

import authenticate

def timestamp():
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    pst = pytz.timezone('America/Los_Angeles')
    current_time_pst = current_time_utc.astimezone(pst)
    current_time_iso = current_time_pst.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
    current_date = current_time_iso[:10]
    return current_date, current_time_iso


def requestlog(test=False):
	# Paths
	credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"
	log_history_path = "temp/log_history.txt" if not test else "temp/test_log_history.txt"

	current_date, current_time_iso = timestamp()
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

	current_date, current_time_iso = timestamp()
	with open(log_path, "r") as file:
		log_time = file.read()
	current_time_iso = datetime.strptime(current_time_iso, "%Y-%m-%dT%H:%M:%S.%f%z")
	log_time = datetime.strptime(log_time, "%Y-%m-%dT%H:%M:%S.%f%z")
	return str(current_time_iso - log_time)


def main(test=False):
	current_date = timestamp()
	maxatmp = 3
	exatmp = 0
	while exatmp < maxatmp:
		try:
			response = requestlog(test)
			if response == []:
				return f'No logs recorded for {current_date}\n'
			else:
				for dictionary in response:
					print(f"{str(userLogs(dictionary))}\n")
				print()
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
    # main(test=True)
	# request = requestlog(test=True)
	print(pseutime(test=True))
	# print(timestamp())
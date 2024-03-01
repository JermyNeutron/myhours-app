# Authenticate
## retrieve bearer token

import configparser
import json
import requests
import time


# check config population
def config_check():

    # # start clock
    # time_start = time.time()

    config = configparser.ConfigParser()
    config.read("config/test_config.ini")
    # LIVE: config.ini

    global missing_authentication
    missing_authentication = 0

    # retrieve email
    if config.has_option("MyHours", "login_email"):
        ini_email = config.get("MyHours", "login_email")
        if ini_email == "":
            print("Oops! Open config.ini and provide an email.", end=" ")
            missing_authentication += 1
        else:
            # print(f"Email is {ini_email}", end=' ') # OPTIONAL
            email_populated = ini_email
    else:
        print("The email key is missing!")
        missing_authentication += 1

    # retrieve password
    if config.has_option("MyHours", "login_password"):
        ini_password = config.get("MyHours", "login_password")
        if ini_password == "":
            print("Oops! Open config.ini and provide a password.")
            missing_authentication += 1
        else:
            # print(f"Password is stored.") # OPTIONAL
            password_provided = ini_password
    else:
        print("The password key is missing!")
        missing_authentication += 1

    # # end clock # OPTIONAL
    # time_end = time.time()
    # print(f'{time_end - time_start}s elapsed')

    # exit function
    if missing_authentication > 0:
        return print("Please resolve your config.ini")

    # continue function
    return email_populated, password_provided


# user authentication and bearer token retrieval
def mh_login(email, password):
    url = "https://api2.myhours.com/api/tokens/login"

    payload = json.dumps(
        {
            "grantType": "password",
            "email": f"{email}",
            "password": f"{password}",
            "clientId": "api",
        }
    )
    headers = {"Content-Type": "application/json", "api-version": "1.0"}

    # Calls bearer token
    pre_response = requests.request("POST", url, headers=headers, data=payload)
    response = pre_response.json()
    if "message" in response:
        print("Incorrect email or password. Review the config.ini")
        return None
    else:
        # print(response)  # OPTIONAL
        # print(type(response))  # OPTIONAL
        return response


# overwriting credentials file
def writing_response(response, credentials_file="temp/test_credentials.txt"):  # LIVE: credentials.txt
    with open(credentials_file, "w") as file:
        json.dump(response, file)


# check credentials file # OPTIONAL
def checking_response(credentials_file="temp/test_credentials.txt"):
    with open(credentials_file, "r") as file:
        json_data = file.read()
        print(
            f"This is read from the .txt file:\n{json_data}\nCredentials successfully retrieved."
        )  # OPTIONAL
    # verify dictionary key # OPTIONAL
    credentials = json.loads(json_data)
    print(f'i found this key: {credentials["accessToken"]}')


# testing purposes
if __name__ == "__main__":
    # start time # optional
    time_start = time.time()

    # check and retrieve config population
    email, password = config_check()
    if not missing_authentication:
        # user authentication and bearer token retrieval
        response = mh_login(email, password)
        if response is None:
            print("Program has exited.")
        else:
            writing_response(response)
            checking_response()  # OPTIONAL

    # end clock # optional
    time_end = time.time()
    print(f"{time_end - time_start}s elapsed")

from time import sleep
import json

import requests

import cls_screen
import recentlogs
import timestamp


def api_edit(id, note, test=False):
    # Paths
    credentials_path = "temp/credentials.txt" if not test else "temp/test_credentials.txt"

    url = "https://api2.myhours.com/api/Admin/editLogOnBehalf"
    
    with open(credentials_path, 'r') as file:
        json_data = file.read()
    cred_data = json.loads(json_data)

    payload = json.dumps({
        "id": id,
        "userId": 956662,
        "note": f"{note}",
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {cred_data["accessToken"]}',
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)
    sleep(3)


def rel_hist(test=False):
    # Paths
    log_history_path = "temp/log_history.txt" if not test else "temp/test_log_history.txt"

    try:
        recentlogs.requestlog(test)
        with open(log_history_path, "r") as file:
            json_data = file.read()
        response = json.loads(json_data)
        print("Edit Logs\n")
        for index, item in enumerate(response):
            print(f"{index+1}. id: #{item['id']}\nnote: {item['note']}\n")
    except requests.exceptions.ConnectionError as e:
        print("Internet connection failed.\nPlease try again later.")
        sleep(3)
        response = False
    return response


def main(test=False):
    # Selects log to edit
    while True:
        cls_screen.screen()
        response = rel_hist(test)
        if response:
            choice = input("Q) Go Back\nSelect log: ")
            if choice == "":
                break
            elif choice.lower() != "q":
                try:
                    # If valid selection, input to overwrite note
                    while True:
                        cls_screen.screen()
                        selchoice = response[int(choice)-1]
                        print(f"Editing Log #{choice}: {selchoice['id']}\n\"{selchoice['note']}\"\n\nQ) Go Back\nEnter a new log note:")
                        modnote = input("")
                        if modnote == "":
                            pass
                        # User verifies new log note
                        elif modnote.lower() != "q":
                            while True:
                                cls_screen.screen()
                                finnote = input(f"Are you sure you want to save this note for Log #{selchoice['id']}?\n\"{modnote}\"\n\nY) Save\nQ) Go Back\n: ")
                                if finnote == "":
                                    pass
                                # API edit
                                elif finnote.lower() != "q":
                                    try:
                                        api_edit(selchoice['id'], modnote, test)
                                    except requests.exceptions.ConnectionError as e:
                                        print("\nInternet connection lost.\nPlease try again later.")
                                        sleep(3)
                                    except Exception as e:
                                        print(e)
                                        sleep(3)
                                else:
                                    break
                        else:
                            break
                except IndexError as e:
                    print("Invalid selection")
                    sleep(2)
                except ValueError as e:
                    print("Invalid selection")
                    sleep(2)
            else:
                break
        else:
            break
    if test:
        print('exiting editlog.py')


if __name__ == '__main__':
    main(test=True)
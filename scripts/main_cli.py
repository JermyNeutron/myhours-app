# main cli
import os
import sys
import time

sys.path.append('.')

from src.timelap import timelap
from src import menu_strings

import authenticate
import get_projects
import timer_start
import timer_stop
import recentlogs


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('cls')

# @timelap
def log_check(test=False):
    log = recentlogs.requestlog(test)
    status = False
    for log_entry in log:
        if log_entry.get("running", False):
            active_timer = log_entry
            status = True
    return status
    

def timer_statement(status):
    if status is False:
        return "Let's get cooking!"
    else:
        return "Can't Stop! Won't Stop"


def timer_start_options():
    clear_screen()
    while True:
        proj_list = get_projects.display_list()

        usel_sub = input('\nHit <Enter> to start a blank timer\n\nType in your project: ')

        if usel_sub == '':
            usel_sub = None
            projectId = None

        if usel_sub is not None:
            for proj in proj_list:
                if proj["name"] == usel_sub:
                    projectId = proj["id"]
                    print(f'Timer started for {usel_sub}')
                    return projectId
            else:
                print("Invalid selection.")
        return projectId


def main_screen(test=False):
    authenticate.main(test)
    get_projects.main(test)
    # initialize timer status
    while True:
        clear_screen()
        options = timer_statement(log_check(test))
        print(menu_strings.main(options, test))
        # print(main_options(test))
        usel = input(': ')
        if usel.lower() == 'q':
            if timer_status:
                timer_stop.main(test)
            break
        elif usel.lower() == 'test' or usel.lower() == 'break':
            break
        elif usel == '1':
            projectId = timer_start_options()
            timer_start.main(test, projectId)
            timer_status = True
            print(timer_status)
            time.sleep(2)
        elif usel == '2':
            timer_stop.main(test)
            timer_status = False
            time.sleep(4)
            clear_screen()
        
        
if __name__ == '__main__':
    main_screen(test=True)

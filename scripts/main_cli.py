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
    # print(type(log))
    if log == []:
        pass
    else:
        for log_entry in log:
            if log_entry.get("running", False):
                active_timer = log_entry
                status = True
    return status
    

def timer_statement(status):
    if status is False:
        return "Let's get cooking!\n"
    else:
        return "Can't Stop! Won't Stop\n"


def timer_start_options(test=False):
    clear_screen()
    while True:
        proj_list = get_projects.main_displist(test)

        usel_sub = input("""\nEnter) Start Empty Timer
    2) Create New Project
    Q) Go Back\n\nType in your project: """)

        if usel_sub.lower() == 'q':
            usel_sub = None
            return False
        elif usel_sub == '':
            usel_sub = None
            projectId = None
            return projectId
        elif usel_sub == '2':
            clear_screen()
            get_projects.genproj(test)
            get_projects.main_rtrvproj(test)
            clear_screen()
            time.sleep(2)
        else: # usel_sub is not None:
            maxatmp = 1
            atmp = 0
            while atmp < maxatmp:
                for proj in proj_list:
                    if proj["name"] == usel_sub:
                        projectId = proj["id"]
                        print(proj["id"])
                        print(f'Timer started for {usel_sub}')
                        return projectId
                else:
                    clear_screen()
                    print(f"\"{usel_sub}\" is an invalid selection.\n\n")
                    atmp += 1


def main_screen(test=False):
    authenticate.main(test)
    get_projects.main_rtrvproj(test)
    # initialize timer status
    while True:
        clear_screen()
        welcome_statement = timer_statement(log_check(test))
        print("MyHours App")
        if log_check(test):
            print(recentlogs.pseutime(test))
        print(welcome_statement)
        print(menu_strings.main(test))
        usel = input(': ')
        if usel.lower() == 'q':
            if log_check(test):
                timer_stop.main(test)
            break
        elif usel.lower() == 'test' or usel.lower() == 'break':
            break
        elif usel == '1':
            while True:
                projectId = timer_start_options(test)
                if projectId is not False:
                    timer_start.main(test, projectId)
                    time.sleep(2)
                    break
                else:
                    time.sleep(2)
                    break
        elif usel == '2':
            if log_check(test):
                timer_stop.main(test)
                time.sleep(4)
                clear_screen()
        elif usel == '3':
            while True:
                clear_screen()
                recentlogs.main(test)
                input("Press any key to return to menu: ")
                break
        # refresh time
        elif usel == '9':
            pass
        else:
            pass
        
        
if __name__ == '__main__':
    main_screen(False)

# main cli
import os
import sys
import time

sys.path.append('.')

import authenticate, get_projects, timer_start, timer_stop, recentlogs

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('cls')

def main_screen_options():
    pass

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

def timer_statement(status):
    if status is False:
        return "Let's get cooking!"
    else:
        return "Can't Stop! Won't Stop"

def main_screen():
    get_projects.main()
    # initialize status
    timer_status = False
    while True:
        statement = timer_statement(timer_status)
        clear_screen()
        print(f"""MyHours App
{statement}

Select an option:
1. Start Timer,
2. Stop Timer,
              
Q. Exit""")
        usel = input(': ')
        if usel.lower() == 'q':
            if timer_status:
                timer_stop.main()
            break
        elif usel == '1':
            projectId = timer_start_options()
            timer_start.main(projectId)
            timer_status = True
            print(timer_status)
            time.sleep(2)
        elif usel == '2':
            timer_stop.main()
            timer_status = False
            time.sleep(4)
            clear_screen()
        
        
if __name__ == '__main__':
    main_screen()

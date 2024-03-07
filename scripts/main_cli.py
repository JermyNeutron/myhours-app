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

def timer_start_options():
    clear_screen()
    while True:
        proj_list = get_projects.display_list()

        usel_sub = input('\nHit <Enter> to start a blank timer\n\nType in your project: ')

        if usel_sub is not None:
            for proj in proj_list:
                if proj["name"] == usel_sub:
                    projectId = proj["id"]
                    print(f'Timer started for {usel_sub}')
                    return projectId
            else:
                print("Invalid selection.")
        return projectId

def main_screen():
    get_projects.main()
    while True:
        clear_screen()
        print("""MyHours App
              
Select an option:
1. Start Timer,
2. Stop Timer,
              
Q. Exit""")
        usel = input(': ')
        if usel == 'q':
            break
        elif usel == '1':
            projectId = timer_start_options()
            timer_start.main(projectId)
        elif usel == '2':
            timer_stop.main()
            time.sleep(5)
            clear_screen()
        
        
if __name__ == '__main__':
    main_screen()

import os

def screen():
    if os.name == 'nt':
        _ = os.system("cls")
    else:
        _ = os.system('clear')

if __name__ == '__main__':
    screen()
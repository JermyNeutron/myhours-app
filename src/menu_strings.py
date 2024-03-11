def main(status, test=False):
    menu_live = f"""MyHours App
{status}
Type an option:
1) Start Timer
2) Stop Timer

Q) Save and Close
"""
    menu_testing = f"""MyHours App
{status}

Type an option:
1) Start Timer
2) Stop Timer

Test) Clean Exit

Q) Save and Close"""
    return menu_live if not test else menu_testing


if __name__ == '__main__':
    print(main("",test=True))
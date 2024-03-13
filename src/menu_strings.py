def main(test=False):
    menu_live = """Type an option:
1) Start Timer
2) Stop Timer
3) Retrieve Recent Logs

9) Refresh

Q) Save and Close
"""
    menu_testing = """Type an option:
1) Start Timer
2) Stop Timer
3) Retrieve Recent Logs

9) Refresh

Test) Clean Exit
Q) Save and Close"""
    menu_live_active = """"""
    menu_testing_active = """"""
    return menu_live if not test else menu_testing


if __name__ == '__main__':
    print(main(test=True))
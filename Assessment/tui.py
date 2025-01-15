"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

import os
from time import sleep
from process import *
from visual import *

mmenu_list = ["[A] View Data", "[B] Visualise Data", "[C] Export Data", "[X] Exit"]
mmenu_valid_options = ["A", "a", "B", "b", "C", "c", "X", "x"]
A_list = ["[A] View Reviews by Park",  "[B] Number of Reviews by Park and Reviewer Location", "[C] Average Score per year by Park", "[D] Average Score per Park by Reviewer Location", " ", "[X] Back to the Main Menu"]
B_list = ["[A] Most Reviewed Park", "[B] Average Scores", "[C] Park Ranking by Nationality", "[D] Most Popular Month by Park", " ", "[X] Back to the Main Menu"]
C_list = ["[A] TXT", "[B] CSV", "[C] JSON", " ", "[X] Press X to return to the Main Menu or Any Other Key to return to the submenu"]

def clear():
    sleep(1)
    os.system('cls')

def backtomainmenu():
    sub_menu_input = input()

    if sub_menu_input in ["X", "x"]:
        sleep(1)
        os.system('cls')
        mainmenu()

def title_workflow():
    title_length = 0
    title = "Disneyland Review Analyser"

    while title_length < len(title):
        print("-", end="")
        title_length += 1

def title_func():
    title_workflow()
    print("\nDisneyland Review Analyser\n", end="")
    title_workflow()

def submenu_a():
    sub_menu_input = input()
    if sub_menu_input in ["A", "a"]:
        #print("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]")
        specific_park()
    if sub_menu_input in ["B", "b"]:
        park_and_loc()
    if sub_menu_input in ["C", "c"]:
        park_and_year()
    if sub_menu_input in ["D", "d"]:
        avg_score()

def submenu_b():
    sub_menu_input = input()
    if sub_menu_input in ["A", "a"]:
        mostreviewed_park()
    if sub_menu_input in ["B", "b"]:
        scores_per_park()
    if sub_menu_input in ["C", "c"]:
        top10_per_park()
def submenu_c():
    sub_menu_input = input()
    if sub_menu_input in ["A", "a"]:
        export_txt("data/", "exported_data", "txt")
    if sub_menu_input in ["B", "b"]:
        export_txt("data/", "exported_data", "csv")
    if sub_menu_input in ["C", "c"]:
        export_txt("data/", "exported_data", "json")
def mainmenu():
    title_func()

    reading_data()

    print("\n\nPlease enter the data that corresponds with your desired menu choice:")
    for m in mmenu_list:
        print(m)
    main_menu_input = input()

    def menu1():
        if main_menu_input in ["A", "a"]:
            print("You have chosen the option A - View Data\n")
            clear()
            print(f"Please enter one of the following options:\n", end="")

            for a in A_list:
                print(a)

            submenu_a()
            backtomainmenu()

        elif main_menu_input in ["B", "b"]:
            print("You have chosen the option B - Visualise data\n")
            clear()
            print(f"Please enter one of the following options:\n", end="")
            for b in B_list:
                print(b)

            submenu_b()
            backtomainmenu()

        elif main_menu_input in ["C", "c"]:
            print("You have chosen the option C - Export Data")
            clear()

            for c in C_list:
                print(c)

            submenu_c()
            backtomainmenu()

        elif main_menu_input in ["X", "x"]:
            print("You have chosen the option X - Exit\n")
            print(f"Program closing in 5 seconds...")

            sleep(5)
            exit()

    def loop1():
        while main_menu_input in mmenu_valid_options:
            menu1()
    loop1()
    while main_menu_input not in mmenu_valid_options:
        print("The menu that you have selected doesn't exist. Please select one of the options above.")
        main_menu_input = input()
        loop1()

#mainmenu()

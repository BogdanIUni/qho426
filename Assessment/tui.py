"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

#Improted os and time to handle the transitions from a menu to another
import os
from time import sleep

from process import *
from visual import *

#Menu options as lists
mmenu_list = ["[A] View Data", "[B] Visualise Data", "[C] Export Data", "[X] Exit"]
A_list = ["[A] View Reviews by Park",  "[B] Number of Reviews by Park and Reviewer Location", "[C] Average Score per year by Park", "[D] Average Score per Park by Reviewer Location", " ", "[X] Back to the Main Menu"]
B_list = ["[A] Most Reviewed Park", "[B] Average Scores", "[C] Park Ranking by Nationality", "[D] Most Popular Month by Park", " ", "[X] Back to the Main Menu"]
C_list = ["[A] TXT", "[B] CSV", "[C] JSON", " ", "[X] Press X to return to the Main Menu"]

#List of error, post process and confirmation messages used throughout the program
corresponding_print = "\n\nPlease enter the data that corresponds with your desired menu choice:"
option_a = "You have chosen the option A - View Data\n"
option_b = "You have chosen the option B - Visualise data\n"
option_c = "You have chosen the option C - Export Data"
option_x = "You have chosen the option X - Exit\nProgram closing in 5 seconds..."
following_options = f"Please enter one of the following options:\n"
invalid = "Invalid option"
wrong_location = "This location is not on the list"
wrong_year = "This year is not on the list"
end_msg = "\nPress any key to return to this submenu"
invalid_option_mainmenu = "The menu that you have selected doesn't exist. Please select one of the options above."

#This function's purpose is to make the transitions from one menu to another, and make it feel more natural while also keeping the interface tidy
def clear():
    sleep(1)
    os.system('cls')

#This function is used to go back to the main menu from any of the submenus
def backtomainmenu():
    clear()
    from main import initial_menu
    from main import main_menu
    initial_menu()
    main_menu()

#The following 2 functions print the title and the number of dashes that will match the length of the title
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

#Handling the submenu A options and ensuring that the program runs as it should after a valid option has been chosen, as well as error handling
def submenu_a():
    sub_menu_input = input()
    if sub_menu_input in ["A", "a"]:
        specific_park()
        input()
        case(option_a, submenu_a, A_list)
    elif sub_menu_input in ["B", "b"]:
        park_and_loc()
        input()
        case(option_a, submenu_a, A_list)
    elif sub_menu_input in ["C", "c"]:
        park_and_year()
        input()
        case(option_a, submenu_a, A_list)
    elif sub_menu_input in ["D", "d"]:
        avg_score()
        input()
        case(option_a, submenu_a, A_list)
    elif sub_menu_input in ["X", "x"]:
        backtomainmenu()
    else:
        print(invalid)
        submenu_a()

#Handling the submenu B options and ensuring that the program runs as it should after a valid option has been chosen, as well as error handling
def submenu_b():
    sub_menu_input = input()
    if sub_menu_input in ["A", "a"]:
        mostreviewed_park()
        sleep(1)
        case(option_b, submenu_b, B_list)
    elif sub_menu_input in ["B", "b"]:
        scores_per_park()
        sleep(1)
        case(option_b, submenu_b, B_list)
    elif sub_menu_input in ["C", "c"]:
        top10_per_park()
        sleep(1)
        case(option_b, submenu_b, B_list)
    elif sub_menu_input in ["D", "d"]:
        rank_by_month()
        sleep(1)
        case(option_b, submenu_b, B_list)
    elif sub_menu_input in ["X", "x"]:
        backtomainmenu()
    else:
        print(invalid)
        submenu_b()

#Handling the submenu B options and ensuring that the program runs as it should after a valid option has been chosen, as well as error handling
def submenu_c():
    sub_menu_input = input()
    if sub_menu_input in ["A", "a"]:
        export_final("txt")
        print("Data exported successfully as a TXT file in the data folder")
        sleep(1)
        case(option_c, submenu_c, C_list)
    elif sub_menu_input in ["B", "b"]:
        export_final("csv")
        print("Data exported successfully as a CSV file in the data folder")
        sleep(1)
        case(option_c, submenu_c, C_list)
    elif sub_menu_input in ["C", "c"]:
        export_final("json")
        print("Data exported successfully as a JSON file in the data folder")
        sleep(1)
        case(option_c, submenu_c, C_list)
    elif sub_menu_input in ["X", "x"]:
        backtomainmenu()
    else:
        print(invalid)
        submenu_c()

#This function is used to loop through the options of every list
def menus_loop(valid_list):

    for option in valid_list:
        print(option)

#This function is used to print a confirmation message, clear the screen, print the menu options of each submenu and call the respective submenu function that will handle their respective options
#The main purpose of this function is to avoid repeatable code, save time and reuse functionalities
def case(option, submenu, menu_list):
    print(option)
    clear()

    menus_loop(menu_list)
    submenu()

#This option is separate from the other choices in the main menu because it is vastly different from the other ones
def case_x():
    print(option_x)

    sleep(5)
    exit()
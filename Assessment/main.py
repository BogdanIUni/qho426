"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
from tui import *

#This function will print the title, call the read data function and print the main menu
#I separated this section from the function "main_menu()" so the user can have a better experience in case of an error#
#(if this section was inside the main_menu function , these information will be printed over and over again, if the user input was incorrect)

def initial_menu():
    title_func()
    reading_data()

    print(corresponding_print)
    menus_loop(mmenu_list)

initial_menu()

#This function will handle the user input ,sending him to the desired menu, while also handling errors and taking care that the program runs continuously
def main_menu():
    while True:
        main_menu_input = input()
        match main_menu_input:
            case "A" | "a":
                case(option_a, submenu_a, A_list)
            case "B" | "b":
                case(option_b, submenu_b, B_list)
            case "C" | "c":
                case(option_c, submenu_c, C_list)
            case "X" | "x":
                case_x()
            case _:
                print(invalid_option_mainmenu)

main_menu()
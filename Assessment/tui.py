"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

mmenu_list = ["[A] View Data", "[B] Visualise Data", "[C] Export Data", "[X] Exit"]
#mmenu_valid_options = ["A", "B", "C", "X"]
A_list = ["[A] View Reviews by Park",  "[B] Number of Reviews by Park and Reviewer Location", "[C] Average Score per year by Park", "[D] Average Score per Park by Reviewer Location"]
B_list = ["[A] Most Reviewed Park", "[B] Average Scores", "[C] Park Ranking by Nationality", "[D] Most Popular Month by Park"]

#Displaying the main menu
def mainmenu():
    print("Please enter the data that corresponds with your desired menu choice:")
    for m in mmenu_list:
        print(m)
    main_menu_input = input()

    if main_menu_input == "A":
        print("You have chosen the option A - View Data\n")
        print(f"Please enter one of the following options:\n", end="")

        for a in A_list:
            print(a)

    elif main_menu_input == "B":
        print("You have chosen the option B - Visualise data\n" + "Please enter one of the following options:\n", end="")
        for b in B_list:
            print(b)

    elif main_menu_input == "C":
        print("You have chosen the option C - Export Data")

    elif main_menu_input == "X":
        print("You have chosen the option X - Exit")

    else:
        print("The menu that you have selected doesn't exist. Please select one of the options above.")
mainmenu()
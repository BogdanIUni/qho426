"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
#import csv

#Title of the Program
print("""
--------------------------
Disneyland Review Analyser
--------------------------
""")

#Lists
mmenu_list = ["[A] View Data", "[B] Visualise Data", "[C] Export Data", "[X] Exit"]
#mmenu_valid_options = ["A", "B", "C", "X"]
A_list = ["[A] View Reviews by Park",  "[B] Number of Reviews by Park and Reviewer Location", "[C] Average Score per year by Park", "[D] Average Score per Park by Reviewer Location"]
B_list = ["[A] Most Reviewed Park", "[B] Average Scores", "[C] Park Ranking by Nationality", "[D] Most Popular Month by Park"]

#Displaying the main menu
print("Please enter the data that corresponds with your desired menu choice:")
for m in mmenu_list:
    print(m)
main_menu = input()

#Menu Option A
if main_menu == "A":
    print("You have chosen the option A - View Data\n")

    print(f"Please enter one of the following options:\n", end="")

    for a in A_list:
        print(a)

#Menu Option B
elif main_menu == "B":
    print("You have chosen the option B - Visualise data\n" + "Please enter one of the following options:\n", end="")
    for b in B_list:
        print(b)

#Menu Option C
elif main_menu == "C":
    print("You have chosen the option C - Export Data")
#Menu Option X
elif main_menu == "X":
    print("You have chosen the option X - Exit")
#Wrong input
else:
    print("The menu that you have selected doesn't exist. Please select one of the options above.")



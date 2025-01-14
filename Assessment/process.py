"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
from tui import *

def reading_data():
    count = 0

    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        #headings = next(csv_reader)
        next(csv_reader)
        for row in csv_reader:
            count += 1
        print("\n\nFinished reading the dataset.")
        print(f"There are {count} rows in the dataset.")

def specific_park():
    with open("data/disneyland_reviews.csv") as file:

        # Can do list(file) to read the file
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

        park_name = input("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]\n")

        result = []
        valid_park = []

        #Workflow
        for p in rows:
            valid_park.append(p[4])

        if park_name in valid_park:
            for row in rows:
                if row[4] == park_name:
                    result.append(row)
            print(*result, sep= "\n")
            print("\nPress X to return to the Main Menu or Any Other Key to return to the previous menu")
        else:
            print("This location is not on the list")

def park_and_loc():
    with open("data/disneyland_reviews.csv") as file:

        csv_reader = csv.reader(file)
        rows = list(csv_reader)

        #Takes user input
        park_name = input("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]\n")
        loc = input("From what location should the reviewer be ?\n")

        # New list that will
        result = []

        #The list of parks and locations that are filled with the content inside the Excel file by the loops
        valid_location = []
        valid_park = []

        #Workflow
        for l in rows:
            valid_location.append(l[3])
        for p in rows:
            valid_park.append(p[4])

        if park_name in valid_park and loc in valid_location:
            for row in rows:
                if row[4] == park_name and row[3] == loc:
                    result.append(row)
            print(*result, sep= "\n")
            print("\nPress X to return to the Main Menu or Any Other Key to return to the previous menu")
        elif park_name not in valid_park:
            print(f"{park_name} is not a valid park.")
        elif loc not in valid_location:
            print(f"{loc} is not a valid location")

def park_and_year():
    with open("data/disneyland_reviews.csv") as file:

        csv_reader = csv.reader(file)
        rows = list(csv_reader)

        #Takes user input
        park_name = input("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]\n")
        year = input("Please enter a year:\n")

        # New list that will
        result = []

        #The list of parks and locations that are filled with the content inside the Excel file by the loops
        year_and_month = []
        valid_park = []

        #Workflow
        for y in rows:
            year_and_month.append(y[2])
        for p in rows:
            valid_park.append(p[4])

        if park_name in valid_park and year in year_and_month:
            for row in rows:
                if row[4] == park_name and row[2] == year:
                    result.append(row[1])
            for i in range(len(result)):
                result[i] = int(result[i])

            print(f"The average rating for the year {year} in the park {park_name} is {sum(result)/len(result)}")
            print("\nPress X to return to the Main Menu or Any Other Key to return to the previous menu")
        else:
            print("This location or year is not on the list")

def avg_score():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

    main_dictionary = {}
    sub_dict = {}
    result = {}

    for row in rows:
        if row[4] not in main_dictionary:
            main_dictionary[row[4]] = {}
        if row[3] not in main_dictionary[row[4]]:
            main_dictionary[row[4]][row[3]] = []

        main_dictionary[row[4]][row[3]].append(row[1])

    for row[4], countries in main_dictionary.items():
        for row[3], score in countries.items():
            for i in range(len(score)):
                score[i] = int(score[i])
            avg_score = sum(score) / len(score)
            sub_dict[row[4], row[3]] = avg_score
            top = dict(sorted(sub_dict.items(), key=lambda x: x[1], reverse=True))
    for i in list(top.items()):
        result[i[0]] = i[1]
    print(sub_dict)
avg_score()

def export():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

    review_loc = {""}
    california_loc = {""}
    hongkong_loc = {""}

    #paris_loc.remove("")
    #california_loc.remove("")
    #hongkong_loc.remove("")

    score_paris = []
    score_california = []
    score_hongkong = []

    count_paris = 0
    positive_paris = 0
    count_cali = 0
    positive_cali = 0
    count_hongkong = 0
    positive_hongkong = 0

    for i in rows:
        if i[4] == "Disneyland_Paris":
            score_paris.append(i[1])
            count_paris += 1
            if int(i[1]) >= 3:
                positive_paris += 1

        elif i[4] == "Disneyland_California":
            score_california.append(i[1])
            count_cali += 1
            if int(i[1]) >= 3:
                positive_cali += 1
        elif i[4] == "Disneyland_HongKong":
            score_hongkong.append(i[1])
            count_hongkong += 1
            if int(i[1]) >= 3:
                positive_hongkong += 1

    for p in range(len(score_paris)):
        score_paris[p] = int(score_paris[p])
    for c in range(len(score_california)):
        score_california[c] = int(score_california[c])
    for h in range(len(score_hongkong)):
        score_hongkong[h] = int(score_hongkong[h])

    print(review_loc)

#export()
#avg_score()
#park_and_year()
#park_and_loc()
#specific_park()
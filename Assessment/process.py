"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
import tui

#Variable used in the export function
info = ""

def reading_data():
    count = 0

    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for _ in csv_reader:
            count += 1
        print("\n\nFinished reading the dataset.")
        print(f"There are {count} rows in the dataset.")

def specific_park():
    with open("data/disneyland_reviews.csv") as file:

        # Reading the csv file after opening it and creating a variable that reads the csv file as a list
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

        #Takes user input
        park_name = input("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]\n")

        #Lists that hold the values appended from the csv file
        result = []
        valid_park = []

        #Workflow
        for parks in rows:
            valid_park.append(parks[4])

        if park_name in valid_park:
            for row in rows:
                if row[4] == park_name:
                    result.append(row)
            print(*result, sep= "\n")
            print(tui.end_msg)
            input()
        else:
            print(tui.wrong_location)
            specific_park()

def park_and_loc():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

        #Takes user input
        park_name = input("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]\n")
        loc = input("From what location should the reviewer be ?\n")

        # New list that will hold the final results
        result = []

        #The list of parks and locations that are filled with the content inside the Excel file by the loops
        valid_location = []
        valid_park = []

        #Workflow
        for l in rows:
            valid_location.append(l[3])
            valid_park.append(l[4])

        if park_name in valid_park and loc in valid_location:
            for row in rows:
                if row[4] == park_name and row[3] == loc:
                    result.append(row)
            print(*result, sep= "\n")
            print(tui.end_msg)
            input()
        elif park_name not in valid_park:
            print(tui.wrong_location)
            park_and_loc()
        elif loc not in valid_location:
            print(tui.wrong_location)
            park_and_loc()

def park_and_year():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        #Empty lists that will be filled with the content inside the Excel file
        year_and_month = []
        valid_park = []

        years = []
        months = []

        result = []

        #Appending the 2 empty lists with the data from the Excel file
        for y in rows:
            valid_park.append(y[4])
            year_and_month.append(y[2])

        for dates in year_and_month:
            if dates != 'missing':
                y ,m = dates.split('-')
            years.append(y)
            months.append(m)

        #Takes user input and asks what to input
        park_name = input("Which park do you wish to see the reviews for? [ Disneyland_HongKong, Disneyland_California,  Disneyland_Paris ]\n")
        year = input("Please enter a year:\n")

        if park_name in valid_park and year in years:
            for row in rows:
                if row[4] == park_name and row[2].startswith(str(year)):
                    result.append(int(row[1]))

            print(f"The average rating for the year {year} in the park {park_name} is {sum(result)/len(result)}")
            print(tui.end_msg)
            input()
        elif park_name not in valid_park:
            print(tui.wrong_location)
            park_and_year()
        elif year not in years:
            print("This year is not on the list")
            park_and_year()

def avg_score():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        dict1 = {}
        sub_dict = {}

        for row in rows:
            if row[4] not in dict1:
                dict1[row[4]] = {}
            if row[3] not in dict1[row[4]]:
                dict1[row[4]][row[3]] = []

            dict1[row[4]][row[3]].append(row[1])

        for row[4], countries in dict1.items():
            for row[3], score in countries.items():
                for i in range(len(score)):
                    score[i] = int(score[i])
                average_score = sum(score) / len(score)
                sub_dict[row[4], row[3]] = average_score

        print(sub_dict)
        input()

def export():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

    global info

    paris_loc_num = []
    california_loc_num = []
    hongkong_loc_num = []

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
            if int(i[1]) > 3:
                positive_paris += 1
            elif i[3] not in paris_loc_num:
                paris_loc_num.append(i[3])
        elif i[4] == "Disneyland_California":
            score_california.append(i[1])
            count_cali += 1
            if int(i[1]) >= 3:
                positive_cali += 1
            elif i[3] not in california_loc_num:
                california_loc_num.append(i[3])
        elif i[4] == "Disneyland_HongKong":
            score_hongkong.append(i[1])
            count_hongkong += 1
            if int(i[1]) >= 3:
                positive_hongkong += 1
            elif i[3] not in hongkong_loc_num:
                hongkong_loc_num.append(i[3])

    for p in range(len(score_paris)):
        score_paris[p] = int(score_paris[p])
    for c in range(len(score_california)):
        score_california[c] = int(score_california[c])
    for h in range(len(score_hongkong)):
        score_hongkong[h] = int(score_hongkong[h])

    avg_score_paris = sum(score_paris)/len(score_paris)
    avg_score_cali = sum(score_california)/len(score_california)
    avg_score_hongkong = sum(score_hongkong)/len(score_hongkong)

    info = (f"""
        Disneyland_Paris:
            - Number of reviews: {count_paris}
            - Number of positive reviews: {positive_paris}
            - Average score: {avg_score_paris}
            - Number of countries that reviewed the park: {len(paris_loc_num)}

        Disneyland_California:
            - Number of reviews: {count_cali}
            - Number of positive reviews: {positive_cali}
            - Average score: {avg_score_cali}
            - Number of countries that reviewed the park: {len(california_loc_num)}

        Disneyland_Paris:
            - Number of reviews: {count_hongkong}
            - Number of positive reviews: {positive_hongkong}
            - Average score: {avg_score_hongkong}
            - Number of countries that reviewed the park: {len(hongkong_loc_num)}
        """)

def export_final(extension, count=0):
    export()

    try:
        with open(f"data/exported_data({count}).{extension}", "x") as data:
            data.write(info)
    except FileExistsError:
        return export_final(extension, count + 1)

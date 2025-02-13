"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt
import csv
import tui

def mostreviewed_park():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        paris_count = 0
        california_count = 0
        hongkong_count = 0

        #Looping through the elements of the Excel File while checking for specific conditions and appending data in their respective list if those conditions are met
        for row in rows:
            if row[4] == "Disneyland_Paris":
                paris_count += 1
            elif row[4] == "Disneyland_California":
                california_count += 1
            elif row[4] == "Disneyland_HongKong":
                hongkong_count += 1

        #Defining the "pie slices size" and labels
        y = [paris_count, california_count, hongkong_count]
        parks = [f"Disneyland_Paris\n{paris_count}", f"Disneyland_California\n{california_count}", f"Disneyland_HongKong\n{hongkong_count}"]

        # Using matplotlib to display the pie chart
        plt.title("Number of Reviews Per Park")
        plt.pie(y, labels=parks)
        plt.show()

def scores_per_park():
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        #Empty lists that will be appended later on
        paris_scores = []
        california_scores = []
        hongkong_scores = []

        #Looping through the elements of the Excel File while checking for specific conditions and appending data in their respective list if those conditions are met
        for row in rows:
            if row[4] == "Disneyland_Paris":
                paris_scores.append(row[1])
            elif row[4] == "Disneyland_California":
                california_scores.append(row[1])
            elif row[4] == "Disneyland_HongKong":
                hongkong_scores.append(row[1])

        #Converting the elements in the score lists into integers to be able to calculate the average score
        for a in range(len(paris_scores)):
            paris_scores[a] = int(paris_scores[a])
        for b in range(len(california_scores)):
            california_scores[b] = int(california_scores[b])
        for c in range(len(hongkong_scores)):
            hongkong_scores[c] = int(hongkong_scores[c])

        avg_paris = int(sum(paris_scores)/len(paris_scores))
        avg_california = int(sum(california_scores)/len(california_scores))
        avg_hongkong = int(sum(hongkong_scores)/len(hongkong_scores))

        #Defining the x and y coordinates
        x = ["Disneyland_Paris", "Disneyland_California", "Disneyland_HongKong"]
        y = [avg_paris, avg_california, avg_hongkong]

        #Using matplotlib to display the bar chart
        plt.title("Average Score Per Park")
        plt.bar(x,y)
        plt.show()

def top10_per_park():
    #Reading the file and skipping headers
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        #Asks the user for input and takes the user input
        park_name = input("Which park would you like to see data on?(Disneyland_Paris, Disneyland_California, Disneyland_HongKong)\n")

        #Empty directories that will be filled with data from the Excel sheet
        main_dictionary = {}
        sub_dict = {}
        top10 = {}

        for row in rows:
            if row[4] not in main_dictionary:
                main_dictionary[row[4]] = {}
            if row[3] not in main_dictionary[row[4]]:
                main_dictionary[row[4]][row[3]] = []

            main_dictionary[row[4]][row[3]].append(row[1])

        if park_name == "Disneyland_Paris" and row[4] == "Disneyland_Paris":
            for row[4],countries in main_dictionary.items():
                    for row[3],score in countries.items():
                        for i in range(len(score)):
                            score[i] = int(score[i])
                        avg_score = sum(score)/len(score)
                        sub_dict[row[3]] = avg_score
                        top = dict(sorted(sub_dict.items(), key=lambda d: d[1], reverse=True))
            for i in list(top.items())[0:10]:
                top10[i[0]] = i[1]

            x = top10.keys()
            y = top10.values()

            plt.title("Top10 Locations per average location review for Disneyland_Paris")

        elif park_name == "Disneyland_California":
            for row[4],countries in main_dictionary.items():
                if row[4] == "Disneyland_California":
                    for row[3],score in countries.items():
                        for i in range(len(score)):
                            score[i] = int(score[i])
                        avg_score = sum(score)/len(score)
                        sub_dict[row[3]] = avg_score
                        top = dict(sorted(sub_dict.items(), key=lambda d: d[1], reverse=True))
            for i in list(top.items())[0:10]:
                top10[i[0]] = i[1]

            x = top10.keys()
            y = top10.values()

            plt.title("Top10 Locations per average location review for Disneyland_California")

        elif park_name == "Disneyland_HongKong":
            for row[4],countries in main_dictionary.items():
               if row[4] == "Disneyland_HongKong":
                   for row[3], score in countries.items():
                       for i in range(len(score)):
                           score[i] = int(score[i])
                       avg_score = sum(score) / len(score)
                       sub_dict[row[3]] = avg_score
                       top = dict(sorted(sub_dict.items(), key=lambda d: d[1], reverse=True))
               for i in list(top.items())[0:10]:
                   top10[i[0]] = i[1]

               x = top10.keys()
               y = top10.values()
            plt.title("Top10 Locations per average location review for Disneyland_HongKong")

        # Creating the actual bar chart using matplotlib and getting the average scores
        # Text rotation needed for better readability

        plt.bar(x, y)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def rank_by_month():
    #Reading the file and skipping headers
    with open("data/disneyland_reviews.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        #Empty lists that will be filled with the content inside the Excel file
        valid_park = []

        january = []
        february = []
        march = []
        april = []
        may = []
        june = []
        july = []
        august = []
        september = []
        october = []
        november = []
        december = []

        for row in rows:
            valid_park.append(row[4])

        #Asks the user for input and takes the user input
        park_name = input("Which park would you like to see data on?(Disneyland_Paris, Disneyland_California, Disneyland_HongKong)\n")

        #First we see if the user's input matches with any valid locations , otherwise it will return an error message and the option will ask again for a valid input
        #Then for every row where the Branch Name column matches with the user's input we also check to for the characters that the year-month column end in so we can put the review score into their respective lists as integers
        if park_name in valid_park:
            for row in rows:
                if row[4] == park_name and row[2].endswith('-1'):
                    january.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-2'):
                    february.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-3'):
                    march.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-4'):
                    april.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-5'):
                    may.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-6'):
                    june.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-7'):
                    july.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-8'):
                    august.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-9'):
                    september.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-10'):
                    october.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-11'):
                    november.append(int(row[1]))
                if row[4] == park_name and row[2].endswith('-12'):
                    december.append(int(row[1]))

            #Creating the x and y variables with their intended values
            #Text rotation needed for better readability

            x = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            y = [float(sum(january)/len(january)), float(sum(february)/len(february)), float(sum(march)/len(march)), float(sum(april)/len(april)), float(sum(may)/len(may)), float(sum(june)/len(june)), float(sum(july)/len(july)), float(sum(august)/len(august)), float(sum(september)/len(september)), float(sum(october)/len(october)), float(sum(november)/len(november)), float(sum(december)/len(december))]

        else:
            print(tui.wrong_location)
            rank_by_month()

        #Creating the actual bar chart using matplotlib
        #Text rotation needed for better readability

        plt.title("Average score per month")
        plt.bar(x, y)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
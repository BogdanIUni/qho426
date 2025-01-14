"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
from typing import Dict

import matplotlib.pyplot as plt
import csv

def mostreviewed_park():
    with open("data/disneyland_reviews.csv") as file:

        # Can do list(file) to read the file
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        paris_count = 0
        california_count = 0
        hongkong_count = 0

        for row in rows:
            if row[4] == "Disneyland_Paris":
                paris_count += 1
            elif row[4] == "Disneyland_California":
                california_count += 1
            elif row[4] == "Disneyland_HongKong":
                hongkong_count += 1

        y = [paris_count, california_count, hongkong_count]
        parks = [f"Disneyland_Paris\n{paris_count}", f"Disneyland_California\n{california_count}", f"Disneyland_HongKong\n{hongkong_count}"]

        plt.title("Number of Reviews Per Park")
        plt.pie(y, labels=parks)
        plt.show()

def scores_per_park():
    with open("data/disneyland_reviews.csv") as file:

        # Can do list(file) to read the file
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        Paris_scores = []
        California_scores = []
        Hongkong_scores = []

        for row in rows:
            if row[4] == "Disneyland_Paris":
                Paris_scores.append(row[1])
            elif row[4] == "Disneyland_California":
                California_scores.append(row[1])
            elif row[4] == "Disneyland_HongKong":
                Hongkong_scores.append(row[1])
        for p in range(len(Paris_scores)):
            Paris_scores[p] = int(Paris_scores[p])
        for c in range(len(California_scores)):
            California_scores[c] = int(California_scores[c])
        for h in range(len(Hongkong_scores)):
            Hongkong_scores[h] = int(Hongkong_scores[h])

        avg_Paris = int(sum(Paris_scores)/len(Paris_scores))
        avg_California = int(sum(California_scores)/len(California_scores))
        avg_HongKong = int(sum(Hongkong_scores)/len(Hongkong_scores))

        x = ["Disneyland_Paris", "Disneyland_California", "Disneyland_HongKong"]
        y = [avg_Paris, avg_California, avg_HongKong]

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
                        top = dict(sorted(sub_dict.items(), key=lambda x: x[1], reverse=True))
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
                        top = dict(sorted(sub_dict.items(), key=lambda x: x[1], reverse=True))
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
                       top = dict(sorted(sub_dict.items(), key=lambda x: x[1], reverse=True))
               for i in list(top.items())[0:10]:
                   top10[i[0]] = i[1]

               x = top10.keys()
               y = top10.values()

            plt.title("Top10 Locations per average location review for Disneyland_HongKong")

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

        #Asks the user for input and takes the user input
        park_name = input("Which park would you like to see data on?(Disneyland_Paris, Disneyland_California, Disneyland_HongKong)\n")


"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt
import csv

def mostreviewed_park():
    with open("data/disneyland_reviews.csv") as file:
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
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = list(csv_reader)

        paris_scores = []
        california_scores = []
        hongkong_scores = []

        for row in rows:
            if row[4] == "Disneyland_Paris":
                paris_scores.append(row[1])
            elif row[4] == "Disneyland_California":
                california_scores.append(row[1])
            elif row[4] == "Disneyland_HongKong":
                hongkong_scores.append(row[1])

        for a in range(len(paris_scores)):
            paris_scores[a] = int(paris_scores[a])
        for b in range(len(california_scores)):
            california_scores[b] = int(california_scores[b])
        for c in range(len(hongkong_scores)):
            hongkong_scores[c] = int(hongkong_scores[c])

        avg_paris = int(sum(paris_scores)/len(paris_scores))
        avg_california = int(sum(california_scores)/len(california_scores))
        avg_hongkong = int(sum(hongkong_scores)/len(hongkong_scores))

        x = ["Disneyland_Paris", "Disneyland_California", "Disneyland_HongKong"]
        y = [avg_paris, avg_california, avg_hongkong]

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


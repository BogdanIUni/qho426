import csv
from tokenize import group

records = []
headings = []

def load_data(file_path):
    global records, headings

    print("Loading data...")

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for row in csv_reader:
            records.append(row)

def display_menu():
    print("""
        Please Select one of the following options:
        [1] Display the names of all passengers
        [2] Display the number of passengers that survived
        [3] Display the number of passengers per gender
        [4] Display the number of passengers per age group
        
        Please select one of the following options: 1-4
    """)

    user_input = int(input())
    return user_input

def display_passengers_names():

    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)

def display_num_of_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived = num_survived + 1

    print(f"{num_survived} passengers survived.")

#display_num_of_survivors()

def display_passengers_per_gender():
    #You can also write it as females = males = 0 ,because both have the value 0
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender.lower() == 'female':
            females = females + 1
        elif gender.lower() == 'male':
            males =females + 1

    print(f"Females:{females}, Males:{males}")

def display_passengers_per_age_group():
    children = adults = elderly = 0
    for record in records:
        age = record[5]
        if age and age.isdigit():
            age = int(age)
            if age < 18:
                children = children + 1
            elif age > 65:
                elderly =elderly + 1
            else:
                adults = adults + 1

    print(f"Children:{children},Adults:{adults}, Elderly:{elderly}")

def run():
    global records
    file_path = "titanic.csv"
    load_data(file_path)

    print(f"Successfully loaded {len(records)} records.")
    print("Done!")

    selected_option = display_menu()

    print(f"You have selected option: {selected_option}")

    if selected_option == 1:
        display_passengers_names()
    elif selected_option == 2:
        display_num_of_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    else:
        print("Error! Option not recognised!")

run()
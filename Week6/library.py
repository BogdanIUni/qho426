def display_chars(file_path, number_of_characters):
    with open(file_path) as file:
        data = file.read(number_of_characters)
        print("The first 5 characters are:")
        print(data)

def display_line(file_path):
    with open(file_path) as file:
        data = file.readline()
        print("\nThe first line is:")
        print(data)

def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print("\nThe full text is:")
        print(data)

def run_task2():
    file_path = "library.txt"
    display_chars(file_path, number_of_characters=5)
    display_line(file_path)
    display_text(file_path)

run_task2()

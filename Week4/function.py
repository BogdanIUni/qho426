def add():
    count = 0
    print("Please enter a number:")
    user_number = int(input())
    count += user_number
    print("Please enter another number:")
    user_number2 = int(input())
    count = user_number + user_number2
    print(f"Your number is {count}")

add()
print("Please enter the first number")

number1 = int(input())

print("Please enter the second number")

number2 = int(input())

if number1 < number2:
    print(f"The first number is the smallest!")
elif number2 < number1:
    print(f"The second number is the smallest!")
else:
    print(f"The numbers are equal!")
print("Please enter your name")
name = input()
print(f"your name is {name}")


print("Please enter your age")
age = int(input())
print(f"your age is {age}")

print("Please enter your weight")
weight = float(input())
print(f"your weight is {weight}")

print("Please enter your height")
height = float(input())
print(f"your height is {height}")

bmi = weight/(height**2)

print(f"Your BMI is {bmi}")
print("How many numbers should I sum?")
sum = int(input())

number = 0
total = 0

while number < sum:
    number += 1
    print(f"Please enter number {number} out of {sum}")
    new_number = int(input())
    total = total + new_number

print(f"The answer is {total}")
print("Program Started!")
print("Please enter a standard character:")
letter = input()
count = 0

for i in range(0, len(letter), 1):
    count += 1
    if count == 1:
        value = ord(letter)
        print(f"The ASCII code for {letter} is {value}")
    elif count > 1:
        print("The input submitted is not a single character")

print("Program Ended!")

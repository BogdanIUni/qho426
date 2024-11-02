print("How many rows should I have?")
row = int(input())
print("How many columns should I have?")
columns = int(input())

print("Here I go:")

for i in range(row):
    for l in range(columns):
        print(f":-)", end="")
    print()
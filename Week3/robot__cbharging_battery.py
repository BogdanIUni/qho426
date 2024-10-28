print("How many bars should be charged?")
bars = int(input())

bars_number = 0

while bars_number <= bars:
    print(f"Charging: {"█ " * bars_number}")
    bars_number += 1

print("The battery has fully charged!")
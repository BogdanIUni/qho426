print("Enter a sequence consisting of dashes and two markers. (e.g. X---X)")
sequence = input()

print("Enter your character used in the sequence above")
marker = input()
dashes = "-"

for i in sequence:
    for count in range(sequence.count(dashes)):
        print(f"The distance between the markers is total")

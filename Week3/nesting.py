print("Enter a sequence consisting of dashes and two markers. (e.g. X---X)")
sequence = input()

print("Enter your character used in the sequence above")
marker = input()

dashes = "-"

for i in sequence:
    count = sequence.count(marker)

    if i == marker:
        print(f"The distance between the markers is {sequence.count(dashes, len(marker))}")
        break

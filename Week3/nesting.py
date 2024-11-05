print("Enter a sequence consisting of dashes and two markers. (e.g. X---X)")
sequence = input()

print("Enter your character used in the sequence above")
marker = input()

mposition1 = -1
mposition2 = -1

for i in range (0, len(sequence), 1):
    letter = sequence[i]

    if letter == marker:
        if mposition1 == -1:
            mposition1 = i
        else:
            mposition2 = i

print(f"The distance between the markers is {mposition2 - mposition1 - 1}.")

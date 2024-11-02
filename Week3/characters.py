print("What word do you see?")
word = input()

print(f"Displaying index positions...\n", end="")

for i in range(0, len(word), 1):
    print(f"Index {i}: {word[i]}")

print("Done!")
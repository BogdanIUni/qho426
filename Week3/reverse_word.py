print("What phrase do you want to see in reverse?")
phrase = input()

print("Reversing...")
print("The phrase is ", end= "")

for i in range(len(phrase)-1, -1, -1):
    print(phrase[i], end= "")

print("\nDone")

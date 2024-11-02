print("How far are we from the target?")
target = int(input())

for i in range(target, 0, -1):
    print(f"{i} Steps are remaining")

print("\nTarget achieved!")
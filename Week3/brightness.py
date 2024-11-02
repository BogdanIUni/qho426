print("What level of brightness is required?")
brightness = int(input())

for i in range(2, brightness+1, 2):
    print(f"Brigthness levels: {"*" * i}")

print("Complete!")
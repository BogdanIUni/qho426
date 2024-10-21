print("Towards which direction should I go (up, down, right, left)")

direction = input()

if direction == "up":
    print("I am moving in an upright direction")
elif direction == "down":
    print("I am moving in an downright direction")
elif direction == "right":
    print("I am moving in the right direction")
elif direction == "left":
    print("I am moving in the left direction")
else:
    print("You entered a wrong input")

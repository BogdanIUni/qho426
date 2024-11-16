def directions():
    steps = ["Move Forward", "Move Backwards", "Turn Left", "Turn Right"]
    return steps

def menu():
    print("Please enter a direction:")
    direc = directions()
    for i in range(0 , len(direc)):
        print(f"{i}: {direc[i]}")

def task3():
    menu()

task3()
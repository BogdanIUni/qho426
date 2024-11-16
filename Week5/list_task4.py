def directions():
    steps = ["Move Forward", "Move Backwards", "Turn Left", "Turn Right"]
    return steps

def menu_and_input():
    print("Please enter a direction:")
    direc = directions()
    for i in range(0 , len(direc)):
        print(f"{i}: {direc[i]}")
    direction = int(input())
    return direc[direction]

def run_task4():
    route = []
    print("Working out escape route..")
    for i in range(0,5):
        route.append(menu_and_input())
    print(f"Escape route is : {route}")

run_task4()
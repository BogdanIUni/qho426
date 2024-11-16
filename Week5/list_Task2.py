def movement():
    path = ["Move Forward",10,"Move Backwards",5,"Turn Left",3,"Turn Right",1]
    return path

def run_task2():
    print("Moving...")
    direction = movement()
    print(f"{direction[0]} for {direction[1]} steps")
    print(f"{direction[2]} for {direction[3]} steps")
    print(f"{direction[4]} for {direction[5]} steps")
    print(f"{direction[6]} for {direction[7]} steps")

    # Alternative method

    #for items in range(0 , len(direction), 2):
        #print(f"{direction[items]} for {direction[items+1]} steps")

run_task2()
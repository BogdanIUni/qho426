print("How many obstacles should I avoid?")
obstacles = int(input())

nr_obstacles = 0

while nr_obstacles <= obstacles:
    print("Avoiding...", end="")
    nr_obstacles += 1
    print(f"...Done! {nr_obstacles} obstacles avoided!")
else:
    print("All the obstacles have been avoided.")
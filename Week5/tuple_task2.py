def likelyhood_min_max():
    likelyhoods = (50, 38, 27, 99 ,4)
    return min(likelyhoods), max(likelyhoods)

def run_task2():
    value = likelyhood_min_max()
    print(f"Minimum likelihood of falling: {min(value)}%") # or can use index range with value[0/1]
    print(f"Maximum likelihood of falling: {max(value)}%")

run_task2()
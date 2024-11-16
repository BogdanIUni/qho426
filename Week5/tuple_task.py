def likelyhood():
    likelyhoods = (50, 38, 27, 99 ,4)
    return min(likelyhoods)

def run_task1():
    value = likelyhood()
    print(f"Minimum likelihood of falling: {value}%")

run_task1()
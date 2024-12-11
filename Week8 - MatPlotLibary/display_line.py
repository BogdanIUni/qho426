import matplotlib.pyplot as plt

def displayline(x, y):
    plt.plot(x, y)
    plt.title("First line graph - task 1")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.grid()
    plt.show()

def run_task1():
    x_values = [1,2,3,4,5]
    y_value = [1,4,9, 16, 25]

    displayline(x_values, y_value)

run_task1()
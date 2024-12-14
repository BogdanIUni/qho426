import matplotlib.pyplot as plt
import random

def data():
    paths = {}
    line_style = input("What type of line would you like (:, -- or -):")
    color = input("What color would you like (r, g ,b):")
    marker = input("What marker would you like (o, s or ^):")

    paths["Line Style"] = line_style
    paths["Color"] = color
    paths["Marker"] = marker

    return paths

def generate():
    userinput = int(input("How many lines would you like to display?"))

    for i in range(userinput):
        values = data()
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1,10), 5)
        format = f"{values['Line Style']}{values['Color']}{values['Marker']}"
        plt.plot(x, y, format)

    plt.show()

def run():
    print("Running...")
    generate()
    print("Done!")

run()
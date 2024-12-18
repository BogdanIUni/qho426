class Robot:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    def display(self):
        print(f"I am {self.name} and my age is {self.age}")

if __name__ == "__main__":
    robot = Robot()
    robot.display()

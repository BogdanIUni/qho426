class Robot:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    #Method 1
    #def display(self):
        #print(f"I am {self.name} and my age is {self.age}")

    #Method 2
    #def __repr__(self):
        #return f'robot(name={self.name}, age={self.age})'

    #Method 3
    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount if Robot.MAX_ENERGY <= 100 else print("Error!Max Energy exceeded!")

    def move(self, distance):
        self.energy -= distance if Robot.MAX_ENERGY >= 0 else print("Error!Max Energy below 0!")

if __name__ == "__main__":
    robot = Robot()
    robot.grow()
    robot.eat(5)
    print(robot, robot.energy)

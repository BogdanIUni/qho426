class Human:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    #Method 1
    #def display(self):
        #print(f"I am {self.name} and my age is {self.age}")

    #Method 2
    #def __repr__(self):
        #return f'Human(name={self.name}, age={self.age})'

    #Method 3
    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

if(__name__ == "__main__"):
    human = Human()
    print(human)
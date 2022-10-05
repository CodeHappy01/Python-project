from abc import ABC, abstractmethod

class Organism(ABC):
    @abstractmethod #Abstract Method
    def move(self):
        pass

class Human(Organism):

    def move(self):
        print("Human: I can walk and run!")

class Bird(Organism):

    def move(self):
        print("Bird: I can fly!")

# Driver code
H = Human()
H.move()

B = Bird()
B.move()



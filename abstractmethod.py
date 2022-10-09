from abc import ABC, abstractmethod

class Organism(ABC):
    def Origin(self):
        print("Origin: Earth")
    @abstractmethod #Abstract Method
    def move(self):
        pass

class Human(Organism):

    def move(self):
        print("\nHuman: I can walk and run!")

class Bird(Organism):

    def move(self):
        print("\nBird: I can fly!")

# Driver code
O = Organism()
O.Origin()

H = Human()
H.move()

B = Bird()
B.move()



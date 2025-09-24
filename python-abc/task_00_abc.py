#!/usr/bin/python3

# Import ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod


# Define the abstract base class Animal
class Animal(ABC):
    # Declare an abstract method named sound
    @abstractmethod
    def sound(self):
        pass


# Define the Dog class that inherits from Animal
class Dog(Animal):

    # Implement the sound method for Dog
    def sound(self):
        return "Bark"


# Define the Cat class that inherits from Animal
class Cat(Animal):
    # Implement the sound method for Cat
    def sound(self):
        return "Meow"

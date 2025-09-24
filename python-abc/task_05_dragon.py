#!/usr/bin/python3


# Define SwimMixin with swim functionality
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Define FlyMixin with fly functionality
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Define Dragon class that inherits from both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

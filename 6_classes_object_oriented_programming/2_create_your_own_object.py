"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self, make, model = "550i"):
        self.make = make
        self.model = model

c1 = Car('bmw')
print(c1.make)
print(c1.model)

c2 = Car('Benz')
print(c2.make)
print(c2.model)
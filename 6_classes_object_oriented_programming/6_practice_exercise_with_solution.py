class Fruit(object):

    def __init__(self):
        print("You just created fruit")

    def nutrition(self):
        print("nutrition...")

    def fruit_shape(self):
        print("fruit shape")

class Apple(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("init apple")

    def nutrition(self):
        print("nutrition apple")

    def color(self):
        print("color apple")

a = Fruit()
a.nutrition()
a.fruit_shape()

b = Apple()
b.nutrition()
b.color()

class People:
    def __init__(self, object, print):
        self.object = object
        self.print = print

    def ShowInfo(self):
        print("this:", self.object, "say:", self.print)

class Brains(People):
     def __init__(self, object, print):
         super().__init__(object, print)

class Heart(People):
    def __init__(self, object, print):
        super().__init__(object, print)

class Legs(People):
    def __init__(self, object, print):
        super().__init__(object, print)

p = People("People,", "my name Jack")
b = Brains("Brains,", "i think")
h = Heart("Heart,", "i give a person the opportunity to live")
l = Legs("Legs,", "i go")
p.ShowInfo()
b.ShowInfo()
h.ShowInfo()
l.ShowInfo()

class Figure:

    def __init__(self, color, pi, x, y):
        self.color = color
        self.pi = pi
        self.x = x
        self.y = y

class Rectangular(Figure):
    def ShowInfo(self):
        print("Rectangular ","Color:", self.color, "Pi:", self.pi, "X:", self.x, "Y:", self.y)


rect = Rectangular("red", 3.14, 50, 60)
rect.ShowInfo()




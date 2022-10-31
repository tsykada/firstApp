class Animal():
    def __init__(self, name, ves, breed):
     self.name = name
     self.ves = ves
     self.breed = breed

    def golos(self):
        pass
    def showInfo(self):
        print("name:", self.name, "breed:", self.breed, "ves:", self.ves)
class Dog(Animal):
    def __init__(self, name, ves, breed):
        super().__init__(name, ves, breed)


    def golos(self):
        print("Gav gav")

class Cat(Animal):
    def __init__(self, name, ves, breed):
        super().__init__(name, ves, breed)


    def golos(self):
        print("meow meow")


myCat = Cat("Kerlinh", 5, "Sphinx")
myCat.showInfo()
myCat.golos()

myDog = Dog("Bobik", 20, "Staff")
myDog.showInfo()
myDog.golos()






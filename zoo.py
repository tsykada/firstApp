class Animal:
    def __init__(self, name, breed):
        self.breed = breed
        self.name = name
        self.satiety = 10

    def to_eat(self):
        print("Time to eat")
        self.satiety += 1

class Zoo:
    def __init__(self, name):
        self.satiety = []
        self.name = name
        self.animals = []

    def addAnimal(self, newAnimal):
        self.animals.append(newAnimal)

    def delAnimal(self, delAnimal):
        try:
            self.animals.remove(delAnimal)
        except:
            print("This animal", delAnimal.name, "is not in the zoo", self.name)

    def printAnimals(self):
        if self.animals != []:
            print("Name of the zoo:", self.name)
            for st in self.animals:
                print("Name:", st.name, "Breed:", st.breed)
        else:
            print("No animals in this zoo!")



fox = Animal("jack", "arctic fox")
cat = Animal("kerlin", "sphinx")
dog = Animal("khlor", "spitz")

zoo = Zoo("land")

zoo.addAnimal(dog)
zoo.addAnimal(fox)
zoo.delAnimal(cat)

zoo.printAnimals()




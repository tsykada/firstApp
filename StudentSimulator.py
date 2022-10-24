import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 80
        self.gladness = 50
        self.progress = 10
        self.alive = True
        self.work = False

    def to_study(self):
        print("time to study")
        self.money += 0.5
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time!")
        self.money -= 10
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress <= 1:
            print("Good bay Univer")
            self.alive = False

        elif self.progress <= 2:
            print("time to study")
            self.progress += 2
            self.gladness -= 10

        elif self.gladness <= 20:
            print("Depression...", "rest time")
            self.gladness += 10
            self.money -= 20
            self.progress -= 0.5
        elif self.gladness <= 17:
            print("Depression...")
            self.alive = False
        elif self.money <= 25:
            self.work = True
            print("time to work")
            self.money += 10
        elif self.money >= 25:
            self.work = False
            self.money += 0

    def endOfDay(self):
        print("Gladness", self.gladness)
        print("Progress: ", self.progress)
        print("Money: ", self.money)
        print("Work: ", self.work)

    def live(self, day):
        print("Day", str(day), " of ", self.name, "life")
        num = random.randint(1, 3)
        if num == 1:
            self.to_study()
        elif num == 2:
            self.to_chill()
        elif num == 3:
            self.to_sleep()

        self.endOfDay()
        self.is_alive()


jack = Student("jack")
for day in range(365):
    if jack.alive == False:
        break
    jack.live(day)
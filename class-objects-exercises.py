class Animal:
    def __init__(self, name):
        self.name = name

    def getname(self):
        print(self.name)

    def speak(self):
        print("sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


a1 = Animal("Gloria")
a2 = Dog("Champion")
a3 = Cat("Snowball")

a1.getname()
a1.speak()

a2.getname()
a2.speak()

a3.getname()
a3.speak()

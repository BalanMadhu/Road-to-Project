class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

dog = Dog()
dog.speak()
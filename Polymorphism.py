class Bird:
    def sound(self):
        print("Bird chirps.")

class Cat:
    def sound(self):
        print("Cat meows.")

# Polymorphism in action
for animal in [Bird(), Cat()]:
    animal.sound()
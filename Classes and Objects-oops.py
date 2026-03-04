class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show(self):
        print(f"{self.name} studies {self.course}")

s1 = Student("Madhu", "Python")
s1.show()
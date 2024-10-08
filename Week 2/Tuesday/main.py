class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def promote(self):
        self.grade += 1
        print(f"{self.name} has been promoted to grade {self.grade}")


anna = Student("Anna", 15, 9)

anna.get_info()

anna.promote()

anna.get_info()

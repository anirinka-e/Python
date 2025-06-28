class Student:

    def __init__(self, first_name, second_name, age, course):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.first_name} {self.second_name}, {self.age} лет, учится на курсе {self.course}"

from student import Student
from courseGroup import CourseGroup

student = Student("Иван", "Иванов", 20, "Инженер по тестированию")
classmates1 = Student("Мария", "Сидорова", 21, "Инженер по тестированию")
classmates2 = Student("Петр", "Петров", 22, "Инженер по тестированию")
classmates3 = Student("Павел", "Васин", 19, "Инженер по тестированию")

cours_group = CourseGroup(student, [classmates1, classmates2, classmates3])

print(cours_group)

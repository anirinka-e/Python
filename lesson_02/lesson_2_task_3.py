import math


def square(a):
    return math.ceil(a ** 2)


side = int(input("Введите сторону: "))
result = square(side)
print(f"Площадь квадрата со сторой {side}: {result}")

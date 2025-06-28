# 1)
import math

employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
print(employee_list[1] + ", " + employee_list[-2])


# 2)
def dev_by_three(num):
    if num % 3 == 0:
        return "Да"
    else:
        return "Нет"


number = int(input("Введите число: "))
result_question = dev_by_three(number)
print(f"Делится ли на три {number}? - {result_question}")


# 3)
def min_boxes(num):
    return math.ceil(num / 5)


count = int(input("Введите количество: "))
result_count = min_boxes(count)
print(f"Количество коробок для {count} предметов: {result_count}")


# 4)
def check_divisibility(n):
    for i in range(1, n + 1):
        if i % 4 == 0:
            print(f"Число {i} делится на 2, и на 4")
        elif i % 2 == 0:
            print(f"Число {i} делится на 2, но не на 4")
        else:
            print(i)


num = int(input("Введите число: "))
check_divisibility(num)


# 5)
def quarter_of_year(n):
    if (n > 12) or (n < 1):
        return "Неверный номер месяца"

    quarter = math.ceil(n / 3)
    if quarter == 1:
        return "I квартал"
    elif quarter == 2:
        return "II квартал"
    elif quarter == 3:
        return "III квартал"
    else:
        return "IV квартал"


month = int(input("Введите номер месяца (1-12): "))
result_month = quarter_of_year(month)
print(result_month)

# 6)
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
for i in range(0, len(lst)):
    if (lst[i] > 15) and (lst[i] % 3 == 0):
        print(lst[i])

# 7)
num_list = list(range(25, 0, -5))
print(num_list)

# 8)
var_1 = 50
var_2 = 5

var_1, var_2 = var_2, var_1
print(f"var_1 = {var_1}; var_2 = {var_2}")

def month_to_season(n):
    if 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
    elif 1 <= n <= 2 or n == 12:
        return "Зима"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")

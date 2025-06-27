# При решении задания использовалось правило григорианского календаря (например, 2100 не будет високосным)

def is_year_leap(num):
    if (num % 400 == 0) or ((num % 4 == 0) and (num % 100 != 0)):
        return True
    else:
        return False


year = int(input("Введите год: "))
result = is_year_leap(year)
print(f"год {year}: {result}")

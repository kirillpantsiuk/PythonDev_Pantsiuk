# -*- coding: cp1251 -*-
print("Завдання 1")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Тестовые данные
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

# Тестирование функции
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


print("Завдання 2")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Перевіряємо чи місяць в діапазоні від 1 до 12
    if month < 1 or month > 12:
        return None

    # Кількість днів у кожному місяці
    days_in_months = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Повертаємо кількість днів для даного місяця
    return days_in_months[month - 1]

# Тестові дані
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

# Тестування функції з виведенням у потрібному форматі
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    result = days_in_month(yr, mo)
    
    # Виводимо результат у відповідному форматі
    month_names = ["січень", "лютий", "березень", "квітень", "травень", "червень", 
                   "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"]
    
    if result is not None:
        print(f"{yr}, {month_names[mo-1]}: {'високосний' if is_year_leap(yr) else 'не високосний'} рік, тому має {result} днів.")
    else:
        print(f"{yr}, {mo} -> Невірний місяць!")

print("Завдання 3")
def is_year_leap(year):
    # Перевірка, чи є рік високосним
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Перевіряємо чи місяць в діапазоні від 1 до 12
    if month < 1 or month > 12:
        return None

    # Кількість днів у кожному місяці
    days_in_months = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Повертаємо кількість днів для даного місяця
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    # Перевірка, чи місяць і день вірні
    if month < 1 or month > 12:
        return None
    
    days_in_current_month = days_in_month(year, month)
    
    if day < 1 or day > days_in_current_month:
        return None
    
    # Підраховуємо кількість днів від початку року до зазначеного дня
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    total_days += day
    return total_days

# Тестування
print(day_of_year(2000, 12, 31))  # 366 (високосний рік)
print(day_of_year(2024, 2, 29))   # 60 (високосний рік)
print(day_of_year(2023, 12, 31))  # 365 (невисокосний рік)
print(day_of_year(2023, 2, 29))   # None (немає 29-го лютого у невисокосному році)
print(day_of_year(2024, 13, 1))   # None (місяць невірний)

print("Завдання 4")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Тестування
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

print("Завдання 5")
# Функція для перетворення літрів на 100 км у милі на галон
def liters_100km_to_miles_gallon(liters):
    # 1 км = 0.621371 милі, 1 літр = 0.264172 галони
    miles_per_100km = 100 * 0.621371  # 100 км у милях
    gallons = liters * 0.264172  # літри у галони
    return miles_per_100km / gallons

# Функція для перетворення миль на галон у літри на 100 км
def miles_gallon_to_liters_100km(miles):
    # 1 км = 0.621371 милі, 1 літр = 0.264172 галони
    kilometers_per_gallon = miles * 1.609344  # милі у кілометри
    liters_per_100km = 100 / kilometers_per_gallon  # літри на 100 км
    return liters_per_100km

# Тестування функцій
print(liters_100km_to_miles_gallon(3.9))   # ~60.31
print(liters_100km_to_miles_gallon(7.5))   # ~31.36
print(liters_100km_to_miles_gallon(10.0))  # ~23.52

print(miles_gallon_to_liters_100km(60.3))  # ~3.90
print(miles_gallon_to_liters_100km(31.4))  # ~7.50
print(miles_gallon_to_liters_100km(23.5))  # ~10.00

print("Завдання 6")
def is_a_triangle(a, b, c):
    # Перевірка, чи всі параметри є додатними числами
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return None
    if a <= 0 or b <= 0 or c <= 0:
        return None

    # Перевірка умови існування трикутника
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Приклад використання
print(is_a_triangle(3, 4, 5))  # True
print(is_a_triangle(1, 1, 2))  # False
print(is_a_triangle(0, 1, 2))  # None
print(is_a_triangle('a', 4, 5))  # None

print("Завдання 7")

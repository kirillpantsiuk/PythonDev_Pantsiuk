# -*- coding: cp1251 -*-
print("�������� 1")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# �������� ������
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

# ������������ �������
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


print("�������� 2")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # ���������� �� ����� � ������� �� 1 �� 12
    if month < 1 or month > 12:
        return None

    # ʳ������ ��� � ������� �����
    days_in_months = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # ��������� ������� ��� ��� ������ �����
    return days_in_months[month - 1]

# ������ ���
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

# ���������� ������� � ���������� � ��������� ������
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    result = days_in_month(yr, mo)
    
    # �������� ��������� � ���������� ������
    month_names = ["�����", "�����", "��������", "������", "�������", "�������", 
                   "������", "�������", "��������", "�������", "��������", "�������"]
    
    if result is not None:
        print(f"{yr}, {month_names[mo-1]}: {'����������' if is_year_leap(yr) else '�� ����������'} ��, ���� �� {result} ���.")
    else:
        print(f"{yr}, {mo} -> ������� �����!")

print("�������� 3")
def is_year_leap(year):
    # ��������, �� � �� ����������
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # ���������� �� ����� � ������� �� 1 �� 12
    if month < 1 or month > 12:
        return None

    # ʳ������ ��� � ������� �����
    days_in_months = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # ��������� ������� ��� ��� ������ �����
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    # ��������, �� ����� � ���� ���
    if month < 1 or month > 12:
        return None
    
    days_in_current_month = days_in_month(year, month)
    
    if day < 1 or day > days_in_current_month:
        return None
    
    # ϳ��������� ������� ��� �� ������� ���� �� ����������� ���
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    total_days += day
    return total_days

# ����������
print(day_of_year(2000, 12, 31))  # 366 (���������� ��)
print(day_of_year(2024, 2, 29))   # 60 (���������� ��)
print(day_of_year(2023, 12, 31))  # 365 (������������ ��)
print(day_of_year(2023, 2, 29))   # None (���� 29-�� ������ � ������������� ����)
print(day_of_year(2024, 13, 1))   # None (����� �������)

print("�������� 4")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# ����������
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

print("�������� 5")
# ������� ��� ������������ ���� �� 100 �� � ��� �� �����
def liters_100km_to_miles_gallon(liters):
    # 1 �� = 0.621371 ���, 1 ��� = 0.264172 ������
    miles_per_100km = 100 * 0.621371  # 100 �� � �����
    gallons = liters * 0.264172  # ���� � ������
    return miles_per_100km / gallons

# ������� ��� ������������ ���� �� ����� � ���� �� 100 ��
def miles_gallon_to_liters_100km(miles):
    # 1 �� = 0.621371 ���, 1 ��� = 0.264172 ������
    kilometers_per_gallon = miles * 1.609344  # ��� � ��������
    liters_per_100km = 100 / kilometers_per_gallon  # ���� �� 100 ��
    return liters_per_100km

# ���������� �������
print(liters_100km_to_miles_gallon(3.9))   # ~60.31
print(liters_100km_to_miles_gallon(7.5))   # ~31.36
print(liters_100km_to_miles_gallon(10.0))  # ~23.52

print(miles_gallon_to_liters_100km(60.3))  # ~3.90
print(miles_gallon_to_liters_100km(31.4))  # ~7.50
print(miles_gallon_to_liters_100km(23.5))  # ~10.00

print("�������� 6")
def is_a_triangle(a, b, c):
    # ��������, �� �� ��������� � ��������� �������
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return None
    if a <= 0 or b <= 0 or c <= 0:
        return None

    # �������� ����� ��������� ����������
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# ������� ������������
print(is_a_triangle(3, 4, 5))  # True
print(is_a_triangle(1, 1, 2))  # False
print(is_a_triangle(0, 1, 2))  # None
print(is_a_triangle('a', 4, 5))  # None

print("�������� 7")

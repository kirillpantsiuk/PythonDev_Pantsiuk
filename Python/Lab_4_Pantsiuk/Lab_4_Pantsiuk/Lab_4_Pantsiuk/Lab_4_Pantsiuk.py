# -*- coding: cp1251 -*-
#�������� 1
#�������������� ���� � ��������� ��������� � Python, �������� ������ ���������� ��������,
# ��� ������ �� ����� ��� �������� n, ���� � ����� ������, � ����� False, ���� n ����� 
# 100 � True, ���� n ����� ��� ������� 100.
#�� ��������� ������ ����� if. ����������� ��� ���, �������������� ���, ����� �����.
print("��������_1")
n = int(input())
print(n >= 100)
## �������� 2
#�������� �������� ���������� ���������� � ���� ������ �����, �������������� ����������� `if-else`.
print("��������_2")
# ������ ��� ������ �����
a = float(input("������ ����� ����� �����: "))
b = float(input("������ ����� ����� �����: "))

# ���������� ���������� �����
if a > b:
    print(f"�������� �����: {a}")
else:
    print(f"�������� �����: {b}")
print("��������_3")

# �������� �����
plant = input("������ ����� �������: ")

# �����
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant}!")
    print("��������_4")
    # ������ input ������������� ��������� �������� ��� ����������
income = 100000  # �� ������ ������ �������� ��� ����������

# ���������� �������
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

# ������� �� ���� ���� ��'�����
if tax < 0:
    tax = 0

# ������������ �������
tax = round(tax, 0)

# ��������� ����������
print("The tax is:", tax, "thalers")

print("��������_5")
# �������� ����
year = int(input("Enter a year: "))

# �������� �� �������� �� �� �������������� ���������
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # �������� �� ���������� ��
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
        print("��������_6")
        # �������� �����
secret_number = 777

# ���������
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# ���� ��� �������� �����
while True:
    user_guess = int(input("Enter your guess: "))  # ���������� ������� �����
    
    if user_guess == secret_number:
        print("Well done, muggle! Now you are free.")
        break  # ����� � �����, ���� ����� ���������
    else:
        print("Ha-ha! You're stuck in my loop!")
        print("��������_7")
        import time  # ������ ������ time ��� ������������ ������� sleep

# ���� for, ���� ���� �� �'���
for i in range(1, 6):  # ���� ���������� � 1 � ���������� �� 5
    print(i, "Mississippi")  # ��������� ������ � ����� "Mississippi"
    time.sleep(1)  # �������� �� ���� ������� �� ����������

# Գ������ ����������� ���� �����
print("Ready or not, here I come!")
print("��������_8")
while True:  # ����������� ����
    user_input = input("Enter a word: ")  # �������� ����� ������������
    
    if user_input == "chupacabra":  # ��������, �� �� �������� �����
        print("You've successfully left the loop.")  # ��������� �����������
        break  # ���������� �����
print("��������_9")
# �������� ����������� ������ �����
user_word = input("Enter a word: ")
user_word = user_word.upper()  # ������������ ����� � ������ ������

# ���� for, �� ��������� ����� ����� ����� �����
for letter in user_word:
    if letter in "AEIOU":  # ��������, �� � ����� ��������
        continue  # ���������� ������ � ���������� �� �������� ��������
    print(letter)  # �������� �� ����� �����, �� �� � ���������
print("���������_10")
word_without_vowels = ""  # ���������� ������� ����� ��� ��������� ���'������ ����

# �������� ����������� ������ �����
user_word = input("Enter a word: ")
user_word = user_word.upper()  # ������������ ����� � ������ ������

# ���� for, �� ��������� ����� ����� ����� �����
for letter in user_word:
    if letter in "AEIOU":  # ��������, �� � ����� ��������
        continue  # ���������� ������ � ���������� �� �������� ��������
    word_without_vowels += letter  # ������ ���'����� ����� �� ������ �����

# �������� �� ����� ����� ��� ��������
print(word_without_vowels)
print("��������_11")

# ������� ������� ����� �� �����������
blocks = int(input("Enter the number of blocks: "))

height = 0  # ���������� ������ ������
current_layer = 1  # ���������� ������� ����� ��� ��������� ����

# ���� ��� ���������� ������ ������
while blocks >= current_layer:
    blocks -= current_layer  # ³������ ������� �����, �� ������ ��� ��������� ����
    height += 1  # �������� ������ ������ �� 1
    current_layer += 1  # �������� ������� ����� ��� ���������� ����

# �������� ���������
print("The height of the pyramid:", height)
print("��������_12")
# ������� ���������� �����
c0 = int(input("Enter a natural number: "))

steps = 0  # ���������� �������� �����

# ���� ��� ��������� ������� ��������
while c0 != 1:
    print(c0)  # �������� ������� �������� c0
    if c0 % 2 == 0:  # ���� c0 �����
        c0 //= 2  # ĳ���� c0 �� 2
    else:  # ���� c0 �������
        c0 = 3 * c0 + 1  # ���������� ���� c0
    steps += 1  # �������� �������� �����

# �������� ������ �������� c0 (��� ������� 1) �� �������� ������� �����
print(c0)
print("steps =", steps)
print("����������_���������_1")
x = 5
y = 10
z = 8

print(x > y)
print(y > z)
print("����������_���������_2")
x, y, z = 5, 10, 8

print(x > z)
print(y - 5 == x)
print ("���������� ���������_3")
x, y, z = 5, 10, 8
x, y, z = z, y, x  
print(x > z)
print(y - 5 == x)
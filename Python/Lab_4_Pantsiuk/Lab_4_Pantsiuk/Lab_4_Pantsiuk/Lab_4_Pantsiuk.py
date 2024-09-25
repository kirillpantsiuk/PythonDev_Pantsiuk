# -*- coding: cp1251 -*-
#Завдання 1
#Використовуючи один з операторів порівняння в Python, напишіть просту дворядкову програму,
# яка приймає як вхідні дані параметр n, який є цілим числом, і друкує False, якщо n менше 
# 100 і True, якщо n більше або дорівнює 100.
#Не створюйте жодних блоків if. Протестуйте свій код, використовуючи дані, надані нижче.
print("Завдання_1")
n = int(input())
print(n >= 100)
## Завдання 2
#Написати програму визначення найбільшого з двох дійсних чисел, використовуючи констуркцію `if-else`.
print("Завдання_2")
# Введіть два дійсних числа
a = float(input("Введіть перше дійсне число: "))
b = float(input("Введіть друге дійсне число: "))

# Визначення найбільшого числа
if a > b:
    print(f"Найбільше число: {a}")
else:
    print(f"Найбільше число: {b}")
print("Завдання_3")

# Введення рядка
plant = input("Введіть назву рослини: ")

# Умови
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant}!")
    print("Завдання_4")
    # Замість input використовуємо фіксоване значення для тестування
income = 100000  # Ви можете змінити значення для тестування

# Розрахунок податку
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

# Податок не може бути від'ємним
if tax < 0:
    tax = 0

# Заокруглення податку
tax = round(tax, 0)

# Виведення результату
print("The tax is:", tax, "thalers")

print("Завдання_5")
# Введення року
year = int(input("Enter a year: "))

# Перевірка чи належить рік до григоріанського календаря
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Перевірка на високосний рік
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
        print("Завдання_6")
        # Секретне число
secret_number = 777

# Привітання
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

# Цикл для введення числа
while True:
    user_guess = int(input("Enter your guess: "))  # Користувач вводить число
    
    if user_guess == secret_number:
        print("Well done, muggle! Now you are free.")
        break  # Вихід з циклу, якщо число правильне
    else:
        print("Ha-ha! You're stuck in my loop!")
        print("Завдання_7")
        import time  # Імпорт модуля time для використання функції sleep

# Цикл for, який рахує до п'яти
for i in range(1, 6):  # Цикл починається з 1 і закінчується на 5
    print(i, "Mississippi")  # Виведення номера і слова "Mississippi"
    time.sleep(1)  # Затримка на одну секунду між ітераціями

# Фінальне повідомлення після циклу
print("Ready or not, here I come!")
print("Завдання_8")
while True:  # Нескінченний цикл
    user_input = input("Enter a word: ")  # Введення слова користувачем
    
    if user_input == "chupacabra":  # Перевірка, чи це секретне слово
        print("You've successfully left the loop.")  # Виведення повідомлення
        break  # Завершення циклу
print("Завдання_9")
# Запитуємо користувача ввести слово
user_word = input("Enter a word: ")
user_word = user_word.upper()  # Перетворюємо слово у верхній регістр

# Цикл for, що проходить через кожну літеру слова
for letter in user_word:
    if letter in "AEIOU":  # Перевірка, чи є літера голосною
        continue  # Пропускаємо голосні і переходимо до наступної ітерації
    print(letter)  # Виводимо на екран літери, які не є голосними
print("Завданння_10")
word_without_vowels = ""  # Ініціалізуємо порожній рядок для зберігання нез'їдених літер

# Запитуємо користувача ввести слово
user_word = input("Enter a word: ")
user_word = user_word.upper()  # Перетворюємо слово у верхній регістр

# Цикл for, що проходить через кожну літеру слова
for letter in user_word:
    if letter in "AEIOU":  # Перевірка, чи є літера голосною
        continue  # Пропускаємо голосні і переходимо до наступної ітерації
    word_without_vowels += letter  # Додаємо нез'їдену літеру до нового рядка

# Виводимо на екран слово без голосних
print(word_without_vowels)
print("Завдання_11")

# Зчитуємо кількість блоків від користувача
blocks = int(input("Enter the number of blocks: "))

height = 0  # Ініціалізуємо висоту піраміди
current_layer = 1  # Ініціалізуємо кількість блоків для поточного шару

# Цикл для обчислення висоти піраміди
while blocks >= current_layer:
    blocks -= current_layer  # Віднімаємо кількість блоків, які потрібні для поточного шару
    height += 1  # Збільшуємо висоту піраміди на 1
    current_layer += 1  # Збільшуємо кількість блоків для наступного шару

# Виводимо результат
print("The height of the pyramid:", height)
print("Завдання_12")
# Зчитуємо натуральне число
c0 = int(input("Enter a natural number: "))

steps = 0  # Ініціалізуємо лічильник кроків

# Цикл для реалізації гіпотези Коллатца
while c0 != 1:
    print(c0)  # Виводимо поточне значення c0
    if c0 % 2 == 0:  # Якщо c0 парне
        c0 //= 2  # Ділимо c0 на 2
    else:  # Якщо c0 непарне
        c0 = 3 * c0 + 1  # Обчислюємо нове c0
    steps += 1  # Збільшуємо лічильник кроків

# Виводимо останнє значення c0 (яке дорівнює 1) та загальну кількість кроків
print(c0)
print("steps =", steps)
print("Контрольне_запитання_1")
x = 5
y = 10
z = 8

print(x > y)
print(y > z)
print("Контрольне_запитання_2")
x, y, z = 5, 10, 8

print(x > z)
print(y - 5 == x)
print ("Контрольне запитання_3")
x, y, z = 5, 10, 8
x, y, z = z, y, x  
print(x > z)
print(y - 5 == x)
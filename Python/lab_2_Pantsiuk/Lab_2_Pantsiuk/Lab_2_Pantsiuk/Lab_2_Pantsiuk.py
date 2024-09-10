# Завданння 1
# Вивести перший рядок з необхідним форматуванням
print("Task 1")
print("Programming***Essentials***in...Python")

# Вивести другий рядок
print("Python")
print("Task 2")
#Завдання 2
#Перший варіант 

def draw_hollow_arrow():
    print("      **      ")
    print("     *  *     ")
    print("    *    *    ")
    print("   *      *   ")
    print("  *        *  ")
    print(" *          * ")
    print("      **      ")
    print("      **      ")
    print("      **      ")
    print("      **      ")
    print("2")
draw_hollow_arrow()
#Другий варіант 
# Функція для відображення верхньої частини стрілки
def draw_arrow_head(max_width):
    # Проходимо по непарних числах для створення рядків стрілки
    for i in range(1, max_width + 1, 2):
        # Обчислюємо кількість пробілів для вирівнювання стрілки по центру
        spaces = (max_width - i) // 2
        # Виводимо пробіли та зірочки для кожного рівня стрілки
        print(" " * spaces + "*" * i + " " * spaces)

# Функція для відображення основи стрілки
def draw_arrow_base(base_width, height):
    # Проходимо по кількості рядків основи
    for _ in range(height):
        # Обчислюємо кількість пробілів для вирівнювання основи по центру
        spaces = (base_width // 2)
        # Виводимо пробіли та зірочки для кожного рядка основи
        print(" " * spaces + "*" * base_width + " " * spaces)

# Основна функція для відображення всієї стрілки
def draw_wide_arrow():
    max_width = 13  # Максимальна ширина верхньої частини стрілки
    base_width = 7  # Ширина основи стрілки
    base_height = 3  # Висота основи (кількість рядків)

    draw_arrow_head(max_width)  # Викликаємо функцію для верхньої частини стрілки
    draw_arrow_base(base_width, base_height)  # Викликаємо функцію для основи стрілки

# Виклик основної функції для відображення стрілки
draw_wide_arrow()


print( "Task 3")
#Завдання 3
print(" I'm student")
#Завдання 4
print ("Task 4")
print("I'm\nlearning\nPython")
print ("Task 5")
# Convert octal number 500 to decimal
octal_number = "500"
decimal_number = int(octal_number, 8)  # Convert from base 8 to base 10

# Output the result
print(f"The octal number {octal_number}_8 is {decimal_number} in the decimal system.")
#Завдання 6
print("Task 6")
# Convert hex number 777 to decimal
hex_number = "777"  # Hexadecimal number as a string
decimal_number = int(hex_number, 16)  # Convert from base 16 to base 10

# Print the result
print(f"The hex number {hex_number}_16 is {decimal_number} in the decimal system.")


# Обчислення виразу 3^(3^4)
result = 3 ** (3 ** 4)


# Виведення результату
print(f"The result of 3^(3^4) is {result}.")

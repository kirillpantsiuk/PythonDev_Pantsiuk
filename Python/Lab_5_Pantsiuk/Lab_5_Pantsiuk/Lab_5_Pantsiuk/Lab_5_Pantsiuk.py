# -*- coding: cp1251 -*-
print("Завдання 1")
hat_list = [1, 2, 3, 4, 5]  # Це існуючий список чисел, що ховається в капелюсі.

# Крок 1: запропонувати користувачеві замінити середнє число на введене число.
hat_list[2] = int(input("Введіть нове число для заміни середнього елемента: "))

# Крок 2: видалити останній елемент зі списку.
hat_list.pop()

# Крок 3: вивести довжину існуючого списку.
print("Довжина списку після змін:", len(hat_list))

print(hat_list)  # Виведення фінального списку
print("Завдання 2")
# Функція сортування методом бульбашки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Оптимізація: прапорець для перевірки, чи були зміни
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Міняємо елементи місцями
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Якщо жодного обміну не було, список уже відсортований
        if not swapped:
            break

# Крок 1: Інтерактивне введення елементів списку
arr = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

# Викликаємо функцію сортування
bubble_sort(arr)

# Виводимо відсортований список
print("Відсортований список:", arr)
print("Завдання 3")
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Створюємо новий список, додаючи до нього тільки унікальні елементи
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# Виведення списку з унікальними елементами
print("The list with unique elements only:")
print(unique_list)
print("Пиклад")
# Створення двовимірного списку для зберігання температур
temps = [[0.0 for h in range(24)] for d in range(31)]

# Виведення структури даних
for day in range(31):
    print(f"Day {day+1}: {temps[day]}")

    print ("Завдання 4")

    def create_chessboard():
        """Створює шахівницю 8x8 з турами по кутах.

    Returns:
        list: Двовимірний список, що представляє шахівницю.
    """

    chessboard = [['_' for _ in range(8)] for _ in range(8)]

    chessboard[0][0] = 'R'
    chessboard[0][7] = 'R'
    chessboard[7][0] = 'R'
    chessboard[7][7] = 'R'

    return chessboard

def print_chessboard(chessboard):
    """Виводить шахівницю в консоль."""
    for row in chessboard:
        print(' '.join(row))

if __name__ == "__main__":
    board = create_chessboard()
    print_chessboard(board)
    
# -*- coding: cp1251 -*-
from random import randrange

def create_board():
    """Створює початкову дошку гри."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Номери клітинок

def display_board(board):
    """Відображає поточний стан дошки."""
    print("\nДошка:")
    for row in board:
        print(" | ".join(str(x) for x in row))
        print("-" * 13)

def enter_move(board, player_sign):
    """Запитує користувача про його хід, перевіряє ввід і оновлює дошку."""
    while True:
        user_input = input("Ваш хід (введіть номер клітинки): ")
        if not user_input.isdigit() or int(user_input) not in range(1, 10):
            print("Неправильний ввід. Будь ласка, спробуйте ще раз.")
            continue

        move = int(user_input)
        row, col = divmod(move - 1, 3)

        if board[row][col] in ['X', 'O']:
            print("Ця клітинка вже зайнята. Спробуйте ще раз.")
            continue

        board[row][col] = player_sign  # Оновлюємо дошку
        break

def make_list_of_free_fields(board):
    """Повертає список вільних клітин у вигляді кортежів (рядок, стовпець)."""
    free_fields = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):  # Якщо клітинка вільна
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    """Перевіряє, чи виграв гравець з 'O' або 'X'."""
    # Перевірка рядків, стовпців та діагоналей
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False  # Переможця не знайдено

def draw_move(board, computer_sign):
    """Випадковим чином обирає вільну клітинку для ходу комп'ютера."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:  # Якщо є вільні клітинки
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = computer_sign  # Комп'ютер ставить свій знак

def print_history(history):
    """Відображає історію ходів гри."""
    print("\nІсторія ходів:")
    for move in history:
        print(move)

def main():
    """Основна функція гри."""
    # Запит користувача про ім'я
    player_name = input("Введіть ваше ім'я: ")
    
    # Запит на вибір символа
    while True:
        player_sign = input("Виберіть ваш символ ('X' або 'O'): ").upper()
        if player_sign in ['X', 'O']:
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть 'X' або 'O'.")

    computer_sign = 'O' if player_sign == 'X' else 'X'  # Призначаємо символ комп'ютера

    wins = 0
    losses = 0
    draws = 0

    while True:
        board = create_board()  # Створення дошки
        display_board(board)

        # Перший хід комп'ютера
        board[1][1] = computer_sign  # Комп'ютер ставить свій знак у центр
        display_board(board)

        history = []  # Історія ходів

        while True:
            enter_move(board, player_sign)
            history.append(f"{player_name} ввів: {player_sign} на позиції {board}")
            display_board(board)

            if victory_for(board, player_sign):
                print(f"Вітаємо, {player_name}! Ви виграли!")
                wins += 1
                break

            if not make_list_of_free_fields(board):
                print("Нічия!")
                draws += 1
                break

            draw_move(board, computer_sign)
            history.append(f"Комп'ютер ввів: {computer_sign} на позиції {board}")
            display_board(board)

            if victory_for(board, computer_sign):
                print(f"На жаль, {player_name}, ви програли!")
                losses += 1
                break

        print_history(history)  # Виведення історії ходів

        # Статистика
        print("\nСтатистика:")
        print(f"Перемоги: {wins}, Поразки: {losses}, Нічії: {draws}")

        # Запит на нову гру
        play_again = input("\nБажаєте зіграти ще раз? (так/ні): ").strip().lower()
        if play_again != 'так':
            break

if __name__ == "__main__":
    main()

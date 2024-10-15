# -*- coding: cp1251 -*-
from random import randrange

def create_board():
    """������� ��������� ����� ���."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # ������ �������

def display_board(board):
    """³������� �������� ���� �����."""
    print("\n�����:")
    for row in board:
        print(" | ".join(str(x) for x in row))
        print("-" * 13)

def enter_move(board, player_sign):
    """������ ����������� ��� ���� ���, �������� ��� � ������� �����."""
    while True:
        user_input = input("��� ��� (������ ����� �������): ")
        if not user_input.isdigit() or int(user_input) not in range(1, 10):
            print("������������ ���. ���� �����, ��������� �� ���.")
            continue

        move = int(user_input)
        row, col = divmod(move - 1, 3)

        if board[row][col] in ['X', 'O']:
            print("�� ������� ��� �������. ��������� �� ���.")
            continue

        board[row][col] = player_sign  # ��������� �����
        break

def make_list_of_free_fields(board):
    """������� ������ ������ ����� � ������ ������� (�����, ��������)."""
    free_fields = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):  # ���� ������� �����
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    """��������, �� ������ ������� � 'O' ��� 'X'."""
    # �������� �����, �������� �� ���������
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False  # ��������� �� ��������

def draw_move(board, computer_sign):
    """���������� ����� ����� ����� ������� ��� ���� ����'�����."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:  # ���� � ���� �������
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = computer_sign  # ����'���� ������� ��� ����

def print_history(history):
    """³������� ������ ���� ���."""
    print("\n������ ����:")
    for move in history:
        print(move)

def main():
    """������� ������� ���."""
    # ����� ����������� ��� ��'�
    player_name = input("������ ���� ��'�: ")
    
    # ����� �� ���� �������
    while True:
        player_sign = input("������� ��� ������ ('X' ��� 'O'): ").upper()
        if player_sign in ['X', 'O']:
            break
        else:
            print("������������ ����. ���� �����, ������� 'X' ��� 'O'.")

    computer_sign = 'O' if player_sign == 'X' else 'X'  # ���������� ������ ����'�����

    wins = 0
    losses = 0
    draws = 0

    while True:
        board = create_board()  # ��������� �����
        display_board(board)

        # ������ ��� ����'�����
        board[1][1] = computer_sign  # ����'���� ������� ��� ���� � �����
        display_board(board)

        history = []  # ������ ����

        while True:
            enter_move(board, player_sign)
            history.append(f"{player_name} ���: {player_sign} �� ������� {board}")
            display_board(board)

            if victory_for(board, player_sign):
                print(f"³����, {player_name}! �� �������!")
                wins += 1
                break

            if not make_list_of_free_fields(board):
                print("ͳ���!")
                draws += 1
                break

            draw_move(board, computer_sign)
            history.append(f"����'���� ���: {computer_sign} �� ������� {board}")
            display_board(board)

            if victory_for(board, computer_sign):
                print(f"�� ����, {player_name}, �� ��������!")
                losses += 1
                break

        print_history(history)  # ��������� ����� ����

        # ����������
        print("\n����������:")
        print(f"��������: {wins}, �������: {losses}, ͳ���: {draws}")

        # ����� �� ���� ���
        play_again = input("\n������ ������ �� ���? (���/�): ").strip().lower()
        if play_again != '���':
            break

if __name__ == "__main__":
    main()

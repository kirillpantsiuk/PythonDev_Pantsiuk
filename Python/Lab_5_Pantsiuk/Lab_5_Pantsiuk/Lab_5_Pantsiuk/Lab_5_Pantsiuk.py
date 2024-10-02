# -*- coding: cp1251 -*-
print("�������� 1")
hat_list = [1, 2, 3, 4, 5]  # �� �������� ������ �����, �� �������� � �������.

# ���� 1: ������������� ������������ ������� ������ ����� �� ������� �����.
hat_list[2] = int(input("������ ���� ����� ��� ����� ���������� ��������: "))

# ���� 2: �������� ������� ������� � ������.
hat_list.pop()

# ���� 3: ������� ������� ��������� ������.
print("������� ������ ���� ���:", len(hat_list))

print(hat_list)  # ��������� ���������� ������
print("�������� 2")
# ������� ���������� ������� ���������
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # ����������: ��������� ��� ��������, �� ���� ����
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # ̳����� �������� ������
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # ���� ������� ����� �� ����, ������ ��� ������������
        if not swapped:
            break

# ���� 1: ������������ �������� �������� ������
arr = list(map(int, input("������ �������� ������ ����� �����: ").split()))

# ��������� ������� ����������
bubble_sort(arr)

# �������� ������������ ������
print("³����������� ������:", arr)
print("�������� 3")
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# ��������� ����� ������, ������� �� ����� ����� ������� ��������
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# ��������� ������ � ���������� ����������
print("The list with unique elements only:")
print(unique_list)
print("������")
# ��������� ����������� ������ ��� ��������� ����������
temps = [[0.0 for h in range(24)] for d in range(31)]

# ��������� ��������� �����
for day in range(31):
    print(f"Day {day+1}: {temps[day]}")

    print ("�������� 4")

    def create_chessboard():
        """������� ��������� 8x8 � ������ �� �����.

    Returns:
        list: ���������� ������, �� ����������� ���������.
    """

    chessboard = [['_' for _ in range(8)] for _ in range(8)]

    chessboard[0][0] = 'R'
    chessboard[0][7] = 'R'
    chessboard[7][0] = 'R'
    chessboard[7][7] = 'R'

    return chessboard

def print_chessboard(chessboard):
    """�������� ��������� � �������."""
    for row in chessboard:
        print(' '.join(row))

if __name__ == "__main__":
    board = create_chessboard()
    print_chessboard(board)
    
# ��������� 1
# ������� ������ ����� � ���������� �������������
print("Task 1")
print("Programming***Essentials***in...Python")

# ������� ������ �����
print("Python")
print("Task 2")
#�������� 2
#������ ������ 

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
#������ ������ 
# ������� ��� ����������� ������� ������� ������
def draw_arrow_head(max_width):
    # ��������� �� �������� ������ ��� ��������� ����� ������
    for i in range(1, max_width + 1, 2):
        # ���������� ������� ������ ��� ����������� ������ �� ������
        spaces = (max_width - i) // 2
        # �������� ������ �� ������ ��� ������� ���� ������
        print(" " * spaces + "*" * i + " " * spaces)

# ������� ��� ����������� ������ ������
def draw_arrow_base(base_width, height):
    # ��������� �� ������� ����� ������
    for _ in range(height):
        # ���������� ������� ������ ��� ����������� ������ �� ������
        spaces = (base_width // 2)
        # �������� ������ �� ������ ��� ������� ����� ������
        print(" " * spaces + "*" * base_width + " " * spaces)

# ������� ������� ��� ����������� �񳺿 ������
def draw_wide_arrow():
    max_width = 13  # ����������� ������ ������� ������� ������
    base_width = 7  # ������ ������ ������
    base_height = 3  # ������ ������ (������� �����)

    draw_arrow_head(max_width)  # ��������� ������� ��� ������� ������� ������
    draw_arrow_base(base_width, base_height)  # ��������� ������� ��� ������ ������

# ������ ������� ������� ��� ����������� ������
draw_wide_arrow()


print( "Task 3")
#�������� 3
print(" I'm student")
#�������� 4
print ("Task 4")
print("I'm\nlearning\nPython")
print ("Task 5")
# Convert octal number 500 to decimal
octal_number = "500"
decimal_number = int(octal_number, 8)  # Convert from base 8 to base 10

# Output the result
print(f"The octal number {octal_number}_8 is {decimal_number} in the decimal system.")
#�������� 6
print("Task 6")
# Convert hex number 777 to decimal
hex_number = "777"  # Hexadecimal number as a string
decimal_number = int(hex_number, 16)  # Convert from base 16 to base 10

# Print the result
print(f"The hex number {hex_number}_16 is {decimal_number} in the decimal system.")


# ���������� ������ 3^(3^4)
result = 3 ** (3 ** 4)


# ��������� ����������
print(f"The result of 3^(3^4) is {result}.")

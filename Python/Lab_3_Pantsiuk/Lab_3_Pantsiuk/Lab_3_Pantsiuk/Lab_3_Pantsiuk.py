import math

# Define the Gaussian function
def gauss_function(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# Example usage
x = 1.0    # value of variable x
mean = 0.0   # mean (expected value)
std_dev = 1.0  # standard deviation

# Calculate the value of the Gaussian function
result = gauss_function(x, mean, std_dev)
print(f"Value of Gaussian function for x={x}, mean={mean}, std_dev={std_dev}: {result}")


print(" exercise 2 ")
# Define variables for the number of apples
john = 3   # number of apples John has
mary = 5   # number of apples Mary has
adam = 6   # number of apples Adam has

# Print the variables in a single line, separated by commas
print(f"{john}, {mary}, {adam}")

# Create a new variable that equals the sum of the three previous variables
total_apples = john + mary + adam

# Print the value of the total_apples variable
print(total_apples)

# Print a string and the value of the total_apples variable together in one line
print(f"Total number of apples: {total_apples}")

print(" exercise 3 ")
kilometers = 12.25
miles = 7.38

# Convert miles to kilometers
miles_to_kilometers = miles * 1.61

# Convert kilometers to miles
kilometers_to_miles = kilometers / 1.61

# Print the results
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

print(" exercise 4 ")
import math

# Зчитування значення з вводу
x = input("Enter a value for x: ")
x = float(x)  # Перетворення введеного значення на тип float

# Обчислення виразу 3x^3 - 2x^2 + 3^x - 1
y = 3 * (x ** 3) - 2 * (x ** 2) + 3 ** x - 1

# Виведення результату
print("y =", y)

print(" exercise 5 ")
# This program computes the number of seconds in a given number of hours

# Number of hours for which we want to calculate the total number of seconds
hours = 2

# Number of seconds in one hour
seconds_per_hour = 3600

# Print the number of hours
print("Hours:", hours)

# Compute and print the number of seconds in the given number of hours
print("Seconds in", hours, "hours:", hours * seconds_per_hour)

# End of the program
print("Goodbye")

print(" exercise 6 ")
# Input values for variables a and b
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

# Prompt the user to choose an arithmetic operation
print("Choose an arithmetic operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Read the user's choice
operation = input("Enter the number of the operation (1/2/3/4): ")

# Perform the chosen operation and output the result
if operation == '1':
    # Output the result of addition
    print("Addition:", a + b)
elif operation == '2':
    # Output the result of subtraction
    print("Subtraction:", a - b)
elif operation == '3':
    # Output the result of multiplication
    print("Multiplication:", a * b)
elif operation == '4':
    # Output the result of division
    # Check if b is not zero to avoid division by zero error
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")

print("\nThat's all, folks!")

print(" exercise 7 ")
# Введіть значення для x
x = float(input("Enter value for x: "))

# Обчислення виразу
# Розкладаємо вираз на декілька кроків для зручності
# Починаємо з самого внутрішнього виразу
inner4 = x + 1 / x
inner3 = x + 1 / inner4
inner2 = x + 1 / inner3
inner1 = x + 1 / inner2
y = 1 / inner1

# Виведення результату
print("y =", y)

print(" exercise 8 ")
# Введіть початковий час (години і хвилини) та тривалість події (хвилини)
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Обчислюємо загальну кількість хвилин від початкового часу
total_minutes = hour * 60 + mins + dura

# Обчислюємо нові години та хвилини
end_hour = (total_minutes // 60) % 24  # Враховуємо перевищення доби
end_minute = total_minutes % 60

# Виведення результату
print(f"End time: {end_hour:02}:{end_minute:02}")



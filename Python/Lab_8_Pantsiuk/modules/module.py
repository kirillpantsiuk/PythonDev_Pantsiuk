# module.py

def add(a, b):
    """Function to add two numbers."""
    return a + b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

if __name__ == "__main__":
    # Testing functions if the module is run directly
    print("Testing the module:")
    print(f"3 + 5 = {add(3, 5)}")
    print(f"3 * 5 = {multiply(3, 5)}")

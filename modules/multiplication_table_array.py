"""
Multiplication Table Arrays Module

This module provides functions to generate a multiplication table as nested arrays.
"""

def generate_multiplication_arrays(number):
    """
    Generate a multiplication table from 1 to the specified number as nested arrays.
    
    Args:
        number (int): The maximum number for the multiplication table
        
    Returns:
        list: A nested list where each inner list contains multiplications for a row
    """
    number = abs(int(number))  # Ensure positive integer
    
    if number == 0:
        return ["0 times anything is 0"]
    
    table_arrays = []
    for x in range(1, number + 1):
        row = []
        for j in range(1, x + 1):
            row.append(x * j)
        table_arrays.append(row)
            
    return table_arrays


def print_multiplication_arrays(number):
    """
    Generate and print a multiplication table as nested arrays.
    
    Args:
        number (int): The maximum number for the multiplication table
    """
    table_arrays = generate_multiplication_arrays(number)
    print(table_arrays)


# Example usage when run as a script
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number to multiply: "))
        print_multiplication_arrays(user_input)
    except ValueError:
        print("Please enter a valid integer.")

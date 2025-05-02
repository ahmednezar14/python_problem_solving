"""
Multiplication Table Module

This module provides a function to generate a multiplication table.
"""

def generate_multiplication_table(number):
    """
    Generate a multiplication table from 1 to the specified number.
    
    Args:
        number (int): The maximum number for the multiplication table
        
    Returns:
        list: A list of strings representing each line of the multiplication table
    """
    number = abs(int(number))  # Ensure positive integer
    
    if number == 0:
        return ["0 times anything is 0"]
    
    table_lines = []
    for x in range(1, number + 1):
        for j in range(1, x + 1):
            table_lines.append(f"{x} x {j} = {x*j}")
            
    return table_lines


def print_multiplication_table(number):
    """
    Print a multiplication table from 1 to the specified number.
    
    Args:
        number (int): The maximum number for the multiplication table
    """
    table_lines = generate_multiplication_table(number)
    for line in table_lines:
        print(line)


# Example usage when run as a script
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number to multiply: "))
        print_multiplication_table(user_input)
    except ValueError:
        print("Please enter a valid integer.")

"""
Mario Pyramid Module

This module provides a function to generate Mario's pyramid pattern.
"""

def generate_pyramid(height):
    """
    Generate Mario's pyramid pattern of a specified height.
    
    Args:
        height (int): The height of the pyramid
        
    Returns:
        list: A list of strings, each representing a row of the pyramid
    """
    if height <= 0:
        return []
    
    pyramid = []
    for i in range(height):
        row = " " * (height - i - 1) + "*" * (i + 1)
        pyramid.append(row)
        
    return pyramid


def print_pyramid(height):
    """
    Print Mario's pyramid pattern of a specified height.
    
    Args:
        height (int): The height of the pyramid
    """
    pyramid_rows = generate_pyramid(height)
    for row in pyramid_rows:
        print(row)


# Example usage when run as a script
if __name__ == "__main__":
    try:
        height = int(input("Enter the number of rows: "))
        print_pyramid(height)
    except ValueError:
        print("Please enter a valid integer.")

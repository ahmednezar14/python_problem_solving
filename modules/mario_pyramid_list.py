"""
Mario Pyramid List Module

This module provides functions to generate Mario's pyramid using list operations.
"""

def generate_pyramid_pop_append(height):
    """
    Generate Mario's pyramid of a specified height using pop and append list operations.
    
    Args:
        height (int): The height of the pyramid
        
    Returns:
        list: A list of strings, each representing a row of the pyramid
    """
    if height <= 0:
        return []
    
    # Initialize with spaces
    spaces = [" "] * height
    pyramid = []
    
    for i in range(height):
        if spaces:  # Check if there are spaces to pop
            spaces.pop(0)
        spaces.append("*")
        pyramid.append("".join(spaces))
        
    return pyramid


def generate_pyramid_list_comprehension(height):
    """
    Generate Mario's pyramid of a specified height using list comprehension.
    
    Args:
        height (int): The height of the pyramid
        
    Returns:
        list: A list of strings, each representing a row of the pyramid
    """
    if height <= 0:
        return []
    
    pyramid = [" " * (height - i - 1) + "*" * (i + 1) for i in range(height)]
    return pyramid


def print_pyramid(pyramid_rows):
    """
    Print the rows of a pyramid.
    
    Args:
        pyramid_rows (list): A list of strings representing the pyramid rows
    """
    for row in pyramid_rows:
        print(row)


# Example usage when run as a script
if __name__ == "__main__":
    try:
        # Method 1: Using pop and append
        print("Mario Pyramid using pop and append method:")
        height1 = 5  # Default height
        pyramid1 = generate_pyramid_pop_append(height1)
        print_pyramid(pyramid1)
        
        # Method 2: Using list comprehension
        print("\nMario Pyramid using list comprehension method:")
        height2 = int(input("Enter the number of rows: "))
        pyramid2 = generate_pyramid_list_comprehension(height2)
        print_pyramid(pyramid2)
        
    except ValueError:
        print("Please enter a valid integer for the height.")

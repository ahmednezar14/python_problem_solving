"""
Character Finder Module

This module provides a function to find the locations of a specific character in a string.
"""

def find_char(input_string, character_to_find):
    """
    Find all occurrences of a character in a string and return their indices.
    
    Args:
        input_string (str): The string to search in
        character_to_find (str): The character to find (only first character is used if multiple)
        
    Returns:
        list: A list of indices where the character was found
    """
    if not character_to_find:
        return []
    
    # Ensure we're only looking for a single character
    char = character_to_find[0]
    
    indices = []
    for i in range(len(input_string)):
        if input_string[i] == char:
            indices.append(i)
            
    return indices


# Example usage when run as a script
if __name__ == "__main__":
    input_string = input("Enter your string: ")
    char_to_find = input("Enter the character to find: ")
    
    indices = find_char(input_string, char_to_find)
    
    print(f"String: {input_string}")
    print(f"Character to find: {char_to_find}")
    
    if indices:
        for index in indices:
            print(f"The character is at index {index}")
    else:
        print(f"The character '{char_to_find}' was not found in the string.")

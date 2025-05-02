"""
Vowel Counter Module

This module provides a function to count the number of vowels in a string.
"""

def count_vowels(input_string):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    
    Args:
        input_string (str): The string to count vowels in
        
    Returns:
        int: The number of vowels in the input string
    """
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    
    for char in input_string.lower():
        if char in vowels:
            count += 1
            
    return count


# Example usage when run as a script
if __name__ == "__main__":
    user_input = input("Enter your word: ")
    vowel_count = count_vowels(user_input)
    print(f"The number of vowels in your word is {vowel_count}")

"""
Main Module for Python Utilities

This module demonstrates how to import and use all the utility modules.
"""

# Import modules from Day 1
from vowel_counter import count_vowels
from character_finder import find_character
from multiplication_table import generate_multiplication_table, print_multiplication_table
from mario_pyramid import generate_pyramid, print_pyramid as print_basic_pyramid

# Import modules from Day 2
from array_sorter import sort_array
from multiplication_table_array import generate_multiplication_arrays
from input_validator import validate_name, validate_email
from mario_pyramid_list import generate_pyramid_pop_append, generate_pyramid_list_comprehension


def demo_vowel_counter():
    """Demo the vowel counter function"""
    print("\n--- Vowel Counter Demo ---")
    test_string = "Hello World"
    vowel_count = count_vowels(test_string)
    print(f"The string '{test_string}' has {vowel_count} vowels.")


def demo_character_finder():
    """Demo the character finder function"""
    print("\n--- Character Finder Demo ---")
    test_string = "Mississippi"
    char_to_find = "s"
    indices = find_character(test_string, char_to_find)
    print(f"In the string '{test_string}', the character '{char_to_find}' is found at indices: {indices}")


def demo_multiplication_table():
    """Demo the multiplication table function"""
    print("\n--- Multiplication Table Demo ---")
    number = 3
    print(f"Multiplication table for {number}:")
    print_multiplication_table(number)


def demo_basic_pyramid():
    """Demo the basic Mario pyramid function"""
    print("\n--- Basic Mario Pyramid Demo ---")
    height = 4
    print(f"Mario pyramid with height {height}:")
    print_basic_pyramid(height)


def demo_array_sorter():
    """Demo the array sorter function"""
    print("\n--- Array Sorter Demo ---")
    test_array = ['c', 'a', 'b', 'e', 'd']
    print(f"Original array: {test_array}")
    
    ascending = sort_array(test_array)
    print(f"Sorted ascending: {ascending}")
    
    descending = sort_array(test_array, descending=True)
    print(f"Sorted descending: {descending}")


def demo_multiplication_arrays():
    """Demo the multiplication table arrays function"""
    print("\n--- Multiplication Table Arrays Demo ---")
    number = 3
    print(f"Multiplication arrays for {number}:")
    arrays = generate_multiplication_arrays(number)
    print(arrays)


def demo_input_validator():
    """Demo the input validator functions"""
    print("\n--- Input Validator Demo ---")
    
    # Just demo with some preset values
    test_name_valid = "John"
    test_name_invalid = "John123"
    test_email_valid = "user@example.com"
    test_email_invalid = "not_an_email"
    
    print(f"Is '{test_name_valid}' a valid name? {validate_name(test_name_valid)}")
    print(f"Is '{test_name_invalid}' a valid name? {validate_name(test_name_invalid)}")
    print(f"Is '{test_email_valid}' a valid email? {validate_email(test_email_valid)}")
    print(f"Is '{test_email_invalid}' a valid email? {validate_email(test_email_invalid)}")


def demo_mario_list_methods():
    """Demo the Mario pyramid list methods"""
    print("\n--- Mario Pyramid List Methods Demo ---")
    
    height = 4
    
    print(f"\nMario pyramid (pop/append) with height {height}:")
    pyramid1 = generate_pyramid_pop_append(height)
    for row in pyramid1:
        print(row)
    
    print(f"\nMario pyramid (list comprehension) with height {height}:")
    pyramid2 = generate_pyramid_list_comprehension(height)
    for row in pyramid2:
        print(row)


def main():
    """Run demos of all utility functions"""
    print("Python Utilities Demo")
    print("=====================")
    
    # Demo Day 1 modules
    demo_vowel_counter()
    demo_character_finder()
    demo_multiplication_table()
    demo_basic_pyramid()
    
    # Demo Day 2 modules
    demo_array_sorter()
    demo_multiplication_arrays()
    demo_input_validator()
    demo_mario_list_methods()


if __name__ == "__main__":
    main()

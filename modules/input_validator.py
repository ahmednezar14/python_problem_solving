"""
Input Validator Module

This module provides functions to validate different types of user input.
"""

import re

def validate_name(name):
    """
    Validate if the provided string is a valid name (contains only alphabetic characters).
    
    Args:
        name (str): The name to validate
        
    Returns:
        bool: True if the name is valid, False otherwise
    """
    return bool(name) and name.isalpha()


def get_valid_name():
    """
    Repeatedly prompt the user for a name until a valid name is provided.
    
    Returns:
        str: A valid name (containing only alphabetic characters)
    """
    name = input("Enter your name: ")
    
    while not validate_name(name):
        print("Please enter a valid name (alphabetic characters only)")
        name = input("Enter your name: ")
        
    return name


def validate_email(email):
    """
    Validate if the provided string is a valid email address.
    
    Args:
        email (str): The email to validate
        
    Returns:
        bool: True if the email is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def get_valid_email():
    """
    Repeatedly prompt the user for an email until a valid email is provided.
    
    Returns:
        str: A valid email address
    """
    email = input("Enter your email: ")
    
    while not validate_email(email):
        print("Invalid email address. Please try again.")
        email = input("Enter your email: ")
        
    return email


# Example usage when run as a script
if __name__ == "__main__":
    # Name validation
    name = input("Enter your name: ")
    if validate_name(name):
        print(f"'{name}' is a valid name.")
    else:
        print(f"'{name}' is not a valid name.")
    
    # Email validation
    email = input("Enter your email: ")
    if validate_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")
        
    # Demo getting valid inputs
    print("\nDemo of getting valid inputs:")
    print("Enter a valid name (alphabetic characters only):")
    valid_name = get_valid_name()
    print(f"Valid name received: {valid_name}")
    
    print("\nEnter a valid email address:")
    valid_email = get_valid_email()
    print(f"Valid email received: {valid_email}")

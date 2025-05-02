"""
Array Sorter Module

This module provides functions to sort arrays in ascending and descending orders.
"""

def sort_array(input_array, descending=False):
    """
    Sort an array in ascending or descending order.
    
    Args:
        input_array (list): The array to be sorted
        descending (bool, optional): Sort in descending order if True, ascending if False
        
    Returns:
        list: A sorted copy of the input array
    """
    # Create a copy to avoid modifying the original array
    sorted_array = input_array.copy()
    sorted_array.sort(reverse=descending)
    return sorted_array


def get_user_array(size=5):
    """
    Get an array of elements from user input.
    
    Args:
        size (int, optional): The size of the array to get from the user
        
    Returns:
        list: The array of elements provided by the user
    """
    user_input = input(f"Enter {size} characters or numbers (no spaces): ")
    
    # Take only the first 'size' characters
    elements = list(user_input[:size])
    
    # If the user provided fewer than 'size' elements, pad with empty strings
    while len(elements) < size:
        elements.append('')
        
    return elements


# Example usage when run as a script
if __name__ == "__main__":
    
    user_array = get_user_array(5)
    
    ascending_sorted = sort_array(user_array)
    print(f"Sorted in ascending order: {ascending_sorted}")
    
    descending_sorted = sort_array(user_array, descending=True)
    print(f"Sorted in descending order: {descending_sorted}")

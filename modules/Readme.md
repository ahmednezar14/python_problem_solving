# Python Utility Modules

This package contains utility modules that provide various functions for string manipulation, pattern generation, array operations, and input validation.

## Modules (Day 1)

### `vowel_counter.py`
Provides functionality to count vowels in a string.
- `count_vowels(input_string)`: Returns the number of vowels in the input string.

### `character_finder.py`
Provides functionality to find all occurrences of a character in a string.
- `find_character(input_string, character_to_find)`: Returns a list of indices where the character is found.

### `multiplication_table.py`
Provides functionality to generate a multiplication table.
- `generate_multiplication_table(number)`: Returns a list of strings representing a multiplication table.
- `print_multiplication_table(number)`: Prints the multiplication table to the console.

### `mario_pyramid.py`
Provides functionality to generate Mario's pyramid pattern.
- `generate_pyramid(height)`: Returns a list of strings representing the pyramid.
- `print_pyramid(height)`: Prints the pyramid to the console.

## Modules (Day 2)

### `array_sorter.py`
Provides functionality to sort arrays in ascending and descending orders.
- `sort_array(input_array, descending=False)`: Returns a sorted copy of the input array.
- `get_user_array(size=5)`: Gets an array of elements from user input.

### `multiplication_table_arrays.py`
Provides functionality to generate a multiplication table as nested arrays.
- `generate_multiplication_arrays(number)`: Returns a nested list representing a multiplication table.
- `print_multiplication_arrays(number)`: Prints the nested arrays to the console.

### `input_validator.py`
Provides functionality to validate different types of user input.
- `validate_name(name)`: Checks if a string is a valid name (contains only alphabetic characters).
- `get_valid_name()`: Repeatedly prompts the user for a name until a valid name is provided.
- `validate_email(email)`: Checks if a string is a valid email address.
- `get_valid_email()`: Repeatedly prompts the user for an email until a valid email is provided.

### `mario_pyramid_list.py`
Provides functionality to generate Mario's pyramid using list operations.
- `generate_pyramid_pop_append(height)`: Generates a pyramid using pop and append list operations.
- `generate_pyramid_list_comprehension(height)`: Generates a pyramid using list comprehension.
- `print_pyramid(pyramid_rows)`: Prints the rows of a pyramid.

## Usage

You can import and use these modules individually:

```python
# Import specific functions
from vowel_counter import count_vowels
from array_sorter import sort_array
from input_validator import validate_email

# Use the functions
vowel_count = count_vowels("Hello World")
sorted_array = sort_array(["c", "a", "b"])
is_valid = validate_email("user@example.com")
```

Or run the demo in `main.py` to see all functions in action:

```
python main.py
```

## Module Structure

```
python_utils/
│
├── __init__.py                    # Makes the directory a Python package
│
├── Day 1 Modules:
│   ├── vowel_counter.py           # Vowel counting functionality
│   ├── character_finder.py        # Character finding functionality
│   ├── multiplication_table.py    # Multiplication table functionality
│   └── mario_pyramid.py           # Basic Mario pyramid pattern
│
├── Day 2 Modules:
│   ├── array_sorter.py            # Array sorting functionality
│   ├── multiplication_table_arrays.py  # Multiplication table as arrays
│   ├── input_validator.py         # Input validation functionality
│   └── mario_pyramid_list.py      # Mario pyramid using list operations
│
├── main.py                        # Demo of all functionalities
└── README.md                      # This file
```

## Running Individual Modules

Each module can also be run as a standalone script:

```
python array_sorter.py
python input_validator.py
# etc.
```

When run individually, each module will prompt for input and demonstrate its functionality.

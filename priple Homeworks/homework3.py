# check_equality.py
# This file contains a function that checks for equality between any two of the three parameters.

def check_equality(param1, param2, param3):
    # Convert parameters to integers if they are strings and can be converted
    try:
        param1 = int(param1)
    except ValueError:
        pass
    
    try:
        param2 = int(param2)
    except ValueError:
        pass
    
    try:
        param3 = int(param3)
    except ValueError:
        pass
    
    # Check for equality between any two parameters
    if param1 == param2 or param1 == param3 or param2 == param3:
        return True
    else:
        return False

# Testing the function
print(check_equality(6, 5, "5"))  # Output: True
print(check_equality(1, "1", 2))  # Output: True
print(check_equality("3", 3, 3))  # Output: True
print(check_equality(4, 5, 6))    # Output: False

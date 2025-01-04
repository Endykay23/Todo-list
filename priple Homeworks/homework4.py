# unique_list.py
# This file contains functions to add unique elements to a list and handle rejected elements.

# Global variables
myUniqueList = []  # An empty list to start
myLeftovers = []   # A list to store rejected elements

def add_to_list(item):
    """
    Adds an item to myUniqueList if it is unique.
    If the item already exists, it is not added.
    
    Parameters:
    item: The item to be added to the list
    
    Returns:
    bool: True if the item was added, False if it already exists
    """
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else:
        return False

def add_to_list_with_leftovers(item):
    """
    Adds an item to myUniqueList if it is unique.
    If the item already exists, it is added to myLeftovers instead.
    
    Parameters:
    item: The item to be added to the list
    
    Returns:
    bool: True if the item was added to myUniqueList, False if it was added to myLeftovers
    """
    if add_to_list(item):
        return True
    else:
        myLeftovers.append(item)
        return False

# Testing the functions
print(add_to_list_with_leftovers("apple"))  # True
print(add_to_list_with_leftovers("banana")) # True
print(add_to_list_with_leftovers("apple"))  # False
print(add_to_list_with_leftovers(42))       # True
print(add_to_list_with_leftovers(42))       # False
print(add_to_list_with_leftovers("cherry")) # True
print(add_to_list_with_leftovers("banana")) # False

# Print the results
print("Unique List:", myUniqueList)
print("Leftovers List:", myLeftovers)

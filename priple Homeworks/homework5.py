# fizz_buzz.py
# This file contains the solution for the Fizz Buzz challenge with an extra feature for identifying prime numbers.

def is_prime(n):
    """
    Check if a number is prime.
    
    Parameters:
    n (int): The number to check for primality
    
    Returns:
    bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fizz_buzz():
    """
    Prints numbers from 1 to 100 with the following rules:
    - For multiples of three, print "Fizz" instead of the number.
    - For multiples of five, print "Buzz" instead of the number.
    - For multiples of both three and five, print "FizzBuzz".
    - For prime numbers, print "prime".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif is_prime(i):
            print("prime")
        else:
            print(i)

# Run the fizz_buzz function
fizz_buzz()

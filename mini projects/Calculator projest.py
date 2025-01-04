def confirmCalculator():  
    calculator = input ("menu\n" 
                        "1. Add\n"
                        "2. Subtract\n"
                        "3. Multiply\n"
                        "4. Divide\n"
                        "Choose an operation: ")  
    calculator = int(calculator)  # Convert input to integer
    if calculator in [1, 2, 3, 4]:   
        num1 = int(input('Enter first number: '))     
        num2 = int(input('Enter second number: '))      
        if calculator == 1:
            result = num1 + num2
        elif calculator == 2:
            result = num1 - num2
        elif calculator == 3:
            result = num1 * num2
        elif calculator == 4:
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero\n"
                      "Try again"
                      )
                confirmCalculator()     
        print("Result is {}".format(result))  # Moved inside the if block0
confirmCalculator()

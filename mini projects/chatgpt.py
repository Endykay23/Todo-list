print("ENDY'S CALCULATOR ")
def calculator():
   print("1 - Add")
   print("2 - Subtract")
   print("3 - Multiply")
   print("4 - Divide")

option = int(input("Choose an operation:  "))
if option in [1, 2, 3, 4]:    
        num1 = int(input("Enter the first number:  "))
        num2 = int(input("Enter the second number:  "))
    
        if option == 1:
            x = num1 + num2
        elif option == 2:
            x = num1 - num2
        elif option == 3:
            x = num1 * num2
        elif option == 4:
            x = num1 / num2
else:    
        print("Invalid operation entered\n"
              "Try again\n"
        )
        calculator()
print("the result of the operation is{}".format(x))          
       
calculator()                
       



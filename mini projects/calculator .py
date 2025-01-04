def confirmCalculator():
    calculator = input("enter operational option:  ")
    if calculator == "0":
        print("Welcome to Endy's CALCULATOR")
    else:
        print(
            "Invaild key\n"
            "Try again"
        )
        confirmCalculator()
          

def confirmCalculator():  
    calculator = input ("menu\n" 
                        "1. Add\n"
                        "2. Subtract\n"
                        "3. Mutiply\n"
                        "4. Divide\n")
    calculator == int(input("choose an operation:  "))    
    if   calculator in [1,2,3,4,] :   
         num1 =int(input('Enter first number:  '))     
         num2 =int(input('Enter second number:  '))      
    elif(calculator == 1):
         result  =num1 + num2
    elif(calculator == 2) :
         result   = num1 - num2

    else:  
        print("invaild operation key")  
        print(" result is {}"(f"result")) 
        confirmCalculator()      

             


           


    
    
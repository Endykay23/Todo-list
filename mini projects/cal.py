
def add(a,b):
    return a+b
def mutiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
operation_dict={
    "+":add,
    "*":mutiply,
    "/":divide,
    "-":subtract
}
def calculator():
    user1 = int(input("enter frist number:  "))
    for symbol in operation_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:    
        op_symbol =  input("pick an operation: ")    
        user2 = int(input("enter next number:    "))
        calculator_function = operation_dict[op_symbol]
        output= calculator_function(user1,user2)
        print(f"{user1} {op_symbol} {user2} = {output}")

        please_continue =input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation or x to exit: ").lower()
        if please_continue == 'y':
            user1 = output
        elif please_continue ==  'n':
             continue_flag = False           
             calculator()
        else:
            continue_flag = False 
            print("Bye")
calculator()            





  
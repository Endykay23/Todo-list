print('Welcome to the platform where you will input your information')
user = input("What is your name: ")
print("Hello " + user)
age = input("What is your age: ")
print("That's nice, you are " + age + " years old")
user = input("Can we continue: ")
if user.upper() == "YES" :
    print('OKAY LETS GO!')
else:
    print("YOU SEE YOU LATER")    
    quit()
    


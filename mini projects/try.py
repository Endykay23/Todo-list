print(" welcome to enid game")
player=input("what is your name? ")
print('nice meeting you ' +  str(player))
player='this a platform where you can play game\ncan we know your age and where you come from?'
print(player)
player=input("ARE YOU READY? ")
if player.upper()=="YES":
   print('OKAY LETS GO!') 
   score=0 
else:
   print('SEE YOU LATER!')           
   quit() 
from datetime import date
today_date=date.today().strftime('%Y')
birth_date=int(input('CAN I KNOW YOUR YEAR OF BRITH '))
print("your current age is: ", int(today_date)-birth_date)
import datetime as today
now=today.datetime.now()
print(now)
print(" MAIN GAME")
print("QUESTION AND ANSWER")
player = input("Q1 WHAT IS THE USE OF A MOUSE? ")
if player.upper()=="MOUSE IS USE FOR CLICKING AND DRAGGING":
   print("CORRECT")
   score+=1
   
else:
   print("INCORRECT")   
player = input("Q2 WHAT IS THE USE ctrl + B? ")
if player.upper()=="IT USE TO BOLD A TEXT":
    print("CORRECT")
    score+=1
else:    
   print("INCORRECT")  
player  = input("Q3 WHAT IS CPU? ")
if player.upper()=="CENTRAL PROCESSING UNIT":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")      
player  = input("Q4 A GROUP OF FILES ARE STORE IN A? ")
if player.upper()=="FOLDER":
   print("CORRECT")
   score+=1
else:
   print("INCORRECT")
player = input("Q5 AN EXAMPLE OF AN OPERATING? ") 
if player.upper()=="WORD":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")   
player = input("Q6 ICT STANDS FOR? ")     
if player.upper()==" Information and Communication Technology ":
    print("CORRECT")
    score+=1
else:
   print("INCORRECT")    
   
print("YOU GOT " + str(score)+ "QUESTION RIGHT")



















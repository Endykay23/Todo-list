import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
def love_message():
    print("I love you\n")
    print("It's you or no one else\n")
    print("I will spend my life with you\n")

# Call the function
love_message()




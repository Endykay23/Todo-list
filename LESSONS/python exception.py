# Exception Handling  
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement:
#Example

#The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")
  
  
  #Example 2:
  #Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
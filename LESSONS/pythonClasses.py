class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Dog(object):
  def __init__(self, name, age,):
      self.name = name
      self.age = age 
      
  def speak(self):    
      print("Hello I am", self.name,"and i am", self.age,"year old")
  def change_age(self, age):
      self.age = age    
      
Endy = Dog ("Endy",  36)    
Adel = Dog("Adel",  89)

Endy.change_age(24)
Adel.change_age(27)

Endy.speak()
Adel.speak()
      

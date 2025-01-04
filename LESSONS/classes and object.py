class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John" , 36)

print(p1)



class speed:
    def __init__(self,):
        self.speed = 60
        self._new_speed = 100
        
    def get_new_speed(self):
        return self._new_speed
s = speed
s.speed =90
print(s.speed)  
        
        
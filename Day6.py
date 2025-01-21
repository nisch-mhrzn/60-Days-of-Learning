x = lambda a,b,c:a*b+c
print(x(5,6,8))

#map function
numbers = [1,2,3,4,5]
strings =['s','t','x','y']
mapped_list = list(map(lambda x,y:(x,y),strings,numbers))
print(mapped_list)
 #map 
days = ['sunday','monday','tuesday']
mod = list(map(str.swapcase,days))
print(mod)

#filter
marks =[95,40,68,70,89,60]
def stud(score):
    return score < 70
fail_list = list(filter(stud,marks))
print(fail_list)

from os.path import join
class FileObject:
    def __init__(self,file_path="~",file_name="test.txt"):
        self.file = open(join(file_path,file_name),'rt')
    def __del__(self):
        self.file.close()
        del self.file
#repr method
class string:
    def __init__(self,string):
        self.string = string
    def __repr__(self):
        return "Object:{}".format(self.string)

        
#Inheriteance
class Vehicle:
    def __init__(self,name,color):
        self.__name = name
        self.__color = color
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color= color
    def get_Name(self):
        return self.__name
class Bike(Vehicle):
    def __init__(self,name,color,model):
        super().__init__(name,color)
        self.__model = model
    def get_details(self):
        return self.get_Name()+self.__model +" in "+ self.getColor()+" color"
b_obj = Bike("Suzuki","red","Tk20")
print(b_obj.get_details())
print(b_obj.get_Name())

# Polymorphism
from math import pi

class Shape:
  def __init__(self, name):
    self.name = name
  def area(self):
    pass

class Sqr(Shape):
  def __init__(self, length):
    super().__init__("Square")
    self.length = length
  def area(self):
    return self.length ** 2

class Circle(Shape):
  def __init__(self, radius):
    super().__init__("Circle")
    self.radius = radius
  def area(self):
    return pi * self.radius ** 2

a = Sqr(6)
b = Circle(10)
print(a.area())
print(b.area())


# try, except, finally
try:
  print(1 / 0)
except:
  print("Error occurred")
finally:
  print("Exit")
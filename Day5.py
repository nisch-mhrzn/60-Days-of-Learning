# Private Variable 

# Single underscore (_)
class test:
    def __init__(self,num):
        self._num= num

# _privatemethod private method
    def _numfunc(self):
        print("Hello")
obj=test(156)

# _attributes can be accessed as normal variables
obj._numfunc()


# Private Variable 
# Double Underscore (__)
class test:
    def __init__(self, num):
        self.__num= num
    def Print(self):
        print("__num = {}".format(self.__num))
obj=test(156)
     

# Private Variable 
# Trailing underscore(n_)
class Test:
    def __init__(self, name):
        #To avoid clash with python keyword 
        self.num_= num

# Local Variable
def test():
    l = "local_variable"
    return l
    
var=test()
print(var)
     

# Global Variable
var = 10
def test():
    var = 20
    print("local variable x:", var)

val=test()
print("global variable x:", var)

# Implementation 2
def outer(a):   # Outer function
  def inner(b):   # Inner function
    return b+10
  return inner(a)

a = 10
var = outer(a) 
print(var)


# Implementation
# fabs() method is defined in the math module which returns the #absolute value of a number
math_score = __import__('math', globals(), locals(), [], 0)
print(math_score.fabs(-17.4))

def result(a,b):
    
    return a+b
print("result is:",result(9,10))
# Implementation 2
def outer(a):   # Outer function
  def inner(b):   # Inner function
    return b+10
  return inner(a)

a = 10
var = outer(a) 
print(var)

class test:
  static_variable = 25

# Access through class
print(test.static_variable) # prints 25

# Access through an instance
ins = test()
print(ins.static_variable) # still 25

# Change within an instance
ins.static_variable = 14
print(ins.static_variable) 

# Access through class
print(test.static_variable)

def result(a, b):
    return a + b

# function with normal variables
print (result(100, 200))
 
# A tuple is created
c = (100, 300)
 
# Tuple is passed
# function unpacked them
 
print (result(*c))
# Private Variable 

# Single underscore (_)
class test:
    def __init__(self,num):
        self._num= num

# _privatemethod private method
    def _numfunc(self):
        print("Private variable")
obj=test(156)

# _attributes can be accessed as normal variables
obj._numfunc()
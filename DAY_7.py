# Decorators

def test_decorator(func):
  def function_wrapper(x):
    print("Before calling " + func.__name__)
    res = func(x)
    print(res)
    print("After calling " + func.__name__)
  return function_wrapper

@test_decorator
def sqr(n):
  return n**2

sqr(20)
# Multiple Decorators
def lowercase_decorator(function):
  def wrapper():
    func= function()
    make_lowercase = func.lower()
    return make_lowercase
  return wrapper

def split_string(function):
  def wrapper():
    func= function()
    split_string =func.split()
    return split_string
  return wrapper

@split_string
@lowercase_decorator
def test_func():
  return 'MOTHER OF DRAGONS'

test_func()
# fibonacci series using Memoization using decorators
def memoization_func(t):
  dict_one = {}
  def h(z):
    if z not in dict_one:            
      dict_one[z] = t(z)
    return dict_one[z]
  return h
    
@memoization_func
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print("the fibonacci sum is :",fib(20))
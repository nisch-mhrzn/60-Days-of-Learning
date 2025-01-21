import pdb
   

class Error(Exception):
    pass
class TooSmallValueError(Error):
    pass

number = 100
while True:
    try:
        num = int(input("enter a number:"))
        
        if num< number:
         raise TooSmallValueError
        print('Good number')
        break
    except TooSmallValueError:
        print("value too small")

import sys,gc
def test():
    list = [18,19,20,34,78]
    list.append(list)
def main():
    print("Garbage Creation")
    for i in range(5):
        test()
            
    print("Collecting...")
    n=gc.collect()
    print("Unreachable objects collected by GC:", n)
    print("Uncollectable garbage list:", gc.garbage)
if __name__ == "__main__":
    main()
    sys.exit()
def multiply(a, b):
  answer = a * b
  return answer
  
pdb.set_trace()
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
sum = multiply(a, b)

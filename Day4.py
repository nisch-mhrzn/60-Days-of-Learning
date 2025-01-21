tup = (10,"Hello",31.4,"a")
print(tup)
print(type(tup))
print(tup[-2])#2nd last element
print(tup[::-1])


# concatenation using + operator
print(tup + (50,60))
print(10 in tup)
print("world" in tup)



# Iterate through Tuple : use for loop to iterate through each item in a tuple
tup = (10,"Hello",3.14,"a")
for i in tup:
    print(i)

# Set operations 
X = {10, 20, 30, 40, 50}
Y = {40, 50, 60, 70, 80}
Z = {20, 30, 100, 50, 10}

# Union : Union of X, Y, Z is a set of all elements from all three sets using | operator or union() method
print("Set Union:", X|Y|Z)

# Intersection :Intersection of X, Y, Z is a set of all elements from all three sets using & operator or intersection()
print("Set Intersection:", X&Y&Z)

# Difference : Difference of X, Y is a set of all elements from both sets using - operator or difference()
print("Set Difference:", X-Y)



# Removing elements : Use the methods discard(), pop() and remove()
set_one = {100, 70, 40, 10, 80, 20, 60, 30}

# discard() method
set_one.discard(100)
print("After discard:",set_one)

# remove() method
set_one.remove(40)
print("After removing element :", set_one)

# pop() method
set_one.pop()
print("After removing element :", set_one)


if len(tup) <20:
    print(f"The length of tuple is:", len(tup))
    print("what a good day")


# While with else statement
print("While loop")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
# continue statement
print('Continue Statement')
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
     
     
class cat:
    def __init__(self,cat_name,cat_breed):
        self.name = cat_name
        self.breed = cat_breed

class emp:
    x= 10
    def __init__(self):
        self.name = 'steve'
        self.salary = 10000
    def display(self):
        print(self.name)
        print(self.salary)
obj_emp=emp()
print("Dictionary conversion:",vars(obj_emp))
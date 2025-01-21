# Int data type
var = 5
print(var)
print(type(var))


# Float data type
var2 = 0.1234
print(var2)
print(type(var2))
     


# Complex numbers data type
x = 2j
print(x)
print(type(x))
     

# String Data type
str_one = "Hello World"
print(str_one)
print(type(str_one))
     

# list data type
list1 = ["cat", "bike"]
print(list1)
print(type(list1))
     
['cat', 'bike']


# tuple data type
tup = ("cat", "bike", "bus")
print(tup)
print(type(tup))
     
('cat', 'bike', 'bus')


# dictionary data type
dict_one = {"Name": "Steve", "Location": "NewYork"}
print(dict_one)
print(type(dict_one))
     

# Set data type
set_one = set({"Hello", "world", "Hello"})
print(set_one)
print(type(set_one))
     

# Frozen set
f_one = frozenset({"Hello", "World", "Hello"})
print(f_one)
print(type(f_one))
     

# Boolean data type
b = True
print(b)
print(type(b))
  
  #Strings 
str1 = "Welcome to complete Python Course"
str2 = "Welcome to the complete Python Course"
str3 = """This is a
        multiline
        String"""

print(str1)
print(str2)
print(str3)

#indexing
s="captain america"
print(s[5])
# Slicing : slice(start, stop, step), it returns a sliced object containing elements in the given range
print(s[1:5:2])#2 is step
print(s[-1])#last element
print(s[::-1])#reverse a tring
#Captial
a = "complete python course"
print(a.capitalize())




# count(sub[, start[,end]]) : Returns the number of non-overlapping occurrences of substring (sub) in the range [start, end]
a = "Welcome to complete Python Course"
print(a.count("c"))
print(a.count("o"))
print(a.count("Python"))


# find(sub[, start[, end]]) : Returns the lowest index in the string where substring is found within the slice [start, end]
a = "Exercise"
print(a.find("r"))
print(a.find("e"))
#Arithmatic Operators
x=10
y=4

#Addition
print("Addition:", x + y)

#Subtraction
print("Subtraction:", x - y)

#Multiply
print("Multiply: ", x * y)

#Division
print("Division:", x / y)

#Modulus
print("Modulus:", x % y)

#Floor Division
print("Floor Division:", x // y)

#Exponent
print("Exponent:", x ** y)
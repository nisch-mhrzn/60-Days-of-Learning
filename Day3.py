
# Create a List
list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print(list_one)
# List with different data types
list_two = ['abc',67,True,3.14,"female"]
print(list_two)
     
# type() with List
print(type(list_two))


# nested list
list_nest= ["hello",[8,4,6],['World']]
print(list_nest)


# slice lists in Python : Use the slicing operator :(colon)
list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print(list_one[1:4])
# sort() method: Sort items in a list in ascending order
list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.sort()
print(list_one)
     
# reverse() : Reverse the order of items in the list
list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.reverse()
print(list_one)
# Membership : check if an item exists in a list or not, using the keyword in
list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print('tuesday' in list_one)
     

# insert() method : insert item at a desired location
list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.insert(2,'friday')
print(list_one)


sqr = [2**x for x in range(10)]
print(sqr)

# dict with items
dict_one = {0:'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday'}
print(dict_one)
     
# Accessing Elements from Dictionary : Using keys or get() method
dict_one = {0:'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday'}
print(dict_one[1])

# get() method
print(dict_one.get(2))
# Changing and Adding Dictionary elements: add new items or change the value of existing items using an = operator
dict_one = {0:'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday'}

# change element
dict_one[2] = 'friday'
print("After changing the element", dict_one)

# add element
dict_one[5] = 'saturday'
print("After adding the element :", dict_one)

# Iterate through dictionay
dict_one = {0:'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday'}
for i in dict_one.items():
    print(i)
    
    
# Dictionary Comprehension
cubes = {x: x*x*x for x in range(10)}
print(cubes)
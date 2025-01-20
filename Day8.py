from collections import defaultdict
default_dict_var = defaultdict(list)
for i in range(10):
    default_dict_var[i].append(i)
print(default_dict_var)

from collections import OrderedDict
my_dict ={'sunday':1,'Monday':0,'tuesday':2}
#creating odered dict
orderedDict=OrderedDict(my_dict)
print(orderedDict)
def test():
    num = 0
    while num<10:
        yield num
        num+=1

for i in test():
    print(i,end='\n')



# Python generator with Loop
# Reverse a string
print('\n')
def reverse(text_str):
    length = len(text_str)
    for i in range(length-1,-1,-1):
        yield text_str[i]
for char in reverse("trojan"):
    print(char,end='')
    
#Generator Expression
#Initialize the list
test_list =[1,3,6,10]
list_comprehension =[x**3 for x in test_list]
test_generator =(x**3 for x in test_list)

print(list_comprehension)
print(type(test))
print(tuple(test_generator))


def func():
    print("My first Collection")
    while True:
        var =(yield)
        print(var)
coroutine =func()
next(coroutine)



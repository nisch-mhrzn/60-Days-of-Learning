#importing Pandas Library as pd (an alias name given to Pandas Library)
import pandas as pd
s = pd.Series([100,290,40,199,76])
print(s)
print(type(s))
print(s.axes)
print(s.dtype)
print(s.ndim)
print(s.ndim)
print(s.values)


# specify indexes in string/objects
s1 = pd.Series([1, 2, 4, 5, 6], index = ["First", "Zero", "Second", "Third", "Fourth"])
print(s1)
print(f"After sorting: ",s1.sort_index(),"\n")

ages = {'Andrew': 31, "Kate": 45, "Matthew": 26, "Helen": 19}
new_ages = pd.Series(ages)
print(new_ages)
# select particular elements from dict
age=pd.Series(ages,index =["Andrew","Helen"])
print("particular age",age,"\n")


#creating pandas series by Numpy array
import numpy as np
n_one = np.array([1,2,3,4])
print(pd.Series(n_one),"\n")

s1 = pd.Series([2,3,55,2,6,44])
s2 = pd.Series([42,32,34,2,1,44])
pd.concat

#Pandas Dataframe

names ={"Names":["Allen","rob","Harold","Amy"],"Age": [21, 11, 13, 15]} 
# Creating a DataFrame using a Dictionary.
new_dic = pd.DataFrame(names)
print(new_dic["Age"],"\n")

# assign column name
var = [10, 30, 20, 89, 48, 40]
df = pd.DataFrame(var, columns = ["Variables"])
print(df,"\n")

# create from numpy
arr = np.random.randint(10, size = (5, 2))

new_arr= pd.DataFrame(arr,columns = ["Var1","Var2"])
print(new_arr)


# determine shape
print(new_arr.shape)
#dimesnion of dataframe
print(new_arr.ndim)

print(new_arr.size)





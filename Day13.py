# Pandas Dataframe
import pandas as pd
import numpy as np

names = {"Names": ["Allen", "rob", "Harold", "Amy"], "Age": [21, 11, 13, 15]}
# Creating a DataFrame using a Dictionary.
new_dic = pd.DataFrame(names)
print(new_dic["Age"], "\n")

# assign column name
var = [10, 30, 20, 89, 48, 40]
df = pd.DataFrame(var, columns=["Variables"])
print(df, "\n")

# create from numpy
arr = np.random.randint(10, size=(5, 2))

new_arr = pd.DataFrame(arr, columns=["Var1", "Var2"])
print(new_arr)


# determine shape
print(new_arr.shape)
# dimesnion of dataframe
print(new_arr.ndim)

print(new_arr.size)
print(new_arr.columns)
import pandas as pd
import numpy as np
# Sorting Indexes
dfc = pd.DataFrame(
    {
        "Name": ["Josh", "Rachel", "Tim", "Kate", "Zach", "Andrew"],
        "Age": [11, 13, 16, 12, 14, 18],
        "Salary": [10000, 23000, 18000, 3900000, 19000, 24000],
    }
)
print(dfc)
dfc.iloc[2] = ["Ron", 15, 185]
print(dfc)
print(dfc.Age)
print(f"the age of the 3rd row is:", dfc["Age"][3])
roll_no = [111, 1233, 45, 67, 89, 1101]
print("Adding new column")
dfc["Roll Number"] = roll_no
print(dfc)
# set index on the basis of "Roll Number"
dfc.set_index("Roll Number", inplace=True)
print(dfc, "\n")
print(dfc.loc[89])
dfc = pd.DataFrame(
    {
        "Name": ["Josh", "Rachel", "Tim", "Kate"],
        "Age": [11, 23, 47, 86],
        "Salary": [10000, 90000, 387737, 9000],
    },
    index=[1, 89, 67, 800],
)
dfc.sort_index(inplace=True)
print(f"the sorted dataframe is: \n", dfc)

employess = pd.DataFrame(
    {
        "Name": ["Josh", "Mike", "Sergio"],
        "Department": ["It", "HR", "Fiannace"],
        "Income": [9000000, 8900000, 9000087],
        "Age": [24, 23, 22],
    }
)

print(employess, "\n")

print(employess["Department"] == "It", "\n")

print(employess.loc[employess["Department"] == "It", "Name"], "\n")

print(employess[employess["Income"] > 5500], "\n")

print(employess[(employess["Age"] > 30) | (employess["Department"] == "HR")], "\n")

print((employess[~(employess["Age"] < 35)]), "\n")

print(employess.filter(items=["Department", "Name", "Income"]), "\n")
print("removing row of JOsh", "\n")
# New row to add
new_employee = pd.DataFrame([{"Name": "Josh"}])

# Use pd.concat to add the new row
employees = pd.concat([employess, new_employee], ignore_index=True)
print("Appending a new row", "\n")
# New row to add as a DataFrame
new_employee = pd.DataFrame(
    [{"Name": "Josh", "Age": 23, "Department": "Finance", "Salary": 90000}]
)
# Use pd.concat to add the new row
employees = pd.concat([employess, new_employee], ignore_index=True)

print(employees)
print("\n", "Dropping employees of age greater than 23")
print(employess.drop(employess[employess["Age"] > 23].index))

import numpy as np
import pandas as pd

arr1 = np.array([[12, 43, 56], [78, 88, 95], [79, 89, 43]])
arr2 = np.array([5, 6, 7, 12, 34, 67, 89])

# mean
print("\n" "Mean: ", np.mean(arr2))
# Median function
print("Median:", np.median(arr2))
# Standard Deviation Function
print("Standard Deviation:", np.std(arr2))
# Variance Function
print("Variance:", np.var(arr2))
# Average Function
print("Average:", np.average(arr2))
# Minimum Function
print("Minimum element:", np.amin(arr1))
# Maximum Function
print("Maximum element:", np.amax(arr1),"\n")
 
df = pd.DataFrame({'A':[1,10,20,2],
                   'B':[1,2,30,40],
                   "C":np.random.randn(4)})
result = df.groupby('B').agg(['min','max'])
print(result, "\n")

print("Q2 quantile of arr:",np.quantile(arr2,.50))
print("Q1 quantile of arr:",np.quantile(arr2,.25))
print("Q3 quantile of arr:",np.quantile(arr2,.75))
print("100th quantile of arr:",np.quantile(arr2,.1))

arr = [31, 35, 45, 49, 59, 69, 74, 79, 80, 81, 89, 94, 96, 99, 101, 104, 112, 117,119,127,134]
# First quartile (Q1)
Q1 = np.median(arr[:12])
# Third quartile (Q3)
Q3 = np.median(arr[12:])
# Interquartile range (IQR)
IQR = Q3 - Q1
print(f"the Inter Quartile Range is",IQR,"\n")

#continuous distribution
from scipy.stats import uniform
arr2 = np.array([5,6,7,12,34,67,89]) 
print ("The continuous distribution: ",uniform.cdf(arr2, loc =4 , scale = 5))
#normal distribution
from scipy.stats import norm
import numpy as np
arr2 = np.array([0.91,0.17,0.99996833, 0.81, 0.97,0.54])
print("The normal distribution:\n ",norm.ppf(arr2))
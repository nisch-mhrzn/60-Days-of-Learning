#NUMPY
import numpy as np
a = np.array([1,2,3])
print(a,"\n")

print(np.zeros(7),"\n")

print(np.zeros(7,dtype=int),"\n")
print(np.ones((3,5),dtype=int),"\n") #3 arrays of size 5
print(np.full((3,5),5,dtype=int),"\n")
print(np.eye(5),"\n")

print(np.arange(1,15).reshape(2,7))

a3=np.array([[1,2],[3,4]])
a3.flatten()
a2= np.arange(1,9).reshape((1,8))
print(a2,"\n")
a2.reshape(-1)
a2.flatten()
print(a2,"\n")

#concat
a1 = np.array([100, 110, 140])
a2 = np.array([120, 121, 220])
a3=np.concatenate([a1, a2])
print(a3,"\n")

#Broadcasting
arr1 = np.array([1, 0, 1])
arr2 = np.array([2])
print(arr1 + arr2,"\n")
print(arr1 * arr2,"\n")

#scalar product
arr1 = np.array([[30, 15],
                 [19, 42]]) 
arr2 = np.array([[101, 90],
                 [45, 64]])
print(np.dot(arr1,arr2))

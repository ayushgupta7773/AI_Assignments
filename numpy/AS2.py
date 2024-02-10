import numpy as np 
import pandas as pd
# a = np.array([[6, 28], [8, 56], [7, 19]]) 
# x = np.transpose(a).reshape(1,6) 
# print(x)
# a = np.arange(10,22).reshape((3, 4)) 
# print(a)

# arr = 2 * np.arange(0,2,0.5) 
# # if arr <= 0.6: print("condition satisfies") 
# # else: print("condition doesn't satisfy")
# a=np.all(arr>0.6)
# print(a)

'''
arr1 = np.array([1,2,3,6,3,2]) 
arr2 = np.array([4,2,1,3,3,2]) 
arr3 = np.zeros(len(arr1))

# for i in range(len(arr1)): arr3[i] = arr1[i] * arr2[i]
# print(arr3)

def m(a,b):
    return a*b


v_func=np.vectorize(m)
arr3=v_func(arr1,arr2)
print(arr3)
'''



# a= np.array([[16, 5], [81, 6], [33, 1]]) 
# x=np.transpose(a).reshape(2,3) 
# print(x.flatten())
'''def ay(n):return round(n)
vfunc= np.vectorize(ay)

a=np.arange(0,100,14)
a=np.random.randint(0,100,10)
a=np.random.rand(2,3)*170
a=vfunc(a)

print(a)

'''

'''
a = np.array([[34, 28,55], [8, 56, 3], [77, 87, 19]]) 
print(a.transpose()[-2,-2])'''











import numpy as np
'''
x = np.ones((5,5)) 
x[1:-1,1:] = 0
print(x)'''

# A= np.arange(9).reshape(3,3)

# print(A[:, ::-1])
'''

X = np.arange(12).reshape((3, 4))
# row = np.array([0, 1, 2])
# mask = np.array([1, 0, 1, 0], dtype=bool)
# print(X[row[:, np.newaxis], mask])

# print([i for i in X])


arr1 = np.array([[1,2], [3,4],[5,6]])
arr2 = np.array([1,2,3])
print(np.dot(arr1, arr2))  #[ 5 11]
'''
''''arr= np.array([[2,3,4,5],[1,7,3,5],[2,8,6,9],[11,23,12,19]])
arr1 = np.array([[2,2,2,2]])
def func(x, y):
    return x * y
vec = np.vectorize(func)
print(vec(arr, arr1))'''



'''x = np.array([[200,200,200],
              [300,300,300],
              [400,400,400]])
# v = np.array([200,300,400])
v=np.array([[200],
 [300],
 [400]])
print((x / v))
# print(v[:,None])'''

'''
p = np.array([[0], [10], [20]])
# q = np.array([10, 11, 12])

# print((p + q))
q=p[p>0]
# p[0][0]=1
print(q)
'''

# arr = np.arange(16)
# print(np.split(arr,8))


# # A.shape = (3,3,1) and B.shape =(3,3)
# A=np.arange(1,10).reshape(3,3)
# A[1][1]=0
# # B=np.arange(10,19).reshape(3,3)
# # A = A.squeeze(axis=2) 
# # B = np.expand_dims(B, axis=2)

# # print(A,(A.shape()))
# # print(B,(B.shape()))

# print(np.all(A,1))
# A = np.arange(9).reshape(3,3)
# print(A)
# print(A[:, ::-1])

# X = np.arange(12).reshape((3, 4))
# row = np.array([0, 1, 2])
# mask = np.array([1, 0, 1, 0], dtype=bool)
# print(X[[0,1,2],mask])
v = np.array([200,300,400])
print(v[:,None])
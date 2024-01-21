import numpy as np
import numpy.matlib

a=np.matrix('1.,3,1;2,3,4;3,1,1') 
print(a)
b=np.array([[1,2],[1,3],[1,4]])
s=np.matmul(a,b) #returns scalar
print(s)
# print(a+b)   #returns vector
arr1=np.array([[1,2,1],[0,2,1],[1,1,1]])
arr2=np.array([[1,2,1],[1,0,1],[2,3,1]])
print(np.dot(arr1,arr2))
print(np.vdot(arr1,arr2))
print(np.inner(arr1,arr2)) #number of col of both arrays should be equal


arr1=np.array([[1,2,3],[4,5,6],[1,2,1]])
arr2=np.array([[1,3,2],[5,4,7],[1,1,1]])
print("np.add(arr1,arr2)")
print(np.add(arr1,arr2))
print("np.inner(arr1,arr2)")
print(np.inner(arr1,arr2))

arr1 = np.arange(18).reshape(3, 2, 3)
print("arr1")
print(arr1)
arr2 = np.arange(6).reshape(3,2)
print("arr2")
print(arr2)
print("np.matmul(arr1, arr2)")
result = np.matmul(arr1, arr2)
print(result)

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[1,1,1],[2,2,3],[5,5,6]])
print(np.linalg.det(arr2))
arr1=np.array([[1,2,3],[4,5,6],[7,8,10]])
s=np.linalg.inv(arr1)
print(arr1)
print(s)
print(np.matmul(s,arr1))
arr1=np.array([[2,3],[3,4]])
print(np.linalg.inv(arr1))
s=np.linalg.inv(arr1)
b=np.array([[8],[10]])
print(np.linalg.solve(arr1,b))

arr1=np.array([[1,2,3],[4,5,6],[7,1,0]])
print(arr1)
eig_val,eig_vect=np.linalg.eig(arr1)
print(eig_val)
print(eig_vect)

arr1=np.matlib.diag((1,2,3,4,5))
print(np.linalg.matrix_rank(arr1))
print(np.trace(arr1))
print(arr1)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])
D= np.array([[1,1],[2,3]])
print(np.dot(np.dot(np.dot(A,B),C),D))
print(np.linalg.multi_dot([A,B,C,D]))

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2],[3,4],[5,6]])
print(np.outer(arr1,arr2))

# complexNumber

a=np.array([complex(1,2),complex(3,4)])
b=np.array([complex(5,6),complex(7,8)])
print("dot is ", np.dot(a,b))
a=np.array([complex(1,2),complex(3,4)])
b=np.array([complex(5,6),complex(7,8)])
print("vdot is " , np.vdot(a,b))
print(complex(1,2))


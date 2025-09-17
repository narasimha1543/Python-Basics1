#numpy_arrays:
import numpy as np
import array as arr

#creating an array with numpy:
# 1 dimentional
a1d=np.array([1,2,3,4,5])
print(a1d)

# 2 dimentional
a2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# [
#    1  2  3
#    4  5  6
#    7  8  9
#]
print(a2d)

#mention and operations in numpy array:

#1. basic array information methods:
a=np.array([1,2,3,4,5])

# ndim: returnd the number of dimentions of the array.

print(a.ndim)
print(a1d.ndim)
print(a2d.ndim)

#shape: returns a tuple showing the sizes of the array in each dimentions(rows,column,etc..)
print(a1d.shape)
print(a2d.shape)

#size:
print(a1d.size)
print(a2d.size)

#dtype:return the datatype of the element in a array.
print(a1d.dtype)
print(a2d.dtype)

#2. creating an array with numpy:
#zeros: 
print(np.zeros(7))

#ones:
print(np.ones(7))

#arange:
print(np.arange(1,11,1))
print(np.arange(0,11,2))
print(np.arange(1,11,2))

#linspace: creates 3 numbers evenly spaced between 0 and 1
print(np.linspace(0,1,3))

#mathematical operations:
a=np.array([1,2,3,4,5])
l=[1,2,3,4,5]
print(a+6)
print(a-1)
print(a*2)
print(a/2)
print(a//2)
print(a**6)

#aggregate functions:
a=np.array([1,2,3,4,5])

#sum():
print(np.sum(a))

#mean():
print(np.mean(a))

#max():
print(np.max(a))

#min():
print(np.min(a))

#median():
print(np.median(a))

#std:
print(np.std(a))

#cumprod:
print(np.cumprod(a))

#matrix operations:
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# [
#     1  2  3
#     4  5  6
#     7  8  9
# ]
mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
# [
#     9  8  7
#     6  5  4
#     3  2  1
# ]

print(mat1+mat2)
print(mat1**2)
print(mat1*mat2)

#dot():
print(np.dot(mat1,mat2))

#transpose:
print(np.transpose(mat1))
print(np.transpose(mat2))
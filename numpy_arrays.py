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



NumPy and NumPy Arrays

✅What is NumPy?
 NumPy (Numerical Python) is a Python library used for scientific and mathematical
computing.
 It provides:
o Powerful array objects (more efficient than Python lists).
o Vectorized operations (fast element-wise calculations).
o Support for linear algebra, statistics, Fourier transforms, random numbers, etc.

👉To use NumPy, install it (if not installed):
pip install numpy

✅Importing NumPy
import numpy as np

3. NumPy Arrays
✅Creating a NumPy Array
import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
👉ndarray means “n-dimensional array.”
 arr1 → 1D
 arr2 → 2D

4. Methods and Operations in NumPy Arrays
A. Basic Array Information
arr = np.array([1, 2, 3, 4, 5])

print(arr.ndim) # Returns the number of dimensions (axes) of the array.
print(arr.shape) # Returns a tuple showing the size of the array in each dimension (rows,
columns, etc.).
print(arr.size) # Returns the total number of elements in the array.
print(arr.dtype) # Returns the data type of the elements in the array.
✅Output:
1
(5,)
5
int32 # (on most systems, could also be int64 depending on your OS/processor)
Explanation of Output:
1. arr.ndim → 1
Because this is a 1D array (just one row of elements).
2. arr.shape → (5,)
This means the array has 5 elements in one dimension.

3. arr.size → 5
There are exactly 5 total elements in the array.
4. arr.dtype → int32 / int64
Shows the data type of elements (here integers).
o On Windows (64-bit) → usually int32
o On Linux/macOS (64-bit) → usually int64

B. Creating Arrays with NumPy
import numpy as np

print(np.zeros(5)) # Creates an array of 5 zeros → [0. 0. 0. 0. 0.]
print(np.ones(5)) # Creates an array of 5 ones → [1. 1. 1. 1. 1.]
print(np.arange(1, 10, 2)) # Creates an array from 1 to 9 with step 2 → [1 3 5 7 9]
print(np.linspace(0, 1, 5)) # Creates 5 numbers evenly spaced between 0 and 1 → [0. 0.25 0.5
0.75 1. ]

C. Indexing and Slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[0]) # First element → 10
print(arr[-1]) # Last element → 50
print(arr[1:4]) # Elements from index 1 to 3 → [20 30 40]

D. Mathematical Operations
arr = np.array([1, 2, 3, 4, 5])

print(arr + 5) # Add 5 to every element → [ 6 7 8 9 10]
print(arr * 2) # Multiply every element by 2 → [ 2 4 6 8 10]
print(arr ** 2) # Square of each element → [ 1 4 9 16 25]

E. Aggregate Functions
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr)) # Sum → 150
print(np.mean(arr)) # Average → 30
print(np.max(arr)) # Maximum → 50
print(np.min(arr)) # Minimum → 10
print(np.std(arr)) # Standard Deviation

G. Multi-Dimensional Arrays (Matrix Operations)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a + b) # Matrix addition
print(a * b) # Element-wise multiplication
print(np.dot(a, b)) # Matrix multiplication

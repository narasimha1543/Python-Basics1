# #arrays in python:
l=[10,10.5,"hello",True]
a=[10,20,30,40,50]
a=[10.5,20.2,30.3,40.4,50.5]

# # ARRAYS VS LIST

# #IMPORTING THE ARRAY MODULE:
import array as arr

# #creating an array:
numbers=arr.array("i",[1,2,3,4,5])   #i=integer , u= string , f= float
# print(type(numbers))
# print(numbers)
# i=integer , 
# u= string ,
#  f= float

# #accessing array element.
# print(numbers[0])
# print(numbers[3])
# print(numbers[-1])

#adding an element in array:
#append()
numbers.append(7)
print(numbers)

#insert():
numbers.insert(2,6)
print(numbers)

#extend():
numbers.extend()
print(numbers)

deleting an element:
# #remove():
# numbers.remove(2)
# print(numbers)

# #pop():
# numbers.pop(-4)
# print(numbers)

# #clear():
# numbers.clear()
# print(numbers)

#updating an element:
numbers[0]=10
print(numbers)

#looping thrugh arrays:
for i in numbers:
    print(i)

#basic operations on arrays:
#len():
print(len(numbers))
#max():
print(max(numbers))
#min():
print(min(numbers))

1. What is an Array? (Definition)
 An array is a collection of elements of the same data type stored in a continuous
memory location.
 Arrays are used to store multiple values in a single variable.
 Example: Storing 10 numbers in a single array instead of creating 10 separate variables.
👉In simple words: An array is like a list of similar items kept together.

2. Why Arrays? (Importance)
 Saves memory.
 Easy to manage multiple values.
 Allows faster operations like searching and sorting.
 Useful in mathematical and scientific problems.

3. Arrays vs Lists in Python
 In Python, we often use lists instead of arrays because lists are more flexible.
 But Python also provides an array module for creating arrays when all elements must be
of the same type.
Feature List Array
Data Types

Can store multiple data types together
(e.g., int, float, string, boolean).

Can only store values of the same
data type.

Flexibility

Very flexible – you can add any type of
item.

Less flexible – restricted to one
type.

Module
Requirement

Built-in, no need to import.

Requires the array module (or
NumPy for advanced arrays).

Feature List Array
Usage General-purpose programming.

More useful in numeric and
scientific calculations.

Speed Slightly slower for numeric operations.

Faster and more memory efficient
for numbers.

Example list1 = [1, "hello", 3.5, True] arr.array('i', [1, 2, 3, 4, 5])

4. Creating Arrays in Python
Using array module
import array as arr

# Create an integer array
numbers = arr.array('i', [1, 2, 3, 4, 5])
print(numbers)
Explanation:
 'i' → type code (for integer).
 Other type codes:
o 'i' → int
o 'f' → float
o 'd' → double

5. Accessing Array Elements
Like lists, use indexing (starts from 0).
print(numbers[0]) # First element
print(numbers[2]) # Third element

6. Adding Elements
 Use .append() to add one element.
 Use .extend() to add multiple elements.
numbers.append(6)
numbers.extend([7, 8])
print(numbers)

7. Removing Elements
 .remove(value) → Removes first occurrence of value.
 .pop(index) → Removes element at given index.
numbers.remove(3)
numbers.pop(1)
print(numbers)

8. Updating Elements
numbers[0] = 10 # Change first element
print(numbers)

9. Looping through Arrays
for num in numbers:
print(num)

10. Basic Operations on Arrays
print(len(numbers)) # Length
print(sum(numbers)) # Sum of elements

print(max(numbers)) # Maximum element
print(min(numbers)) # Minimum element


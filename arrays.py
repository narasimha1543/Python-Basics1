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

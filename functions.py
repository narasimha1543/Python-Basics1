#FUNCTIONS:
#syntax:
# def function_name(parameters):
    #function body  code
#     return value #optional
# function_name()

#example:
# def greet():
#     print("hello world1")
# greet()

# #calling a function:
# def greet():  #function name 
#     print("hello world")
# greet()   #calling a function

# def greet(name,branch):  #function name 
#     print("hello world",name,branch)
# greet("NARASIMHA","CSE AI&ML")  #calling a function
# greet("NARASIMHA","CSE AI&ML")
# greet("NARASIMHA","CSE AI&ML")

#passing parameters & arguments:
#example:
# def greet(name,roll no):  #name = parameter
#     print("hello",name,"your roll no is",roll no)
# greet("narasimha","k7")

#same task without functions:
# name="narasimha"  #here name is input variable(parameter),and "narasimha" is value of parameter(argument).
# print("hello",name)

#types of functions arguments:

#1. Positional Arguments:
#when we pass argumens is the same order as the function parameter, they are called positional arguments.
#here the order(positional) is very important.

# def greet(name,rollno):  #step2: value stores
#     print("hello",name,"your rollno is",rollno)  #step3: excute the line
# greet("narasimha","K7")  #step1: function calling

#2. Keyword Arguments:
#when we pass value or argumens by writing the parameter(variable=value), they are called keyword arguments.
# def greet(rollno,name):
#     print("hello",name,"your rollno is",rollno)
# greet(name="narasimha",rollno="K7")

#3. default arguments:
# # when a parameter has default value(assigning the value in parameter) in the function definition, it becomes a defaultarguments.
# def greet(name="students"):
#     print("hello",name)
# greet()
# greet(name="narasimha")

#4. Variable-Length Arguments:
#sometimes we dont know how many arguments will be passed to a function.
#python provides two special ways to handle this:
# A. *args:(variable length arguments):
# # l=10,20,30,40,50
# def sum1(*list1):
#     sum2=0
#     for i in range(len(list1)):
#         sum2=sum2+list1[i]
#     print(sum2)     #150
#     print(type(list1))  #<class 'tuple'>
# sum1(10,20,30,40,50)

#B.**kwargs:(keyword variale-length arguments):
#collets multiple key=value pair into a dictionary.
# def details(**info):
#     for key,value in info.items():
#         print(key,"=",value)
# details(name="narasimha",rollno="K7",branch="CSM")

# def details(**info):
#     for i,j in info.items():
#         print(i,":",j)
# details(name="narasimha",rollno="K7",branch="CSM")

#scope of the variable:
x=10 #global variable
# def
# var1():
#     y=5 #local variable
#     print('inside var1 function',x,)
# var1()
# def var2():
# #         print('inside var2 function',x,)
# # var2()
# # print('outside function',x,)
# #lambda fuctions:
# #normal function
# def sqe(a):
#       print(a*a)
# sqe(5)

# #lambda function
# squ=lambda x:x*x
# print(squ(5))


Functions in Python
1. Defining a Function
A function is a block of code that performs a specific task.
It allows us to group instructions together and reuse them whenever needed.
Instead of writing the same code again and again, we just define a function once and call it
whenever required.
🔹 Defining a Function
Definition: Defining a function means creating it using the def keyword.
 We give the function a name.
 We can give it parameters (inputs).
 Inside it, we write the code that will run when the function is called.
Syntax:
def function_name(parameters):
# function body
return value # (optional)
example:
def greet():
print("Hello, Welcome to Python!")

2. Calling a Function
📘 Calling a Function – Definition
Calling a function means telling Python to run the code inside a function by using its name
followed by parentheses ().
 If the function needs input (parameters), we provide values (arguments) inside the
parentheses.
 When we call a function, Python jumps to the function, executes its code, and then
comes back to continue the program.

def greet():
print("Hello, Welcome to Python!")

greet() # calling
# Output: Hello, Welcome to Python!
📍 Key Point: Function must be defined before it is called.

3. Passing Parameters & Arguments
 Parameter → A variable declared inside the function definition. It acts like an empty
container waiting to receive a value.
 Argument → The actual value you pass into the function when calling it. It fills the
container (parameter).
def greet(name): # name is parameter
print("Hello", name)

greet("Nandan") # "Nandan" is argument

📘 Types of Function Arguments
A. Positional Arguments
When we pass arguments in the same order as the function parameters, they are called
positional arguments.
Here, the position (order) is very important. If you change the order, the result will also change.
def student(name, age):
print(name, "is", age, "years old")

student("Ravi", 20) # Correct
# student(20, "Ravi") → Wrong order

B. Keyword Arguments
When we pass values by writing the parameter name = value, they are called keyword
arguments.
Here, order doesn’t matter, because Python knows which value belongs to which parameter. def
def student(name, age):
print(name, "is", age, "years old")

student(age=22, name="Anjali")
👉Output: Anjali is 22 years old

C. Default Arguments
When a parameter has a default value in the function definition, it becomes a default
argument.
If no argument is given during the call, the default value is used.
If an argument is given, it overrides the default.
def greet(name="Student"):
print("Hello", name)

greet() # Output: Hello Student
greet("Ravi") # Output: Hello Ravi

D. Variable-Length Arguments
Sometimes we don’t know how many arguments will be passed to a function.
Python provides two special ways to handle this:
*args → (Non-keyword variable-length arguments)
 Collects multiple values into a tuple.

def add(*numbers):
print(sum(numbers))

add(10, 20, 30) # Output: 60
 **kwargs → (Keyword variable-length arguments)
 Collects multiple key=value pairs into a dictionary.
def details(**info):
for key, value in info.items():
print(key, ":", value)

details(name="Ravi", age=20, course="Python")
Can a Function Have Both *args and **kwargs?
✅Yes, a function in Python can have both *args and **kwargs together.
 *args → collects extra positional arguments into a tuple.
 **kwargs → collects extra keyword arguments into a dictionary.
When both are used, the function can accept any number of positional arguments and any
number of keyword arguments at the same time.

📘 Scope of Variables
🔹 Definition of Scope
The scope of a variable means the part of the program where that variable can be accessed or
used.
In Python, variables can be local or global, depending on where they are created.
Local Variable
A variable declared inside a function is called a local variable.
 It exists only while the function is running.
 It cannot be used outside that function.

Global Variable
A variable declared outside all functions is called a global variable.
 It can be accessed anywhere in the program (inside or outside functions).
x = 10 # global variable

def test():
y = 5 # local variable
print("Inside function:", x, y)

test()
print("Outside function:", x)

📘 Recursive Functions
Recursion is when a function calls itself to solve a smaller part of the same problem.
Think: “I’ll solve this by asking a smaller version of the same question.”
Two parts every recursive function needs:
1. Base case — the simplest input you know the answer to (so recursion stops).
2. Recursive case — how to reduce the problem and call the same function on the smaller
problem.
Short rule: Check base case → otherwise break the problem into smaller part(s) and call the
function on them → combine results and return.
2) Why use recursion? When to use it
 Natural for problems defined in terms of smaller subproblems (factorials, tree traversals,
divide-and-conquer like binary search, etc.).
 Makes code short and expressive for certain problems.
 But recursion can be slower or use more memory (call stack) for large inputs.

3) The best simple example: factorial
Definition: n! = n * (n-1) * (n-2) * ... * 1 and 0! = 1.
Recursive idea:
 Base case: 0! = 1 (or 1! = 1)
 Recursive case: n! = n * (n-1)!
Python code
def factorial(n):
if n == 0: # base case
return 1
else:
return n * factorial(n - 1) # recursive call
4) Step-by-step trace of factorial(4)
Explain by writing the calls and returns (call stack):
Call sequence (what happens first):
factorial(4)
-> needs factorial(3)
-> needs factorial(2)
-> needs factorial(1)
-> needs factorial(0)
-> base case: return 1
-> factorial(1) returns 1 * 1 = 1
-> factorial(2) returns 2 * 1 = 2
-> factorial(3) returns 3 * 2 = 6
-> factorial(4) returns 4 * 6 = 24
Call stack view (top = current active call):
[ active: factorial(4) ]

[ factorial(3) ]
[ factorial(2) ]
[ factorial(1) ]
[ factorial(0) ] <-- base case returns 1
Then return up the stack multiplying at each step.

📘 Anonymous (Lambda) Functions
One-line functions without def.
square = lambda x: x*x
print(square(5)) # 25

📘 Higher Order Functions
Python provides some very powerful built-in higher-order functions that make it easier to
process collections (like lists, tuples).
The three most common ones are:
✅map()
✅filter()
✅reduce() (in functools module
map()
map() applies a function to each element of a sequence (list, tuple, etc.) and returns a new
sequence (iterator).
👉Think: “Do this function to every element in the list.”
Syntax: map(function, iterable)
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares) # [1, 4, 9, 16]

filter()
filter() selects elements from a sequence that satisfy a condition (True/False).
👉Think: “Pick only those elements that pass the test.”
Syntax:
filter(function, iterable)

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x%2==0, nums))
print(evens) # [2, 4]
reduce()
reduce() is in the functools module. It applies a function cumulatively to the elements of a
sequence, reducing it to a single value.
Syntax:
from functools import reduce
reduce(function, iterable)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Add all numbers together
result = reduce(lambda x, y: x + y, numbers)
print(result) # 15

🔹 Functions Practice Problems in Python
✅1. Basic Level (for very beginners)
👉Goal: Learn to define and call a function.
1. Write a function to print "Hello, World!".
2. Write a function that takes a name as input and prints "Hello, <name>".
3. Write a function that prints the sum of two fixed numbers (e.g., 10 + 20).
4. Write a function to check if a number is even or odd.
5. Write a function to return the square of a number.

✅2. Medium Level (parameters, return values, small logic)
👉Goal: Learn arguments, return, conditions, loops inside functions.
1. Write a function that takes two numbers and returns their sum.
2. Write a function that takes a number n and returns the factorial (using a loop).
3. Write a function that takes a list of numbers and returns the largest number.
4. Write a function that takes a list of numbers and returns a new list with only even
numbers.
5. Write a function that takes a string and returns the number of vowels in it.
💻Example (Medium level – Factorial with loop):
def factorial(n):
result = 1
for i in range(1, n+1):
result *= i
return result

print(factorial(5)) # 120

✅3. Hard Level (recursion, higher-order functions, nested logic)
👉Goal: Learn **recursion, *args, kwargs, higher-order functions, problem-solving.
1. Write a recursive function to find the factorial of a number.
2. Write a recursive function to generate the Fibonacci sequence up to n terms.
3. Write a function that takes a list of numbers and uses map() to return their squares.
4. Write a function that uses filter() to keep only prime numbers from a list.
5. Write a function that uses reduce() to calculate the product of all numbers in a list.
6. Write a recursive function to calculate the sum of digits of a number.
7. Write a function that accepts any number of arguments (*args) and returns their sum.
8. Write a function that counts the frequency of each word in a sentence (use dictionary
inside function).
💻Example (Hard level – Fibonacci Recursion):
def fibonacci(n):
if n <= 1:
return n
else:
return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5





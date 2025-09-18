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
#         print('inside var2 function',x,)
# var2()
# print('outside function',x,)
#lambda fuctions:
#normal function
def sqe(a):
      print(a*a)
sqe(5)

#lmbda function
squ=lambda x:x*x
print(squ(5))


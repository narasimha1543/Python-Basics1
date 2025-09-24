# om shree laxmi narasimhaya namaha
# error handling:

#  types of error handling:

# 1.compile-time error:
# error that happens when the code is not written correctly (wrong syntax).

# 2. logical error:
# errors when the program runs but gives wrong output because the logic is wrong.

# 3. runtime error:
# error happens whe the program is running.

# types of exception in python:
# 1. Zerodivision error:
# 2.value error:
# 3. index error:
# 4.key error:
# 5. type error:
# 6. file not fount error:
# 7.name error:

# 1.zerodivision error:
# it is an exception which divides a number by zero.
# try:
#     a=int(input("enter the numerator: "))
#     b=int(input("enter the dinominator: "))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error:Division by zero is not possible")
    

# try:
#     a=int(input("enter the numerator: "))
#     b=int(input("enter the dinominator: "))
#     c=a//b
#     print(c)
# except ZeroDivisionError:
#     print("Error:Division by zero is not possible")


# try:
#     a=int(input("enter the numerator: "))
#     b=int(input("enter the dinominator: "))
#     c=a%b==0
#     print(c)
# except ZeroDivisionError:
#     print("Error:Division by zero is not possible")


# try:
#     i=2
#     n=int(input("enter the n value:"))
#     if i%n==0:
#         print("yes,number is multiple of",n)
#     else:
#         print("no, number not is multiple of",n)

# except ZeroDivisionError:
#     print("Error:Division by zero is not possible")


# 2. VALUE ERROR:
# it's an exception thet gives as invalid value given.
# try:
#     rollno=int(input("emter the rollno:"))
# except ValueError:
#     print("error: given value is not in the integer datatype")


# 3. index error:
# my_string = "hello"
# try:
#     print(my_string[5])

# except IndexError:
#     print("Error: index is out of range for my_string.")


# 4.key error:

# my_dict = {"name": "narasimha", "age": 18}

# try:
#     value = my_dict["city"]
#     print(value)
# except KeyError:
#     print("The key 'city' does not exist in the dictionary.")


# 5. type error:
# try:
#     list=[10,20,30]
#     sum=list+5
#     print(sum)
# except TypeError:
#     print("invalid type operation.")


# #6. name error:
# try:
#     print(mult)
# except NameError:
#     print("variable not decleared.")

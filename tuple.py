my_tuple=(10,20,30,40,50,60)
print(my_tuple)
print(type(my_tuple))



#creating a tuple:
#empty tuple:
et=()


#tuple with numbers:
n=(1,2,3,4,5,6)


#tuple with string:
s=("A","B","C","a","b","c")


#tuple with mixed datatype:
m=(24,3.14,"A","C",True,"False")


#tuple with single element:
a=10
b=[10]
c=(10)
d=(10,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#accessing element
#tuple uses index values to access an element.
a=  (10,20,30,40)
#i    0  1  2  3
#-i  -4 -3 -2 -1
print(a[0])
print(a[1]) 
print(a[2])
print(a[3])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])


#slicing:
#extracts part of the tuple using start index and end index
#([start index: end index])
a= (10,20,30,40)
#i   0  1  2  3
#-i -4 -3 -2 -1
print(a[1:3])        # (20, 30)
print(a[:2])         # (10, 20)
print(a[-3:-1])      # (20, 30)


#changing the values:
#tuples are immutable so we cannot change the values.
# a= (10,20,30,40)
# a[1]=50            #'tuple' object does not support item assignment
# print(a)



# #append():
# #
# a.append(50)
# print(a)      # 'tuple' object does not support item assignment


#length():
a= (10,20,30,40)
print(len(a))


#max():
a= (10,20,30,40)
print(max(a))


#min():
a= (10,20,30,40)
print(min(a))


#sum():
a= (10,20,30,40)
print(sum(a))


#cancatination:
a= (10,20,30,40)
b=(50,60,70)
c=a+b
print(c)


#repetation:
a= (10,20,30,40)
n=int(input("enter the value:"))
b=a*n
print(b)


#searching and checking:
a= (10,20,30,40)
if 30 in a:
    print('yes it exists')


#not in
if 60 not in a:
    print('no it does not exists')


#index():
a= (10,20,30,40)
print(a.index(10))


#count():
a= (10,20,30,40)
print(a.count(30))

#sorting & reversing is  not applicable to tuple
# 'tuple' object does not support item assignment

#NESTED TUPLE:
#   0  0  1    0  1
t=(10,(20,30),(40,50))
#   0     1      2
print(t[1][1])


















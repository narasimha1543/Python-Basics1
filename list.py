#collection datatypes
# #example
# list1=[10,20,30,40,50]
# fruits=["apple","banana","watermelon"]
# # list2=[10.1,20.2,30.3,40.4,50.5]
# # list3=[True,False,True,False]
# # list4=[10,20.2,"hello",True,"False"]
# # print(list1)
# # print(fruits)
# # print(list2)
# # print(list3)
# # print(list4)

# list1=[10,20,30,40,50]
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])

# list1=[10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])

# #slicing
# list1=[10,20,30,40,50]
# # print(list1[2:4])

# slc1=["prabhas","mahesh babu","allu arjun","jmr","mallareddy"]
# print(slc1[0:5])
# print(slc1[0:4])
# print(slc1[-3])

#adding elements in list:
#append
# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# print(kalkicast)
# kalkicast.append("deesha patani")
# print(kalkicast)

# # #insert:
# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# kalkicast.insert(4,"vijay devarakonda")
# print(kalkicast)

#extending:

# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# kalkicast.extend(["anudeep","mrunal thakur"])
# print(kalkicast)             

#removing element in list:
# #1.remove():
# kalkicast.remove("dipika padukon")
# print(kalkicast)

# #2.pop():
# kalkicast.pop(4)
# print(kalkicast)

# #3.clear():
# kalkicast.clear()
# print(kalkicast)

#changing the elements:
# kalkicast[1]="sandeep reddy vanga"
# print(kalkicast)

#mathematical operations:
#1.concatation:
# a=[1,2]
# b=[3,4]
# c=a+b
# print(c)

# # #repeation:
# a=[1,2]
# n=int(input("enter the n value:"))
# b=a*n
# print(b)

# #searching and checking
# a=[2,4,6,8,10.12,14]
# if 2 in a:
#     print("yes item is present in the list")

#not in operator:
# a=[2,4,6,8,10.12,14]
# if 3 not in a:
#     print("3 is not in list")

# #index():
# a=[2,4,6,8,10.12,14]
# print(a.index(8))

# #count():
# a=[2,4,6,8,8,10,12,14]
# print(a.count(8))

# a=[2,4,6,8,8,8,10,12,14]
# cnt=0
# print(a.count(8))
# for i in range(10):
#     a.append(i)
#     if i ==8:
#         cnt=cnt+1
# print(cnt)

#sorting:
# st=[25,12,5,31,13,18,7,45,8,55,68]   =  #Asending order=5,7,8,12,13,18,25,31,45,55,68
# st.sort()
# print(st)

# st=[25,12,5,31,13,18,7,45,8,55,68]  = #decending order= 68,55,45,31,25,18,13,12,8,7,5
# st.reverse()
# print(st)

# st1=[5,8,7,6,25]
# st1.sort(reverse=True)
# print(st1)

#copying the list
# frd1=["A","C","D","A","D","B","B","C","C","A","A"]
# frd2=frd1.copy()
# frd2[2]="B"
# print(frd2)

#built-in functions with loops:
# st=[25,12,5,31,13,18,7,45,8,55,68]
# #lens():returns the number of elements.
# print(len(st))
# #max():returns the maximum elements from the list.
# print(max(st))
# #min(): returns the minimum element from the list.
# print(min(st))
# #sum():returns the total sum of all numerical elements.
# print(sum(st))

# a="hello world"
# b=a.split()
# print(b)

# # multiple values using input data to the list:
# a=input("enter the multiple values:").split()      # 10 20 30 40
# print(a)   =  #['10', '20', '30', '40'] 

# a=list(map(int,input("enter the multiple values:").split()))      # 10 20 30 40 50
# print(a) 

# b=input("enter the multiple values:").split()
# print(b)

#traversing a list:
# #accessing the element using a loop
# cars=["thar","maruthi800","audi","bmw"]
# for car in cars:
#     print("cars=",car)

# # #using index with loop:
# a=len(cars)
# for i in range(0,a):
#     print("cars=",i,cars[i])


# # # Adding elements using for loop
# list1=[]
# n=int(input("enter the number of list values:"))
# for i in range (0,n):
#   a=input("enter the list value:")
#   list1.append(a)
# print(list1)

# Give the input values to the lists from 0 to 10
# list1=[]
# n=int(input("enter the number of list values:"))
# for i in range ():
#   a=input("enter the list value:")
#   list1.append(a)
# print(list1)

#Sum of  list items = 10 20 30 40 50 without using sum().

# list1=[10,20,30,40,50]
# sum=0
# for i in list1:
#     sum=sum+i 
# print(sum)

# #multiply
# list1=[10,20,30,40,50]
# sum=1
# for i in list1:
#     sum=sum*i 
# print(sum)

# convert ["p","y","t","h","o","n"] to python (list to str):
# list1=["p","y","t","h","o","n"]
# result="".join(list1)
# print(result)

            # (or)

# list1=["y","t","h","o","n"]
# word="p"
# for i in list1:
#     word=word+i
# print(word)

# find the maxmum and minimum numbers from list without using max() and min()

# list1=[7,18,12,31,45,17,10,23,229,227]
# list1.sort()
# list1.sort()
# print(list1)

list1=[7,18,12,31,45,17,10,23,229,227]
#list1=[7,18,12,31,45,17,10,23,229,227]
 #      0  1  2  3  4  5  6  7  8   9
list1.sort()
print(list1)
print("maxmim valy=ue of list:",list1[9])
print("minimum value of the list:",list1[0])

#find the maxmum and minimum numbers from list without using max() and min() and sort().
list1=list(map(int,input("enter the multiple ")))











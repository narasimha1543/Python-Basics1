#sets:
#syntax;
#my_set={element1,element2,element3}

#characterstics of sets:'
#unordered:
#ex: {1,2,3} and {3,2,1} are cosidered the same set.

#unindexed:
  #          you cannot set elements by the index like lists or tuples.set[1]
#ex:
#a={1,2,3}
#print(a[1])   = 'set' object is not subscriptable

#unique values:  duplicate values are automatically removed from the set.
#ex:
#a={1,2,3,3,2,1,1,1,2}
# print(a)    =  {1, 2, 3}


#creating a set:
# s1={1,2,3}
# s2={10,12.5,"hello",True}

#empty set:
# s3={}
# s3=set()
# print(type(s3))   = <class 'set'>

#accessing sets:
#we cannot directly access an element using index but we can access an element using loops.
# a={"rajinikanth","snake king","upendra"}
# for role in a:
#     print(role)

# #adding an element in sets:
# s={12,18,20}
# s.add(25)# adds only single element  in any position
# s.update([34,29])#adds the multiple values in the side
# print(s)

# #deleting the element in set:
# s={34,12,18,20,25,34,29}
# s.remove(34)
# print(s)   =  {18, 20, 25, 12, 29}


#dicard(): removes the element ,but it gives no error if the value is not found in the set.
# s={12,18,20,25,34,29,25}
# s.discard(26)
# print(s)

#pop(): removes the random element from the set.
# s={12,18,20,25,34,29,25}
# s.pop()
# print(s)

# # clear(): removes all the elements from the set.
# s={12,18,20,25,34,29,25}
# s.clear()
# print(s)

# #mathametical operations in set:
# #union"|":
a={1,2,3}
b={4,5,6}
print(a|b)

#intersection"∩"="&":
a={1,2,3}
b={4,5,6}
print(a&b)

#diferencec# a={1,2,3,4}
b={3,4,5,6}
print(a-b)
print(b-a)

#symmetric difference"Δ"="^": removes the common elements from the lists but prints only the first sets values.
a={1,2,3,4}
b={3,4,5,6}
print(a^b)

#mathematical operations using functions:
# union
print(a.union(b))
# intersection
print(a.intersection(b))
# diference
print(a.difference(b))
#symmetric difference
print(a.symmetric_difference(b))



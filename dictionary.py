# #dictionary:
# #syntax:
# my_dict={
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4"
# }
# print(my_dict)


# #characterstics of dictionary:
# #key-value pairs:
# #every entry of dictionary's element is a pair:keys and values.
# #{"name":"narasimha"}
# #unique keys:
# #example:
# a={"n":"narasimha","n":"kumar"}
# print(a)

# # keys must be immutable:
# #keys can be(valid keys):integer,flote,string
# my_dict={
#     1:"value1",
#     10.2:"value2",
#     "key3":"value3",
#     "key4":"value4"
# }
# print(my_dict)


# #creating dictionary:
# #normal dictionary:
# biodata={
#     "name":"narasimha",
#     "roll no":"25N3A166K7",
#     "branch":"cse ai-ml",
#     "place":"bhadrachalam"
# }
# print(biodata)


# #dictionar using constructor:
# biodata1 = dict(name= "narasimha", roll_no= "25N3A166K7", branch= "cse ai-ml", place= "bhadrachalam")
# print(biodata1)

# # empty dictionary:
# e_d={}

# #accessing the dictionary:
# #-> to access an element we use key names inside the square brackets[] or we can use get()method.
# biodata={
#     "name":"narasimha",
#     "roll no":"25N3A166K7",
#     "branch":"cse ai-ml",
#     "place":"bhadrachalam"
# }
# # #square brackets[]
# print(biodata["name"])
# print(biodata["roll no"])
# print(biodata["branch"])
# print(biodata["place"])
# print(biodata["age"]) #key error(because the "age" is not created in the dictonary).

# #using get()method:
# print(biodata.get("name"))
# print(biodata.get("roll no"))
# print(biodata.get("branch"))
# print(biodata.get("place"))
# print(biodata.get("age")) #'none' instead of error
 
#adding and updating dictionary:
#adding:you can insert a new key-value pair into a dictionary.
#updating:you can update or change the values using  exsisted elements in the dictionary.

# biodata={
#     "name":"narasimha",
#     "roll no":"25N3A166K7",
#     "branch":"cse ai-ml",
#     "place":"bhadrachalam"
# }
# #adding
# biodata["age"] = 18   # ADDING THE NEW KEYS AND VALUES
# print(biodata)

# #updating
# biodata["place"]="hyderabad"  # CHANGING OR UPDATING THE EXSISTED KEY'S VALUE
# print(biodata)

#removing in dictionary:
#python gives multiple ways to delete items from a dictionary.
#pop(),popitem(),clear(),del()(delete).
# biodata={
#     "name":"narasimha",
#     "roll no":"25N3A166K7",
#     "branch":"cse ai-ml",
#     "place":"bhadrachalam",
#     "role":"mlrd_student"
# }
# #pop():  removes the key vlue
# biodata.pop("roll no")
# print(biodata)

# #popitem():  removes te last inserterd item from the dictionary.
# biodata.popitem()
# print(biodata)

# #del(delete):  deletes te keys from dictionary.
# del biodata["branch"]
# print(biodata)

# #clear():   removes every item from the dictionary.
# biodata.clear()
# print(biodata)

#dictionary methods:
#methods allow you to access dictionary data easily.
#keys(),values(),items()
#
biodata={
    "name":"narasimha",
    "roll no":"25N3A166K7",
    "branch":"cse ai-ml",
    "place":"bhadrachalam",
    "role":"software_developer"
}
#keys():it prints only the keys of dictionary
print(biodata.keys())

#values(): it prints only the values of the dictionary.
print(biodata.values())

#item(): it prints both keys and values of the dictionary.
print(biodata.items())

#updating update():  update the multiple values
biodata.update({"role":"web developer","place":"hyderabad"})
print(biodata)

#loops for dictionary:

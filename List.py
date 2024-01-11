'''
list is mutable data type
store different types of elements like int,string,float,complex,boolean
it allows duplicate values
it allows indexing
we store list values in []

Methods:

Append
extend
count
remove
pop
insert
index

we can do slicing of the list by using above methods.

'''

lst1 = [1,2,3,4,5,"Chaitanya"]
# print(lst1[0])

lst2 = [1,1,1,2,3,4,5,"Chaitanya"]
# #lst2.append(9)
# print(lst2)

# #lst2.extend([9,10,21])
# print(lst2)

# print(lst2.count(1))

# lst2.remove(5)
# print(lst2)

# lst2.pop(0)
# print(lst2)

lst2.insert(2,"Kommi")
print(lst2)

print(lst2.index("Kommi"))
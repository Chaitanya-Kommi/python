'''
In this data will store in flower brackets{ }
This doesn't allow duplicates
In this no index and values stored in un ordered

set methods:
add
update
pop
remove

set operators:
union
interaction
difference
issubset
issuperset
'''

# s = {1,2,3,4,5,6}
# print(s)
# s.add(7)
# print(s)
# s.update({8,9,10,10,10})
# print(s)
# s.pop()
# print(s)
# s.remove(10)
# print(s)

set1 = {11,12,13}
set2 = {13,14,15}
print(set1.union(set2))

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
'''
Dictionary key should be immutable and value can be mutable
In this data should be store in key value pair
In this keys should be unique
Key will act as index
In this data will store in flower brackets{ }
we cannot do slicing in dictionary

Methods:

get
update
values
keys
item

'''
a = {"name":"chaitanya"}
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
a.update({12:24,32:35})
print(a)
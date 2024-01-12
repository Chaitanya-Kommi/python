'''
We can any number of objects for class
Memory will be allocated when object is created

Syntax:

objectname = classname()

Example:

class a():
b = a():


By using object we can access the methods and variables of a class

Syntax:
objectname.method()
objectname.variable()

'''

class chaitanya():
    a = 2
    def func1(self):
        print(self.a)

obj1 = chaitanya()

obj1.func1() # // calling by using function name
print(obj1.a) # calling by using variable name
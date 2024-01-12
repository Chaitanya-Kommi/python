'''
Properties getting from parent to child is known as inheritance

Types of inheritance:

single inheritance
muiti level inheritance
multiple inheritance
Hirearchy inheritance

'''

# Single Inheritance:

# class parent():
#     def func1(self):
#         print("I am parent")
# class child(parent):
#     def func2(self):
#         print("I am child")

# obj1 = child()
# obj1.func1()
# obj1.func2()

# multilevl Inheritance

# class grandfather():
#     def func1(self):
#         print("I am grandfather")
# class parent(grandfather):
#     def func2(self):
#         print("I am parent")
# class child(parent):
#     def func3(self):
#         print("I am child")

# obj1 = child()
# obj1.func1()
# obj1.func2()
# obj1.func3()

# multiple inheritance

# class mother():
#     def func1(self):
#         print("I am mother")
# class father():
#     def func2(self):
#         print("I am father")
# class child(mother,father):
#     def func3(self):
#         print("I am child")

# obj1 = child()
# obj1.func1()
# obj1.func2()
# obj1.func3()

# Hirearchy inheritance

class parent():
    def func1(self):
        print("I am parent")
class child(parent):
    def func2(self):
        print("I am child")
class child1(parent):
    def func3(self):
        print("I am child1")

obj1 = child()
obj1.func1()
obj1.func2()

obj2 = child1()
obj2.func1()
obj2.func3()

'''
interupting normal execution of a code is called error (or) exeception

we will handle this by using error handling.

To over come that error handling we will use below blocks:

try
except
else
finally

'''
a = 1
# print(b)

# try:
#     print(b)
# except:
#     print("There is no variable type b")
# else:
#     print("Hello")
# finally:
#     print("Welcome to python")

try:
    print("a"+3)
except TypeError:
    print("type error")
except ValueError:
    print("value error")
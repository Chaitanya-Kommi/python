'''
function is known as block of code
if we want to run the block of code we will call that function

'''

def chaitanya():
    print("Hello world")
    def Kommi():
        print("Welcome to python")
        def bhanu():
            print("This is your tutor bhanu")
        bhanu()
    Kommi()
chaitanya()

# parameters and arguments

def func(a,b,c):
    print("This is function",a,b,c)
func(1,2,3)

# oribitary arguments

def func1(*a):
    print("This is function",a)
func1(1,2)

# keyword arguments

def func2(**a):
    print("This is function",a)
func2(a=1,b=2)


# Calling functions in another file

def addition(a,b):
    print(a+b)
def subraction(a,b):
    print(a-b)
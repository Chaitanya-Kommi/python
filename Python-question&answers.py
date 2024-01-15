#wite a program to calculate a length of a string

a = "Welcome to python learning"
# print(len(a))

def string_io(st):
    count = 0
    for char in st:
        count+=1
    return count
print(string_io(a))

#finding vowels in a given word

vowels = ['a','e','i','o','u']
word = "chaitanya"
count = 0
for character in word:
    if character in vowels:
     count += 1
print(count)

#Reversing a string

name = "chaitanya"
print(name[::-1])
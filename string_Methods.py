'''
String is a collection of characters

we can define a string by using single quotes(' '), double quotes(" "), and triple quotes(''' ''').

Ex: 
 a = 'Hello'
 b = "Hello"
 c = "'Hello"'

Methods:

upper
lower
endswith
startswith
replace
find
index
count
remove prefix
remove suffix
split
strip
rstrip
lstrip

'''
a = "Hello"
print(a.upper())

b = "Hello"
print(b.lower())

c = "Chaitanya Kommi"
print(c.endswith("i"))

d = "Chaitanya Kommi"
print(d.startswith("C"))

e = "Chaitanya Kommi"
print(e.replace("Kommi","k"))

g = "Hello"
print(g.index("H"))
print(g.find("k"))

f = "Python"
print(f.count("p"))

h = "Python programming"
print(h.removeprefix("Python"))
print(h.removesuffix("programming"))

i = "Python programming"
print(i.split())

j = "   python programming   "
print(j.lstrip())
print(j.rstrip())
print(j.strip())
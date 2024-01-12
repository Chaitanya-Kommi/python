'''
Doing crud operations in python is called file handling

modes:

r - read
w - write (truncate)
a - append
r+ - read/write
w+ - write/read (truncate)

'''

# kommi = open('demofilehandlingfile', mode='r')
# print(kommi.read())
# kommi.close()

kommi = open('demofilehandlingfile', mode='w+')
kommi.write(" Hello everyone")
kommi.seek(0)
print(kommi.read())
kommi.close()
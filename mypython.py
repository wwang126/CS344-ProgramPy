import random

#Open/Create files
f1 = open("file1.txt","w+")
f2 = open("file2.txt","w+")
f3 = open("file3.txt","w+")

#get random values from 1 to 42 inclusive
x = random.randrange(1,43)
y = random.randrange(1,43)
z = x * y
print(x)
print(y)
print(z)

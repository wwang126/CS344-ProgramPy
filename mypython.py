import random
import string

#Create random strings
#get string 1
f1str = ""
for j in range(0,10):
    i = random.randrange(97,123)
    char = chr(i)
    f1str += char
print(f1str, end= "")
#get string 2
f2str = ""
for j in range(0,10):
    i = random.randrange(97,123)
    char = chr(i)
    f2str += char
print(f2str)
#get string 3
f3str = ""
for j in range(0,10):
    i = random.randrange(97,123)
    char = chr(i)
    f3str += char
print(f3str)


#Open/Create file1
f1 = open("file1.txt","w+")
#Open/Create file1
f2 = open("file2.txt","w+")
#Open/Create file1
f3 = open("file3.txt","w+")

#get random values from 1 to 42 inclusive
x = random.randrange(1,43)
y = random.randrange(1,43)
z = x * y
print(x)
print(y)
print(z)

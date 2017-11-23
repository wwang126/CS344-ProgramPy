import random
import string

#Create random strings
#get string 1
f1str = ""
for j in range(0,10):
    i = random.randrange(97,123)
    char = chr(i)
    f1str += char
#Add new line character
f1str += "\n"
#Suppress print new line
print(f1str, end= "")
#get string 2
f2str = ""
for j in range(0,10):
    i = random.randrange(97,123)
    char = chr(i)
    f2str += char
#Add new line character
f2str += "\n"
#Suppress print new line
print(f2str, end = "")
#get string 3
f3str = ""
for j in range(0,10):
    i = random.randrange(97,123)
    char = chr(i)
    f3str += char
#Add new line character
f3str += "\n"
#Suppress print new line
print(f3str, end = "")


#Open/Create file1
f1 = open("file1.txt","w+")
#Write into file1
f1.write(f1str);
#Close file1
f1.close()
#Open/Create file2
f2 = open("file2.txt","w+")
#Write into file1
f2.write(f2str);
#Close file1
f2.close()
#Open/Create file3
f3 = open("file3.txt","w+")
#Write into file1
f3.write(f3str);
#Close file1
f3.close()

#get random values from 1 to 42 inclusive
x = random.randrange(1,43)
y = random.randrange(1,43)
z = x * y
print(x)
print(y)
print(z)

'''
Created on 04.06.2019

@author: Taavi Kase
'''
import mysql.connector
import os

print("Hello World")
x = 4
print(x)
x = "Sally"
print(x)


cwd = os.getcwd()
print(cwd)

# Python is not type sensitive
s = "awesome"
print("Python is " + s) # String concatinating can be done like this

x = 5
#print(x + s) # Python does not want to add numbers and texts

print()
print("file handling")
print()

#Append to file
filename = "fileTest.txt"
permAppend = "a"
permRead = "r"
permWrite = "w"

# Read file
def readFile(filename):
    f = open(filename, permRead)
    print(f.read())
    f.close()

fileTest = open(filename, permAppend)
fileTest.write("Now there's content in the fileTest\n")
fileTest.close()
readFile(filename)

# Overwrite file
fileTest = open(filename, permWrite)
fileTest.write("New Content\n")
fileTest.close
readFile(filename)

# Bit more appending
fileTest = open(filename, permAppend)
fileTest.write("Now there's content in the fileTest\n")
fileTest.close()

readFile(filename)



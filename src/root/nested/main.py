'''
Created on 04.06.2019

@author: Taavi Kase
'''

print("Hello World")
x = 4
print(x)
x = "Sally"
print(x)

# Python is not type sensitive
s = "awesome"
print("Python is " + s) # String concatinating can be done like this

x = 5
#print(x + s) # Python does not want to add numbers and texts

print
print("file handling")
print

filename = "fileTest.txt"
permAppend = "a"
permRead = "r"
fileTest = open(filename, permAppend)
fileTest.write("Now there's content in the fileTest")
fileTest.close()

fileTest = open(filename, permRead)
print(fileTest.read())

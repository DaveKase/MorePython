'''
Created on 04.06.2019

@author: Taavi Kase
'''
import mysql.connector

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

'''
fileTest = open(filename, permRead)
print(fileTest.read())
fileTest.close
'''
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

hostName = "localhost"
userName="root"
pwd = "root"
pyDb="pyTestDb"

mydb = mysql.connector.connect(host=hostName, user=userName, passwd=pwd, database=pyDb)
print(mydb)


mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE pyTestDb") # Already had that db
#mycursor.execute("SHOW DATABASES")

'''
for db in mycursor:
    print(db)
'''

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") # Already exists

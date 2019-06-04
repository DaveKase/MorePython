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
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") # Already done

"""
Did this already
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
name = "John"
address = "Highway 21"
val = (name, address)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")



sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

"""

mycursor.execute("SELECT * FROM customers")
results = mycursor.fetchall()

for result in results:
    print(result)

mycursor.execute("SELECT name, address FROM customers")
results = mycursor.fetchall()

for result in results:
    print(result)


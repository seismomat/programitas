import mysql.connector

db= mysql.connector.connect(
	host="localhost",
	user="batman",
	passwd="batman",
	database="testdatabase"

)

mycursor= db.cursor()

#mycursor.execute(" CREATE DATABASE testdatabase")

"""
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
"""
# para crear tablas
#mycursor.execute(" CREATE TABLE students ( name VARCHAR(255),age INTEGER(10) )")

# para mostrar las tablas 

"""
mycursor.execute(" SHOW TABLES" )

for tb in mycursor:
	print(tb)
"""
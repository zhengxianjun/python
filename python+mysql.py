#!/usr/bin/python3
#coding=utf-8

#show db version

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()




#!/usr/bin/python3
#coding=utf-8

#create table

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS employee")

# Create table as per requirement
sql = """CREATE TABLE `employee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` char(20) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

cursor.execute(sql)
print("Created table Successfull.")
# disconnect from server
db.close()




#!/usr/bin/python3
#coding=utf-8

#Insert table

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Su', 20, 'M', 5000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

## 再次插入一条记录
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Kobe', 'Bryant', 40, 'M', 8000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
print (sql)
print('Yes, Insert Successfull.')
# disconnect from server
db.close()


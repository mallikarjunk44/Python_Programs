import mariadb

import sys



conn = mariadb.connect(

    user = "root",

    password = "kishmish442001",

    host = "localhost",

    port = 3306,

    database = "employee"

)



name = input("Enter Your Name : ")

phone = input("Enter Your Telephone Number : ")

age = input("Enter Your Age : ")

city = input("Enter your City : ")

sal = input("Enter your salary : ")

dept = input("Enter Your Department : ")



cur = conn.cursor()

conn.autocommit = True



try:

    cur.execute("create table customer(name varchar(255) NOT NULL, phone int,age int,city varchar(255),sal int,dept varchar(255));")

except Exception as y:

    print(y)



insertquery = "insert into customer (name, phone, age, city, sal, dept)values(%s, %s, %s, %s, %s, %s)"

data = [name, phone, age, city, sal, dept]

cur.execute(insertquery, data)



cur.execute("select name, phone, age, sal from customer;")

for (name, phone, age, sal) in cur:

    print("Name: ", {name}, "Age : ", {phone}, "Age : ", {age}, "Salary : ", {sal})
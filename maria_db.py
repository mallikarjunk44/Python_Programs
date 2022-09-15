import mariadb

import sys



conn = mariadb.connect(

    user = "root",

    password = "password",

    host = "localhost",

    port = 3306,

    database = "employee"

)



name = input("Enter your name \n")

while (not name.isalpha() or len(name)<=0 ):

    print(" Not valid")

    name = input("Enter your name \n")





phone = input("Enter your Phone Number \n")

while (not phone.isnumeric() or len(phone)!=10 ):

    print(" Not valid")

    phone = input("Enter your Phone number \n")



age = input("Enter your age \n")

while (not age.isnumeric() or len(age)>3 or len(age)<=0 or int(age)<20):

    print(" Not valid")

    age = input("Enter your age \n")



city = input("Enter your City \n")

while (not city.isalpha() or len(city)<=0 ):

    print(" Not valid")

    city = input("Enter your city \n")
sal = input("Enter your Salary \n")
while (not sal.isnumeric() or len(sal)<=0 or int(sal)<0):
    print(" Not valid")
    sal = input("Enter your salary \n")

dept = input("Enter your Department name \n")
while (not dept.isalpha() or len(dept)<=0 ):
    print(" Not valid")
    dept = input("Enter your Department name \n")

cur = conn.cursor()
conn.autocommit = True

try:
    cur.execute("create table customer(name varchar(255) NOT NULL, phone bigint,age int,city varchar(255),sal int,dept varchar(255));")
except Exception as y:
    print(y)

insertquery = "insert into customer (name, phone, age, city, sal, dept)values(%s, %s, %s, %s, %s, %s)"

data = [name, phone, age, city, sal, dept]

cur.execute(insertquery, data)



cur.execute("select name, phone, age, sal from customer;")

for (name, phone, age, sal) in cur:

    print("Name: ", {name}, "Age : ", {phone}, "Age : ", {age}, "Salary : ", {sal})
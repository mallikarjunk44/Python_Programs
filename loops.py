Name=input("enter your name: ")
if len(Name)<=0:
    print("name is a mandatory field")
else:
    print(Name)
Telephone_no=input("enter your telephone number: ")
while len(Telephone_no)!=10:
    Telephone_no=input("enter the proper telephone number")
print(Telephone_no)
Age=input("enter your age: ")
if int(Age)>=20:
    print(Age)
else:
    print("enter the proper age")
salary=int(input("enter the salary: "))
if int(salary)<=0:
    print("salary cannot be less than 0")
else:
    print(salary)

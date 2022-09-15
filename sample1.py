'''
total_class=200
print("enter the student name")
a=input()
print("enter the number of classes attended by the student")
b=int(input())
if (b//total_class)>=0.75:
    print(a + " is eligible for the exams")
else:
    print(a +" is not eligible for the exams")
    '''
salary=10000
bonus15=salary+(salary*0.15)
bonus10=salary+(salary*0.10)
bunus5=salary+(salary*0.05)
employee=input("enter the employee name")
year=input("enter the year of experience")
if year>=10:
    print("total salary="+bonus15)
elif year>=5 and year<10:
    print("total salary="+bonus10)
    
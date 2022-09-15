import calculate



a=input("Enter your Firstname: ")

b=input("Enter your Lastname: ")

print("Name:{0} {1}".format(a,b))



s=calculate.take_salary()

u=calculate.HRA(s)

v=calculate.DA(s)

w=calculate.Bonus(s)



totalsal=float(s)+float(u)+float(v)+float(w)

print("Your Total salary =",totalsal)
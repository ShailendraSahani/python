name=input("Enter the name of Employee :")
salary = eval(input('Enter salary: '))
if salary <=500000:
    taxamt=0.05*salary
elif salary <=600000:
    taxamt=0.07* salary
elif salary <=700000:
    taxamt =0.08*salary
else:
    taxamt =0.10*salary
print("Name: ", name, "Salary :", salary, "Tax :", taxamt)

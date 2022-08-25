x=y=0
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
if(x>y):
    x,y=y,x #swap (interchange) values
    print("The larger number is : ",y)
    print("The smaller number is : ",x)
else:
    print("The larger number is : ",y)
    print("The smaller number is : ",x)
    

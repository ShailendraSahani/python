num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
print("1.Calculate sum")
print("2.Calculate product")
choice = int(input("Enter your choice 1 or 2): "))
if (choice == 1):
    sum = num1+num2+num3
    print("Sum of three numbers are :", sum)
else:
    product = num1*num2*num3
    print("Product of three numbers are : ",product )
    

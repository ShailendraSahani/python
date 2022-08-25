# Program to check divisibility of a number
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
remainder = num1%num2
if remainder == 0:
    print("First number is divisible by second number")
else:
    print("First number is not divisible by second number")

# Program to calculate area of a triangle using Heron's formula
side1 = float(input("Enter first side of a triangle : "))
side2 = float(input("Enter second side of a triangle : "))
side3 = float(input("Enter third side of a triangle : "))

s=(side1+side2+side3)/2
area =(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("Area of a triangle is :", area)

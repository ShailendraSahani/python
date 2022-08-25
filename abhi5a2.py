# Take a number from the user and print its absolute value.
num = eval(input("Enter a number: "))
print('|',num,'|=', (-num if num < 0 else num))

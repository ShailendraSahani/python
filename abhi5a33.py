num = int(input("Enter any number:"))
# print number is always greater than 1
if num > 1:
    for i in range (2, num):
        if (num % 1) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

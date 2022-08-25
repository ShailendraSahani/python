num = int(input("Enter any number : "))
count= 1
sum_even=sum_odd=0
while (count<=num):
    if (count% 2) ==0:
        sum_even += count
    else:
        sum_odd += count
    count += 1
print("Sum of all even numbers up to ",num,"is",sum_even)
print("Sum of all odd numbers up to ",num,"is",sum_odd)

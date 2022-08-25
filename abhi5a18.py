count_emp = 0
while(count_emp <3):
    hours = int(input("Hours :"))
    rate = float(input("Rate :"))
    pay = hours * rate
    print("Pay is Rs. ", pay)
    count_emp = count_emp +1
print( "All employees processed" )

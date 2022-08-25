# Program to convert the time given in minutes in hours and minutes
time = int(input("Enter time in minutes:"))
hours = time/60
minutes = time%60
print("Hours : ",round(hours))
print("Minutes :",minutes)

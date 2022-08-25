my_list=[]
print("Enter list of five integers")
for i in range(5):
    print("Enter integer",i)
    userinput=int(input())
    my_list.append(userinput)
print("The list is:",my_list)
length=len(my_list)
element=int(input("Enter element:"))
c=0
for i in range(0,length-1):
    if element==my_list[i]:
        c+=1
if c == 0:
    print(element,"not found in a given list")
else:
    print(element,"has frequency as",c,"in given list")

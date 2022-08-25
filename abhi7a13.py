list_of_elements=[14, 12, 18, 19, 13, 17]
print("list of items is", list_of_elements)
x=int(input("Enter number to search:"))
found=False
for i in range(len(list_of_elements)):
    if(list_of_elements[i]==x):
        found=True
        print("%d found at %dth position"%(x,i))
        break
    if(found==False):
        print("%d is not in list"%x)

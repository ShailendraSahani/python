items=[2,8,9,12,17]
print("list of items is",items)
x=int(input("enter item to search:"))
i=flag=0
while i <len (items):
    if items[i]==x:
        flag=1
        break
    i=i+1
    if flag==1:
        print(x,"found at position:",i)
    else:
        print(x,"not found in a list")

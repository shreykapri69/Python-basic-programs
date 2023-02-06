#WAP to print even and odd numbers in different list
evenlst=[]
oddlst=[]
a=[]
x=int(input("Enter the size of list: "))
for i in range(x):
    b=int(input("Enter the elements: "))
    a.append(b)
for j in a:
    if (j%2==0):
        evenlst.append(j)
    else:
        oddlst.append(j)
print("Total elements= ",a)
print("Even list is: ",evenlst)
print("Odd list is: ",oddlst)

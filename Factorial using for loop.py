#Factorial using for loop
a=int(input("Enter a number: "))
i=1
f=1
for i in range(1,a+1):
    f=f*(i)
    i=i+1   
print(f)

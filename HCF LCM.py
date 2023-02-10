#To find the HCF & LCM
x=int(input("Enter 1st no. "))
y=int(input("Enter 2nd no. "))
if x>y :
    smaller=y
else:
    smaller=x
for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
        hcf=i
lcm=x*y /hcf
print("HCF",hcf)
print("LCM",lcm)

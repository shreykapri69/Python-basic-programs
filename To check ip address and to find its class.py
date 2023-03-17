#Valid ip address
#Class

ip=input("Enter the IP address: ")
ip2=ip.split(".")
print(ip2)

if int(ip2[0])<=127:
    print("Class A")
elif int(ip2[0])>=128 and int(ip2[0])<=191:
    print("Class B")
elif int(ip2[0])>=192 and int(ip2[0])<=223:
    print("Class C")
elif int(ip2[0])>=224 and int(ip2[0])<=239:
    print("Class D")
elif int(ip2[0])>=240 and int(ip2[0])<=255:
    print("Class E")
else:
    print("Please enter some valid IP address")

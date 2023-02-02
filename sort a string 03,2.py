#Program to sort a string alphabetically and sort item's length wise
x=input("Enter string: ")
dic={}
for i in x:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1


for j in dic:
    print(j, dic[j])
print("Sorted alphabetically: ",sorted(dic.items()))
print("Sorted item wise: ",sorted(dic.items(), key=lambda x:x[1]))




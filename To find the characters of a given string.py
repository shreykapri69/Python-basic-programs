#To find the legth of characters of the given string
str="Akshat Johri 652"
char=0
for i in str:
    if i.isalpha():
        char=char+1
dict={str:char}
print(dict)




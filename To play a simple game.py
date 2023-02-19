#To play a simple game
a=int(input("Enter any num.: "))
import random
b= random.randrange(a+1)
if a==b:
    print("U WON")
else:
    print("U LOSE")

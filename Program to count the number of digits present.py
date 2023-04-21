#Program to find the number of digits present in the string
num = 6285
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))

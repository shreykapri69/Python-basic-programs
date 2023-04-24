#Program to convert Miles into kilometers
mile = float(input("Enter value in Miles: "))

conv_fac = 0.621371

#Calculate kilometers
km = mile / conv_fac
print("%0.2f miles is equal to %0.2f km" %(mile,km))

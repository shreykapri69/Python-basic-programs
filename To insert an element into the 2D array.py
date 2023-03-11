# Program to insert the element into the 2D array.  
from array import*  
arr1 = [[1, 2, 3, 4], [8, 9, 10, 12]]   
print("Before inserting the array elements: ")  
print(arr1)   

arr1.insert(1, [5, 6, 7, 8]) 
print("After inserting the array elements: ")  
for i in arr1: 
    for j in i: 
        print(j, end = " ") # print inserted elements.  

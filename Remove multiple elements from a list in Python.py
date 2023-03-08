list1 = [11, 5, 17, 18, 23, 50]


for ele in list1:
	if ele % 2 == 0:
		list1.remove(ele)


print("New list after removing all even numbers: ", list1)

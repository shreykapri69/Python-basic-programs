test_str = 'geeksforgeeks_is_best'


print("The original string is : " + test_str)


res = test_str.replace("_", " ").title().replace(" ", "")


print("The String after changing case : " + str(res))

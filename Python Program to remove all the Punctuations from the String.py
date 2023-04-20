#Program to remove all the punctuations.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter a string: ")

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char


print("String after Removing Punctuations: ", no_punct)

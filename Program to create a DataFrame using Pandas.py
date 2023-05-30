#Program to create a dataframe using Pandas
import pandas as pd
   
# Calling DataFrame constructor
df = pd.DataFrame()
print(df)
 
lst = ['Akshat', 'Johri', 'studies', 'in', 
            'Sharda', 'University']
   
df = pd.DataFrame(lst)
print(df)

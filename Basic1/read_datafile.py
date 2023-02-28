# The problem here is the datafile have a lot of spaceses in an unstructured way. 
# So how to get python reading text file with an undefined number of whitespaces as column separator


import pandas as pd

# df = pd.read_csv("my_datafile.txt", sep=r"\s{1,}", engine="python", header=None)  # Undefined data will appere as None
# print(df)

df = pd.read_csv("my_datafile.txt", delim_whitespace=True, header=None) # Undefined data will appere as NaN
print(df)

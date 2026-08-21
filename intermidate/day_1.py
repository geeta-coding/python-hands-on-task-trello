import pandas as pd 

df = pd.read_excel("files/students.xlsx")
# print(df.head())
# print(df.shape)
print(df.dtypes)
print()
print("="*50)
print()
ss = pd.read_excel("files/patient.xlsx")
print(ss.head())

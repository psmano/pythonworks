import pandas as pd

df1 = pd.read_excel('excel1.xlsx')
df2 = pd.read_excel('excel2.xlsx')

difference = df1[df1 != df2]
print(difference)
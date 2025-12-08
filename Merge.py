
import pandas as pd

df1 = pd.read_excel('NRA FMCG HC instruction W-91.xlsb', sheet_name='INSTRUCTION', engine='pyxlsb')

print("Rows & Columns in Sheet1:", df1.shape)

df2 = pd.read_excel('NRA FMCG HC instruction W-92.xlsb', sheet_name='instruction', engine='pyxlsb')
print("Rows & Columns in Sheet2:", df2.shape)

pd.concat([df1, df2]).to_csv('Merged.csv', index=False, encoding='utf-8-sig')

print("Merged CSV created successfully.")
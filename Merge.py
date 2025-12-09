
import pandas as pd

# Read the Excel File
df1 = pd.read_excel('NRA FMCG HC instruction W-91.xlsb', sheet_name='INSTRUCTION', engine='pyxlsb')

# Print the Rows & Columns
print("Rows & Columns in Sheet1:", df1.shape)

df2 = pd.read_excel('NRA FMCG HC instruction W-92.xlsb', sheet_name='instruction', engine='pyxlsb')

# Print the Rows & Columns
print("Rows & Columns in Sheet2:", df2.shape)

# Merging the Two DataFrames and Exporting o CSV 
pd.concat([df1, df2]).to_csv('Merged_File.csv', index=False, encoding='utf-8-sig')

# Print Successfully Message
print("Merged CSV created successfully.")
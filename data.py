
# Import libraries
import pandas as pd
import os

# Step 1: Read SPECIFIC sheets from Excel files
df1 = pd.read_excel('NRA FMCG HC instruction W-91.xlsb', sheet_name='INSTRUCTION', engine='pyxlsb')  # Sheet1 read karo
# Second file Read the Sheet 
df2 = pd.read_excel('NRA FMCG HC instruction W-92.xlsb', sheet_name='instruction', engine='pyxlsb')

print(f"Rows: {len(df1)}")

print(f"Rows: {len(df2)}")

# Step 2: Merge both Sheets data
merged_df = pd.concat([df1, df2], ignore_index=True)

print("\n MERGED SHEETS DATA:")

print(f"Total Rows: {len(merged_df)}")

# Step 3: Save new CSV file
csv_filename = 'Merged_File_Data.csv'
merged_df.to_csv(csv_filename, 
                index=False, 
                encoding='utf-8-sig')  # Extra Use for Urdu and Arabic Characters
print(f"\n CSV FILE SAVED: {csv_filename}")

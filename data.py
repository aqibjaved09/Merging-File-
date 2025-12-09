
# Import libraries
import pandas as pd
import os

# Step 1: Read SPECIFIC sheets from Excel files
df1 = pd.read_csv('Hair Color Relation with Main Template F-W91-V0.csv')  # Sheet1 read karo
df2 = pd.read_csv('Hair Color Relation with Main Template F-W92-V0.csv')  # Sheet1 read karo
df3 = pd.read_csv('Hair Color Relation with Main Template F-W93-V0.csv')
df4 = pd.read_csv('Hair Color Relation with Main Template F-W94-V0.csv')  # Sheet1 read karo
df5 = pd.read_csv('Hair Color Relation with Main Template F-W95-V0.csv')  # Sheet1 read karo
df6 = pd.read_csv('Hair Color Relation with Main Template F-W96-V0.csv')  # Sheet1 read karo
  # Sheet2 read karo

print(f"Rows: {len(df1)}")

print(f"Rows: {len(df2)}")
print(f"Rows: {len(df3)}")
print(f"Rows: {len(df4)}")
print(f"Rows: {len(df5)}")
print(f"Rows: {len(df6)}")

# Step 2: Merge both Sheets data
merged_df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

print(f"Total Rows of Merging: {len(merged_df)}")

# Step 3: Save new CSV file
csv_filename = 'Merged_File_91_96_Data.csv'
merged_df.to_csv(csv_filename, 
                index=False, 
                encoding='utf-8-sig')  # Extra Use for Urdu and Arabic Characters
print(f"\n CSV FILE SAVED: {csv_filename}")

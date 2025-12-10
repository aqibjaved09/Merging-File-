
# Import libraries
import pandas as pd
import os

# Adding the folder path where Excel files are stored
folder_path = 'D:/E/Tables/DBs/'

# We Read Specific sheets from Excel files
df1 = pd.read_csv(folder_path + 'Hair Color Relation with Main Template F-W91-V0.csv') # Select the Csv 1st sheet
df2 = pd.read_csv(folder_path + 'Hair Color Relation with Main Template F-W92-V0.csv') # Select the Csv 1st sheet
df3 = pd.read_csv(folder_path + 'Hair Color Relation with Main Template F-W93-V0.csv') # Select the Csv 1st sheet
df4 = pd.read_csv(folder_path + 'Hair Color Relation with Main Template F-W94-V0.csv') # Select the Csv 1st sheet
df5 = pd.read_csv(folder_path + 'Hair Color Relation with Main Template F-W95-V0.csv') # Select the Csv 1st sheet
df6 = pd.read_csv(folder_path + 'Hair Color Relation with Main Template F-W96-V0.csv') # Select the Csv 1st sheet
  
# Using to check Rows of each file
print(f"Rows: {len(df1)}") # Checking Rows file 1
print(f"Rows: {len(df2)}") # Checking Rows file 2
print(f"Rows: {len(df3)}") # Checking Rows file 3
print(f"Rows: {len(df4)}") # Checking Rows file 4
print(f"Rows: {len(df5)}") # Checking Rows file 5
print(f"Rows: {len(df6)}") # Checking Rows file 6


# Merge both Sheets data
merged_df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

print(f"Total Rows of Merging: {len(merged_df)}")

# Save new CSV file
csv_filename = 'Merged_File_91_96_Data.csv'
merged_df.to_csv(csv_filename, 
                index=False, 
                encoding='utf-8-sig')  # Extra Use for Urdu and Arabic Characters
print(f"\n CSV FILE SAVED: {csv_filename}")

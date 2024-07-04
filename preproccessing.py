import pandas as pd

# Define the path to your Excel file
excel_file_path = "C:\\Users\\mktad\\Desktop\\E\\master_table_data.xlsx"

# Load the Excel file
df = pd.read_excel(excel_file_path, header=None)

# Initialize an empty list to hold the split rows
split_data = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    cell_value = row[0]  # Assuming the cell to split is in the first column
    split_values = cell_value.split(', ')
    split_data.append(split_values)

# Create a new DataFrame from the split data
split_df = pd.DataFrame(split_data)

# Save the new DataFrame to an Excel file
new_excel_file_path = "C:\\Users\\mktad\\Desktop\\E\\split_columns.xlsx"
split_df.to_excel(new_excel_file_path, index=False, header=False)

print(f"The cell values have been split into columns and saved at {new_excel_file_path} in UTF-8 encoding")

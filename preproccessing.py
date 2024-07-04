import pandas as pd

excel_file_path = "C:\\Users\\mktad\\Desktop\\E\\master_table_data.xlsx"

df = pd.read_excel(excel_file_path, header=None)

split_data = []

for index, row in df.iterrows():
    cell_value = row[0]  # Assuming the cell to split is in the first column
    split_values = cell_value.split(', ')
    split_data.append(split_values)

split_df = pd.DataFrame(split_data)

new_excel_file_path = "C:\\Users\\mktad\\Desktop\\E\\split_columns.xlsx"
split_df.to_excel(new_excel_file_path, index=False, header=False)

print(f"The cell values have been split into columns and saved at {new_excel_file_path} in UTF-8 encoding")

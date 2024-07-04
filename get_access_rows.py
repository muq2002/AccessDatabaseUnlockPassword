import pyodbc
import pandas as pd

# Connect to the Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\mktad\Desktop\E\الأستفسارات.mde'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Function to fetch all rows from a specific table
def fetch_table_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

# Specify the table name you want to export to Excel
table_name = 'master'
table_data = fetch_table_data(cursor, table_name)

# Convert the fetched data into a pandas DataFrame
df = pd.DataFrame(table_data)

# Specify the path to save the Excel file
excel_file_path = 'C:\\Users\\mktad\\Desktop\\E\\master_table_data.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f"Data from table '{table_name}' has been exported to '{excel_file_path}'.")

# Close the connection
cursor.close()
conn.close()
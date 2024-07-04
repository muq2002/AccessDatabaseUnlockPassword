import pyodbc
import pandas as pd

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

table_name = 'master'
table_data = fetch_table_data(cursor, table_name)

df = pd.DataFrame(table_data)

excel_file_path = 'C:\\Users\\mktad\\Desktop\\E\\master_table_data.xlsx'

df.to_excel(excel_file_path, index=False)

print(f"Data from table '{table_name}' has been exported to '{excel_file_path}'.")

cursor.close()
conn.close()
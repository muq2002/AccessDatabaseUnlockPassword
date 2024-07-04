import pyodbc

# Connect to the Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\mktad\Desktop\E\الأستفسارات.mde'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Function to get column information for a specific table
def get_column_info(cursor, table_name):
    columns = []
    for row in cursor.columns(table=table_name):
        column_name = row.column_name
        columns.append(column_name)
    return columns

# Specify the table name you want to retrieve columns for
table_name = 'master'
columns = get_column_info(cursor, table_name)

# Print the columns for the specified table
print(f"Columns for table '{table_name}':")
for column in columns:
    print(f"  - {column}")

# Close the connection
cursor.close()
conn.close()
import pyodbc

# Connect to the Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\mktad\Desktop\E\الأستفسارات.mde'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Function to get all table names
def get_table_names(cursor):
    table_names = []
    for row in cursor.tables(tableType='TABLE'):
        table_name = row.table_name
        if not table_name.startswith('MSys') and not table_name.startswith('~'):
            table_names.append(table_name)
    return table_names

# Get all table names
table_names = get_table_names(cursor)

# Print the table names
print("Table Names in the Database:")
for name in table_names:
    print(name)

# Close the connection
cursor.close()
conn.close()

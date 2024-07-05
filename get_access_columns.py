import pyodbc


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\mktad\Desktop\E\الأستفسارات.mde'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def get_column_info(cursor, table_name):
    columns = []
    for row in cursor.columns(table=table_name):
        column_name = row.column_name
        columns.append(column_name)
    return columns

# Specify the table name you want to retrieve columns for
table_name = 'custtypeind'
columns = get_column_info(cursor, table_name)

print(f"Columns for table '{table_name}':")
for column in columns:
    print(f"  - {column}")


cursor.close()
conn.close()
import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\mktad\Desktop\E\الأستفسارات.mde'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def get_table_names(cursor):
    table_names = []
    for row in cursor.tables(tableType='TABLE'):
        table_name = row.table_name
        if not table_name.startswith('MSys') and not table_name.startswith('~'):
            table_names.append(table_name)
    return table_names

table_names = get_table_names(cursor)

print("Table Names in the Database:")
for name in table_names:
    print(name)

cursor.close()
conn.close()

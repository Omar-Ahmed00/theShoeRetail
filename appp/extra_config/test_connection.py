

import pyodbc

server_name = "depigroup1" 
server_name = "depigroup1" 
database_name = "retail_store" 
username = "omar"  
password = "A1b2c3d4e10&"  

connection_string = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={server_name}.database.windows.net;"
    f"Database={database_name};"
    f"UID={username};"
    f"PWD={password};"
)

try:
    with pyodbc.connect(connection_string) as conn:
        print("Database connection successful!")
except pyodbc.InterfaceError as e:
    print(f"Database connection failed: {e}")

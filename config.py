import os 

server_name = "depigroup1" 
database_name = "retail_store" 
username = "omar"  
password = "A1b2c3d4e10&"  




class Config :  

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A1b2c3d4e10&'  
    SQLALCHEMY_DATABASE_URI = (
    f'mssql+pyodbc://{username}:{password}@{server_name}.database.windows.net:1433/'
    f'{database_name}?driver=ODBC+Driver+18+for+SQL+Server'
)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

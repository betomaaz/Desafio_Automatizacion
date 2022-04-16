import pyodbc

server = 'ANGELICAVACCA'
database = 'tiendpython'
username = 'tiendapython'
password = 'tiendapython'

try:
    conex = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                           server+';DATABASE='+database+';UID='+username+';PWD=' + password)
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

import mysql.connector
import pyodbc
from bd import conex

server = 'ANGELICAVACCA'
database = 'tiendpython'
username = 'tiendapython'
password = 'tiendapython'


class Conexion:

    def abrir(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
        cursor = cnxn.cursor()
        return cursor

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into productos(codigo, precio,nombre) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            with conex.cursor() as cursor:
                sql = "select nombre_pro, precio, stock from Productos where codigo=?;"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        except Exception as e:
            print("Ocurrió un error al consultar: ", e)

    def recuperar_todos(self):
        try:
            with conex.cursor() as cursor:
                sql = "select codigo,nombre_pro, precio, stock from productos"
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print("Ocurrió un error al consultar: ", e)

    def lista_compras(self, datos):
        try:
            with conex.cursor() as cursor:
                sql = "select p.nombre_pro, cantidad, p.precio*cantidad as Total,fecha_compra from compras a inner join clientes b on a.id_cliente = b.id_cliente  left join productos p on a.id_producto = p.id_producto where b.rut=?; "
            cursor.execute(sql, datos)
            return cursor.fetchall()
        except Exception as e:
            print("Ocurrió un error al consultar: ", e)

    def consultaCliente(self, datos):
        try:
            with conex.cursor() as cursor:
                sql = "select nombre, ap_paterno, ap_materno from clientes where rut = ?;"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        except Exception as e:
            print("Ocurrió un error al consultar: ", e)

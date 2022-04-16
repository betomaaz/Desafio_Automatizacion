import mysql.connector


class Conexion:

    def abrir(self):
        conexion = mysql.connector.connect(host="localhost",
                                           user="root",
                                           passwd="",
                                           database="TiendaPython")
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into productos(codigo, precio,nombre) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select nombre_pro, precio, stock from productos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo,nombre_pro, precio, stock from productos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def lista_compras(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select p.nombre_pro, cantidad, p.precio*cantidad,fecha from compras a inner join clientes b on a.id_cliente = b.id_cliente  left join productos p on a.id_producto = p.id_producto where b.rut=%s "
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def consultaCliente(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select nombre, ap_paterno, ap_materno from clientes where rut = %s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

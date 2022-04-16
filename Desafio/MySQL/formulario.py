import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import conexion


class Formulario:
    def __init__(self):
        self.articulo1 = conexion.Conexion()
        self.ventana1 = tk.Tk()
        self.ventana1.title("TiendaPython")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.consulta_por_codigo()
        self.consulta_por_cliente()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Productos")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe2, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigo = tk.StringVar()
        self.entrycodigo = ttk.Entry(
            self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe2, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar()
        self.entrydescripcion = ttk.Entry(
            self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio = tk.StringVar()
        self.entryprecio = ttk.Entry(
            self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.label4 = ttk.Label(self.labelframe2, text="Stock:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.stock = tk.StringVar()
        self.entrystock = ttk.Entry(
            self.labelframe2, textvariable=self.stock, state="readonly")
        self.entrystock.grid(column=1, row=3, padx=4, pady=4)

        self.boton1 = ttk.Button(
            self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(), )
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
            self.stock.set(respuesta[0][2])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información",
                        "No existe un artículo con dicho código")

    def consulta_por_cliente(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Consulta por cliente")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Clientes")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe4, text="Rut:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.rut = tk.StringVar()
        self.entryrut = ttk.Entry(
            self.labelframe4, textvariable=self.rut)
        self.entryrut.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe4, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre = tk.StringVar()
        self.entrynombre = ttk.Entry(
            self.labelframe4, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe4, text="Apellido Paterno:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.app = tk.StringVar()
        self.entryapp = ttk.Entry(
            self.labelframe4, textvariable=self.app, state="readonly")
        self.entryapp.grid(column=1, row=2, padx=4, pady=4)

        self.label4 = ttk.Label(self.labelframe4, text="Apellido Materno:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.apm = tk.StringVar()
        self.entryapm = ttk.Entry(
            self.labelframe4, textvariable=self.apm, state="readonly")
        self.entryapm.grid(column=1, row=3, padx=4, pady=4)

        self.boton1 = ttk.Button(
            self.labelframe4, text="Consultar", command=self.consultar_cliente)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

        self.scrolledtext2 = st.ScrolledText(
            self.labelframe4, width=30, height=10)
        self.scrolledtext2.grid(column=1, row=6, padx=5, pady=5)

    def consultar_cliente(self):
        datos = (self.rut.get(), )
        respuesta = self.articulo1.consultaCliente(datos)
        respuesta2 = self.articulo1.lista_compras(datos)
        if len(respuesta) > 0:
            self.nombre.set(respuesta[0][0])
            self.app.set(respuesta[0][1])
            self.apm.set(respuesta[0][2])
            self.scrolledtext2.delete("1.0", tk.END)
            for fila in respuesta2:
                self.scrolledtext2.insert(tk.END, "Producto:"+str(
                    fila[0])+"\nCantidad:"+str(fila[1])+"\nTotal:"+str(fila[2])+"\nFecha:"+str(fila[3])+"\n\n")
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información",
                        "No existe un cliente con ese rut")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Productos Disponibles")
        self.labelframe3 = ttk.LabelFrame(
            self.pagina3, text="Lista de Productos")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1 = ttk.Button(
            self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1 = st.ScrolledText(
            self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(
                fila[0])+"\nnombre:"+fila[1]+"\nprecio:"+str(fila[2])+"\nstock:"+str(fila[3])+"\n\n")


aplicacion1 = Formulario()

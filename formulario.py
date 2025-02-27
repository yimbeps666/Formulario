import tkinter as tk
from tkinter import messagebox

def guardar():
    campos_faltantes = []
    if not cedula.get():
        campos_faltantes.append("Cédula")
    if not nombres.get():
        campos_faltantes.append("Nombres")
    if not apellidos.get():
        campos_faltantes.append("Apellidos")
    if not telefono.get():
        campos_faltantes.append("Teléfono")
    if not direccion.get():
        campos_faltantes.append("Dirección")
    if not correo.get():
        campos_faltantes.append("Correo Electrónico")

    if campos_faltantes:
        messagebox.showwarning("Campos Faltantes", f"Faltan los siguientes campos: {', '.join(campos_faltantes)}")
    else:
        messagebox.showinfo("Datos Completos", "Datos completos")

def limpiar():
    cedula.set("")
    nombres.set("")
    apellidos.set("")
    telefono.set("")
    direccion.set("")
    correo.set("")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Empleado")

# Variables para almacenar los datos
cedula = tk.StringVar()
nombres = tk.StringVar()
apellidos = tk.StringVar()
telefono = tk.StringVar()
direccion = tk.StringVar()
correo = tk.StringVar()

# Crear los campos de entrada
tk.Label(ventana, text="Cédula:").grid(row=0, column=0)
tk.Entry(ventana, textvariable=cedula).grid(row=0, column=1)

tk.Label(ventana, text="Nombres:").grid(row=1, column=0)
tk.Entry(ventana, textvariable=nombres).grid(row=1, column=1)

tk.Label(ventana, text="Apellidos:").grid(row=2, column=0)
tk.Entry(ventana, textvariable=apellidos).grid(row=2, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=3, column=0)
tk.Entry(ventana, textvariable=telefono).grid(row=3, column=1)

tk.Label(ventana, text="Dirección:").grid(row=4, column=0)
tk.Entry(ventana, textvariable=direccion).grid(row=4, column=1)

tk.Label(ventana, text="Correo Electrónico:").grid(row=5, column=0)
tk.Entry(ventana, textvariable=correo).grid(row=5, column=1)

# Crear los botones
tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, column=0)
tk.Button(ventana, text="Limpiar", command=limpiar).grid(row=6, column=1)

# Iniciar la aplicación
ventana.mainloop()

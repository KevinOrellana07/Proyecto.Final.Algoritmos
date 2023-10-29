import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

clientes_db_file = "clientes.txt"
productos_db_file = "productos.txt"
clientes_id_file = "clientes_id.txt"
productos_id_file = "productos_id.txt"
clientes_db_file = "clientes.txt"
productos_db_file = "productos.txt"
clientes_id_file = "clientes_id.txt"
productos_id_file = "productos_id.txt"

def asignar_cliente_id():
    with open(clientes_id_file, "r") as file:

        cliente_id = int(file.read())
    cliente_id += 1
    with open(clientes_id_file, "w") as file:
        file.write(str(cliente_id))
    return cliente_id

def asignar_producto_id():
    with open(productos_id_file, "r") as file:
        producto_id = int(file.read())
    producto_id += 1
    with open(productos_id_file, "w") as file:
        file.write(str(producto_id))
    return producto_id

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    
    cliente_id = asignar_cliente_id()
    
    with open(clientes_db_file, "a") as file:
        file.write(f"{cliente_id},{nombre},{direccion},{telefono}\n")

def registrar_producto():
    nombre = input("Nombre del producto: ")
    precio = input("Precio del producto: ")
    existencia = input("Existencia del producto: ")
    proveedor = input("Proveedor del producto: ")
    producto_id = asignar_producto_id()
    
    with open(productos_db_file, "a") as file:
        file.write(f"{producto_id},{nombre},{precio},{existencia},{proveedor}\n")

def mostrar_cliente_por_id(cliente_id):
    with open(clientes_db_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if int(parts[0]) == cliente_id:
                print(f"ID: {parts[0]}, Nombre: {parts[1]}, Dirección: {parts[2]}, Teléfono: {parts[3]}")
                return
        print("Cliente no encontrado.")

def mostrar_producto_por_id(producto_id):
    with open(productos_db_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if int(parts[0]) == producto_id:
                print(f"ID: {parts[0]}, Nombre: {parts[1]}, Precio: {parts[2]}, Existencia: {parts[3]}, Proveedor: {parts[4]}")
                return
        print("Producto no encontrado.")

def actualizar_cliente():
    cliente_id = int(input("Ingrese el ID del cliente a actualizar: "))
    
    with open(clientes_db_file, "r") as file:
        lines = file.readlines()

    with open(clientes_db_file, "w") as file:
        for line in lines:
            parts = line.strip().split(",")
            if int(parts[0]) == cliente_id:
                nombre = input("Nuevo nombre: ")
                direccion = input("Nueva dirección: ")
                telefono = input("Nuevo teléfono: ")
                line = f"{cliente_id},{nombre},{direccion},{telefono}\n"
            file.write(line)

def actualizar_producto():
    producto_id = int(input("Ingrese el ID del producto a actualizar: "))
    
    with open(productos_db_file, "r") as file:
        lines = file.readlines()

    with open(productos_db_file, "w") as file:
        for line in lines:
            parts = line.strip().split(",")
            if int(parts[0]) == producto_id:
                nombre = input("Nuevo nombre: ")
                precio = input("Nuevo precio: ")
                existencia = input("Nueva existencia: ")
                proveedor = input("Nuevo proveedor: ")
                line = f"{producto_id},{nombre},{precio},{existencia},{proveedor}\n"
            file.write(line)

def eliminar_cliente():
    cliente_id = int(input("Ingrese el ID del cliente a eliminar: "))
    
    with open(clientes_db_file, "r") as file:
        lines = file.readlines()

    with open(clientes_db_file, "w") as file:
        for line in lines:
            parts = line.strip().split(",")
            if int(parts[0]) != cliente_id:
                file.write(line)

def eliminar_producto():
    producto_id = int(input("Ingrese el ID del producto a eliminar: "))
    
    with open(productos_db_file, "r") as file:
        lines = file.readlines()

    with open(productos_db_file, "w") as file:
        for line in lines:
            parts = line.strip().split(",")
            if int(parts[0]) != producto_id:
                file.write(line)

def enviar_correo():
    servidor_smtp = 'smtp.gmail.com'
    puerto = 587
    usuario = 'ko3645348@gmail.com'
    contrasena = 'hwia ypaa kvze aezp'
    destinatario = input("Ingrese el correo electrónico del destinatario:")
    asunto = 'Informe de ventas'
    cuerpo = 'Por medio de este correo se adjuntan los archivos solicitados.'
    archivo = input("Seleccione el archivo a enviar:")

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(cuerpo, 'plain'))
    adjunto = open(archivo, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((adjunto).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + archivo)

    msg.attach(part)

    servidor = smtplib.SMTP(servidor_smtp, puerto)
    servidor.starttls()
    servidor.login(usuario, contrasena)
    text = msg.as_string()
    servidor.sendmail(usuario, destinatario, text)
    servidor.quit()



# Luego, continuamos con el bucle while y el menú del programa
while True:
    print("\n--- Sistema de Control de Negocio ---")
    print("1. Registrar Cliente")
    print("2. Registrar Producto")
    print("3. Mostrar Cliente por ID")
    print("4. Mostrar Producto por ID")
    print("5. Actualizar Cliente")
    print("6. Actualizar Producto")
    print("7. Eliminar Cliente")
    print("8. Eliminar Producto")
    print("9. Enviar Correo")
    print("10. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        registrar_producto()
    elif opcion == "3":
        cliente_id = int(input("Ingrese el ID del cliente a mostrar: "))
        mostrar_cliente_por_id(cliente_id)
    elif opcion == "4":
        producto_id = int(input("Ingrese el ID del producto a mostrar: "))
        mostrar_producto_por_id(producto_id)
    elif opcion == "5":
        actualizar_cliente()
    elif opcion == "6":
        actualizar_producto()
    elif opcion == "7":
        eliminar_cliente()
    elif opcion == "8":
        eliminar_producto()
    elif opcion == "9":
        enviar_correo()
    elif opcion == "10":
        print("¡Gracias por su preferencia, esperamos que vuelva pronto!")
        break
    else:
        print("Opción no permitida. Por Favor Intente de Nuevo.")

        

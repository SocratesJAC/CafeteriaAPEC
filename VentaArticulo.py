# F. AGREGAR
def agregar_venta(ventas):
    no_factura = input("Ingrese el número de factura: ")
    if no_factura in ventas:
        print("La venta ya existe.")
        return
    empleado = input("Ingrese el empleado: ")
    articulo = input("Ingrese el artículo: ")
    usuario = input("Ingrese el usuario: ")
    fecha_venta = input("Ingrese la fecha de venta: ")
    monto_articulo = float(input("Ingrese el monto del artículo: "))
    unidades_vendidas = int(input("Ingrese las unidades vendidas: "))
    comentario = input("Ingrese un comentario: ")
    estado = input("Ingrese el estado de la venta: ")
    ventas[no_factura] = {"Empleado": empleado, "Artículo": articulo, "Usuario": usuario, "Fecha Venta": fecha_venta, "Monto del artículo": monto_articulo, "Unidades vendidas": unidades_vendidas, "Comentario": comentario, "Estado": estado}
    print("Venta agregada con éxito.")

# F. ELIMINAR
def eliminar_venta(ventas):
    no_factura = input("Ingrese el número de factura de la venta que desea eliminar: ")
    if no_factura in ventas:
        del ventas[no_factura]
        print("Venta eliminada con éxito.")
    else:
        print("La venta no existe.")

# F. VISUALIZAR
def visualizar_ventas(ventas):
    if not ventas:
        print("No hay ventas para mostrar.")
    else:
        print("Listado de Ventas:")
        for no_factura, info in ventas.items():
            print(f"No. Factura: {no_factura}, Empleado: {info['Empleado']}, Artículo: {info['Artículo']}, Usuario: {info['Usuario']}, Fecha Venta: {info['Fecha Venta']}, Monto del artículo: {info['Monto del artículo']}, Unidades vendidas: {info['Unidades vendidas']}, Comentario: {info['Comentario']}, Estado: {info['Estado']}")

# Diccionario para almacenar las ventas
ventas = {}

# Menu Opciones
while True:
    print("\n--- GESTIÓN DE VENTAS ---")
    print("1. Agregar venta")
    print("2. Eliminar venta")
    print("3. Visualizar ventas")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        agregar_venta(ventas)
    elif opcion == "2":
        eliminar_venta(ventas)
    elif opcion == "3":
        visualizar_ventas(ventas)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
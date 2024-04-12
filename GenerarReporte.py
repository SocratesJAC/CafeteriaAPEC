# F. REPORTE
def generar_reporte(ventas, criterio1, criterio2, fecha_inicio=None, fecha_fin=None):
    if criterio1 not in ventas or criterio2 not in ventas[criterio1]:
        print("Uno o ambos criterios de búsqueda no existen en las ventas.")
        return

    print(f"Reporte de rentas para {criterio1} '{criterio2}' entre {fecha_inicio} y {fecha_fin}:")
    total_renta = 0
    for no_factura, info in ventas[criterio1][criterio2].items():
        if fecha_inicio and fecha_fin and info["Fecha Venta"] < fecha_inicio or info["Fecha Venta"] > fecha_fin:
            continue
        print(f"No. Factura: {no_factura}, Empleado: {info['Empleado']}, Artículo: {info['Artículo']}, Usuario: {info['Usuario']}, Fecha Venta: {info['Fecha Venta']}, Monto del artículo: {info['Monto del artículo']}, Unidades vendidas: {info['Unidades vendidas']}, Comentario: {info['Comentario']}, Estado: {info['Estado']}")
        total_renta += info["Monto del artículo"] * info["Unidades vendidas"]

    print(f"Total de renta para {criterio1} '{criterio2}' entre {fecha_inicio} y {fecha_fin}: {total_renta}")

# Diccionario para almacenar las ventas por criterios
ventas_por_criterio = {"Campus": {"Campus 1": {"Proveedor 1": {"No. Factura": "001", "Empleado": "Empleado 1", "Artículo": "Artículo 1", "Usuario": "Usuario 1", "Fecha Venta": "2022-01-01", "Monto del artículo": 100, "Unidades vendidas": 2, "Comentario": "Comentario 1", "Estado": "Activo"}, "Proveedor 2": {"No. Factura": "002", "Empleado": "Empleado 2", "Artículo": "Artículo 2", "Usuario": "Usuario 2", "Fecha Venta": "2022-01-02", "Monto del artículo": 200, "Unidades vendidas": 3, "Comentario": "Comentario 2", "Estado": "Activo"}}}, "Fecha Venta": {}}

# Agregar algunas ventas de ejemplo
ventas_por_criterio["Fecha Venta"]["2022-01-01"] = {"No. Factura": "003", "Empleado": "Empleado 3", "Artículo": "Artículo 3", "Usuario": "Usuario 3", "Fecha Venta": "2022-01-01", "Monto del artículo": 300, "Unidades vendidas": 4, "Comentario": "Comentario 3", "Estado": "Activo"}

# Menu Opciones
while True:
    print("\n--- GESTIÓN DE VENTAS ---")
    print("1. Agregar venta")
    print("2. Eliminar venta")
    print("3. Visualizar ventas")
    print("4. Consultar ventas por criterio")
    print("5. Generar reporte de rentas")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        # Agregar venta
        pass
    elif opcion == "2":
        # Eliminar venta
        pass
    elif opcion == "3":
        # Visualizar ventas
        pass
    elif opcion == "4":
        # Consultar ventas por criterio
        pass
    elif opcion == "5":
        criterio1 = input("Seleccione el primer criterio de búsqueda (Campus, Fecha Venta): ")
        criterio2 = input("Seleccione el segundo criterio de búsqueda: ")
        fecha_inicio = input("Ingrese la fecha de inicio (formato YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (formato YYYY-MM-DD): ")
        generar_reporte(ventas_por_criterio, criterio1, criterio2, fecha_inicio, fecha_fin)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
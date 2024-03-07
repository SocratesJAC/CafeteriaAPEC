# F. AGREGAR
def agregar_marca(marcas):
    id_marca = input("Ingrese el ID de la marca: ")
    if id_marca in marcas:
        print("La marca ya existe.")
        return
    descripcion = input("Ingrese la descripción de la marca: ")
    estado = input("Ingrese el estado de la marca: ")
    marcas[id_marca] = {"Descripción": descripcion, "Estado": estado}
    print("Marca agregada con éxito.")

# F. ELIMINAR
def eliminar_marca(marcas):
    id_marca = input("Ingrese el ID de la marca que desea eliminar: ")
    if id_marca in marcas:
        del marcas[id_marca]
        print("Marca eliminada con éxito.")
    else:
        print("La marca no existe.")

# F. VISUALIZAR
def visualizar_marcas(marcas):
    if not marcas:
        print("No hay marcas para mostrar.")
    else:
        print("Listado de Marcas:")
        for id_marca, info in marcas.items():
            print(f"ID: {id_marca}, Descripción: {info['Descripción']}, Estado: {info['Estado']}")

# Diccionario para almacenar las marcas
marcas = {}

# Menu Opciones
while True:
    print("\n--- GESTIÓN DE MARCAS ---")
    print("1. Agregar marca")
    print("2. Eliminar marca")
    print("3. Visualizar marcas")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        agregar_marca(marcas)
    elif opcion == "2":
        eliminar_marca(marcas)
    elif opcion == "3":
        visualizar_marcas(marcas)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


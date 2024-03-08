class GestionArticulos:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, identificador, descripcion, marca, costo, proveedor, existencia, estado):
        nuevo_articulo = Articulo(identificador, descripcion, marca, costo, proveedor, existencia, estado)
        self.articulos.append(nuevo_articulo)
        print(f'Articulo agregado: {nuevo_articulo.identificador}')

    def mostrar_articulos(self):
        print("Articulos:")
        for articulo in self.articulos:
            print(f"Identificador: \n{articulo.identificador}")
            print(f"Descripcion: \n{articulo.descripcion}")
            print(f"Marca: \n{articulo.marca}")
            print(f"Costo: \n{articulo.costo}")
            print(f"Proveedor: \n{articulo.proveedor}")
            print(f"Existencia: \n{articulo.existencia}")
            print(f"Estado: \n{articulo.estado}")
            print("----------------------")

# Define the Articulo class
class Articulo:
    def __init__(self, identificador, descripcion, marca, costo, proveedor, existencia, estado):
        self.identificador = identificador
        self.descripcion = descripcion
        self.marca = marca
        self.costo = costo
        self.proveedor = proveedor
        self.existencia = existencia
        self.estado = estado

# Función para obtener el estado del articulo
def obtener_estado():
    while True:
        estado = input("Ingrese el estado (activo/inactivo): \n").lower()
        if estado in ["activo", "inactivo"]:
            return estado
        else:
            print("Por favor, ingrese 'activo' o 'inactivo'.")

# Función para obtener la opción del proveedor
def obtener_proveedor():
    while True:
        proveedor = input("Ingrese el nombre del proveedor: \n").lower()
        if proveedor:
            return proveedor
        else:
            print("Por favor, ingrese el nombre del proveedor.")

sistema_articulos = GestionArticulos()

while True:
    print("Gestion de articulos:")
    print("\n1. Agregar nuevo articulo")
    print("2. Mostrar articulos existentes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        identificador = int(input("Ingrese el identificador del articulo: \n"))
        descripcion = str(input("Ingrese la descripcion del articulo: \n"))
        marca = str(input("Ingrese la marca del articulo: \n"))
        costo = str(input("Ingrese el costo del articulo: \n"))
        proveedor = obtener_proveedor()
        existencia = int(input("Ingrese la existencia del articulo: \n"))
        estado = obtener_estado()
        sistema_articulos.agregar_articulo(identificador, descripcion, marca, costo, proveedor, existencia, estado)

    elif opcion == '2':
        sistema_articulos.mostrar_articulos()

    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")
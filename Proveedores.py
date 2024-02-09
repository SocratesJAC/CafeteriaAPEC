from datetime import datetime

class Proveedores:
    def __init__(self, identificador, nombre_comercial, rnc, fecha_registro, estado):
        self.identificador = identificador
        self.nombre_comercial = nombre_comercial
        self.rnc = rnc
        self.fecha_registro = fecha_registro
        self.estado = estado

    def mostrar_proveedor(self):
        """Muestra los datos del proveedor."""
        print(f"Identificador: {self.identificador}")
        print(f"Nombre Comercial: {self.nombre_comercial}")
        print(f"RNC: {self.rnc}")
        print(f"Fecha de Registro: {self.fecha_registro}")
        print(f"Estado: {self.estado}")
        print()

def crear_proveedor():
    """Crea un nuevo proveedor."""
    identificador = int(input("Ingrese el identificador del proveedor: "))
    nombre_comercial = input("Ingrese el nombre comercial del proveedor: ")
    rnc = input("Ingrese el RNC del proveedor: ")
    fecha_registro = datetime.now()
    estado = input("Ingrese el estado del proveedor (Activo/Inactivo): ")
    nuevo_proveedor = Proveedores(identificador, nombre_comercial, rnc, fecha_registro, estado)
    return nuevo_proveedor

def mostrar_proveedores(proveedores):
    """Muestra los proveedores existentes."""
    if not proveedores:
        print("No hay proveedores almacenados.")
    else:
        for proveedor in proveedores:
            proveedor.mostrar_proveedor()

def menu():
    """Muestra el menú de opciones."""
    print("Menú de Proveedores")
    print("------------------")
    print("1. Crear proveedor")
    print("2. Mostrar proveedores")
    print("3. Salir")
    print()

def main():
    proveedores = []
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            nuevo_proveedor = crear_proveedor()
            proveedores.append(nuevo_proveedor)
        elif opcion == 2:
            mostrar_proveedores(proveedores)
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
class GestionEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, identificador, nombre, cedula, tanda_labor, porciento_comision, fecha_ingreso, estado):
        nuevo_empleado = Empleado(identificador, nombre, cedula, tanda_labor, porciento_comision, fecha_ingreso, estado)
        self.empleados.append(nuevo_empleado)
        print(f'Empleado agregado: {nuevo_empleado.identificador}')

    def mostrar_empleados(self):
        print("Empleados:")
        for empleado in self.empleados:
            print(f"Identificador: \n{empleado.identificador}")
            print(f"Nombre: \n{empleado.nombre}")
            print(f"Cedula: \n{empleado.cedula}")
            print(f"Tanda labor: \n{empleado.tanda_labor}")
            print(f"Porciento comision: \n{empleado.porciento_comision}")
            print(f"Fecha de ingreso: \n{empleado.fecha_ingreso}")
            print(f"Estado: \n{empleado.estado}")
            print("----------------------")

# Define the Empleado class
class Empleado:
    def __init__(self, identificador, nombre, cedula, tanda_labor, porciento_comision, fecha_ingreso, estado):
        self.identificador = identificador
        self.nombre = nombre
        self.cedula = cedula
        self.tanda_labor = tanda_labor
        self.porciento_comision = porciento_comision
        self.fecha_ingreso = fecha_ingreso
        self.estado = estado

# Función para obtener el estado del empleado
def obtener_estado():
    while True:
        estado = input("Ingrese el estado (activo/inactivo): \n").lower()
        if estado in ["activo", "inactivo"]:
            return estado
        else:
            print("Por favor, ingrese 'activo' o 'inactivo'.")

sistema_empleados = GestionEmpleados()

while True:
    print("Gestion de empleados:")
    print("\n1. Agregar nuevo empleado")
    print("2. Mostrar empleados existentes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        identificador = int(input("Ingrese el identificador del empleado: \n"))
        nombre = str(input("Ingrese el nombre del empleado: \n"))
        cedula = int(input("Ingrese la cedula del empleado: \n"))
        tanda_labor = int(input("Ingrese la tanda labor del empleado: \n"))
        porciento_comision = float(input("Ingrese el porciento de comision del empleado: \n"))
        fecha_ingreso = input("Ingrese la fecha de ingreso del empleado: \n")
        estado = obtener_estado()
        sistema_empleados.agregar_empleado(identificador, nombre, cedula, tanda_labor, porciento_comision, fecha_ingreso, estado)

    elif opcion == '2':
        sistema_empleados.mostrar_empleados()

    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")
class Usuario:
    def __init__(self, identificador, nombre, cedula, tipousuario, limitecredito, fecharegistro, estado):
        self.identificador = identificador
        self.nombre = nombre
        self.cedula = cedula
        self.tipousuario = tipousuario
        self.limitecredito = limitecredito
        self.fecharegistro = fecharegistro
        self.estado = estado

class SistemaGestionUsuarios:
    def __init__(self):
        self.usuario = []

    def agregar_usuario(self, identificador, nombre, cedula, tipousuario, limitecredito, fecharegistro, estado):
        nuevo_usuario = Usuario(identificador, nombre, cedula, tipousuario, limitecredito, fecharegistro, estado)
        self.usuario.append(nuevo_usuario)
        print(f'Usuario agregado: {nuevo_usuario.cedula}')

    def mostrar_usuario(self):
        print("Usuarios:")
        for usuario in self.usuario:
            print(f"Identificador: \n{usuario.identificador}")
            print(f"Nombre: \n{usuario.nombre}")
            print(f"Cedula: \n{usuario.cedula}")
            print(f"Tipo de usuario: \n{usuario.tipousuario}")
            print(f"Limite de Credito: \n{usuario.limitecredito}")
            print(f"Fecha de Registro: \n{usuario.fecharegistro}")
            print(f"Estado: \n{usuario.estado}")
            print("----------------------")

# Función para obtener la opción de estado (activo o inactivo) del usuario
def obtener_estado():
    while True:
        estado = input("Ingrese el estado (activo/inactivo): \n").lower()
        if estado in ["activo", "inactivo"]:
            return estado
        else:
            print("Por favor, ingrese 'activo' o 'inactivo'.")

# Función para obtener la opción del tipo de usuario
def obtener_tipo():
    while True:
        estado = input("seleccione el tipo de usuario (estudiante/empleado/profesor/personal administrativo): \n").lower()
        if estado in ["estudiante", "empleado", "profesor", "personal administrativo"]:
            return estado
        else:
            print("Por favor, ingrese un tipo de usuario valido.")

sistema_usuarios = SistemaGestionUsuarios()

while True:
    print("Gestion de usuario:")
    print("\n1. Agregar nuevo usuario")
    print("2. Mostrar usuarios existentes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        identificador = int(input("Ingrese el identificador del tipo de usuario: \n"))
        nombre = str(input("Ingrese nombre del usuario: \n"))
        cedula = int(input("Ingrese la cedula: \n"))
        tipousuario = obtener_tipo()
        limitecredito = input("Ingrese limite de creditos del usuario: \n")
        fecharegistro = input("Ingrese la fecha de registro del usuario: \n")
        estado = obtener_estado()
        sistema_usuarios.agregar_usuario(identificador, nombre, cedula, tipousuario, limitecredito, fecharegistro, estado)

    elif opcion == '2':
        sistema_usuarios.mostrar_usuario()

    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")
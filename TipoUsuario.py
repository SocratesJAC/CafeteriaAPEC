class TipoUsuario:
    def __init__(self, identificador, descripcion, estado):
        self.identificador = identificador
        self.descripcion = descripcion
        self.estado = estado

class SistemaGestionUsuarios:
    def __init__(self):
        self.tipos_usuarios = []

    def agregar_tipo_usuario(self, identificador, descripcion, estado):
        nuevo_tipo_usuario = TipoUsuario(identificador, descripcion, estado)
        self.tipos_usuarios.append(nuevo_tipo_usuario)
        print(f'Tipo de usuario agregado: {nuevo_tipo_usuario.descripcion}')

    def mostrar_tipos_usuarios(self):
        print("Tipos de Usuarios:")
        for tipo_usuario in self.tipos_usuarios:
            print(f"Identificador: {tipo_usuario.identificador}")
            print(f"Descripción: {tipo_usuario.descripcion}")
            print(f"Estado: {tipo_usuario.estado}")
            print("----------------------")

# Función para obtener la opción de estado (activo o inactivo) del usuario
def obtener_estado():
    while True:
        estado = input("Ingrese el estado (activo/inactivo): ").lower()
        if estado in ["activo", "inactivo"]:
            return estado
        else:
            print("Por favor, ingrese 'activo' o 'inactivo'.")

sistema_usuarios = SistemaGestionUsuarios()

while True:
    print("Gestion de tipos de usuario:")
    print("\n1. Agregar nuevo tipo de usuario")
    print("2. Mostrar tipos de usuarios existentes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        identificador = int(input("Ingrese el identificador del tipo de usuario: "))
        descripcion = input("Ingrese la descripción del tipo de usuario: ")
        estado = obtener_estado()
        sistema_usuarios.agregar_tipo_usuario(identificador, descripcion, estado)

    elif opcion == '2':
        sistema_usuarios.mostrar_tipos_usuarios()

    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")
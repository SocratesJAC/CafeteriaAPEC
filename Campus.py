class Campus:
    def __init__(self, identificador, descripcion, estado):
        self.identificador = identificador
        self.descripcion = descripcion
        self.estado = estado

def main():
    campus_list = []  # Lista para almacenar los campus

    while True:
        print("\nMenú:")
        print("1. Agregar campus")
        print("2. Mostrar todos los campus")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == "1":
            identificador = input("Ingrese el identificador del campus: ")
            descripcion = input("Ingrese la descripción del campus: ")
            estado = input("Ingrese el estado del campus: ")

            # Crear un objeto Campus y agregarlo a la lista
            campus = Campus(identificador, descripcion, estado)
            campus_list.append(campus)

            print("¡Campus agregado con éxito!")

        elif opcion == "2":
            if not campus_list:
                print("No hay campus almacenados.")
            else:
                print("\nLista de campus:")
                for campus in campus_list:
                    print(f"Identificador: {campus.identificador}, Descripción: {campus.descripcion}, Estado: {campus.estado}")

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

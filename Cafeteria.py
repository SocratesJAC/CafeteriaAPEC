class Cafeteria:
    def __init__(self, identificador, descripcion, campus, encargado, estado):
        self.identificador = identificador
        self.descripcion = descripcion
        self.campus = campus
        self.encargado = encargado
        self.estado = estado

def main():
    cafeteria_list = []  # Lista para almacenar las cafeterías

    while True:
        print("\nMenú:")
        print("1. Agregar cafetería")
        print("2. Mostrar todas las cafeterías")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == "1":
            identificador = input("Ingrese el identificador de la cafetería: ")
            descripcion = input("Ingrese la descripción de la cafetería: ")
            campus = input("Ingrese el campus de la cafetería: ")
            encargado = input("Ingrese el nombre del encargado de la cafetería: ")
            estado = input("Ingrese el estado de la cafetería: ")

            # Crear un objeto Cafeteria y agregarlo a la lista
            cafeteria = Cafeteria(identificador, descripcion, campus, encargado, estado)
            cafeteria_list.append(cafeteria)

            print("¡Cafetería agregada con éxito!")

        elif opcion == "2":
            if not cafeteria_list:
                print("No hay cafeterías almacenadas.")
            else:
                print("\nLista de cafeterías:")
                for cafeteria in cafeteria_list:
                    print(f"Identificador: {cafeteria.identificador}, Descripción: {cafeteria.descripcion}, Campus: {cafeteria.campus}, Encargado: {cafeteria.encargado}, Estado: {cafeteria.estado}")

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
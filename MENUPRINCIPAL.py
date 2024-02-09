class Menu:
    def __init__(self):
        self.options = {
            1: self.manage_usuarios,
            2: self.manage_campus,
            3: self.manage_cafeterias,
            4: self.manage_proveedores,
            0: self.exit
        }

    def display_menu(self):
        print("\n=================================")
        print(" Bienvenido a la Cafeteria!")
        print("=================================\n")
        print("Seleccione una opción:")
        print("1. Tipo de Usuarios")
        print("2. Campus")
        print("3. Cafeterías")
        print("4. Proveedores")
        print("0. Salir")

    def run(self):
        while True:
            self.display_menu()
            option = int(input("Opción: "))
            if option in self.options:
                self.options[option]()
            elif option == 0:
                self.exit()
                break
            else:
                print("Opción inválida, por favor seleccione otra opción.")

    def manage_usuarios(self):
        print("Gestión de Tipos de Usuarios")

    def manage_campus(self):
        print("Gestión de Campus")

    def manage_cafeterias(self):
        print("Gestión de Cafeterías")

    def manage_proveedores(self):
        print("Gestión de Proveedores")

    def exit(self):
        print("¡Hasta luego!")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
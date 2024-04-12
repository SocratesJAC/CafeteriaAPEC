# menu_principal.py

import Cafeteria
import Campus
import TipoUsuario
import Proveedores
import GestionMarca
import GestionUsuarios 
import GestionArticulos
import GestionEmpleados
import VentaArticulo
import ConsultaCriterio
import GenerarReporte

def main():
    while True:
        print("\n=================================")
        print(" Bienvenido a la Cafeteria!")
        print("=================================\n")
        print("Selecciona una opción:")
        print("1. Gestionar cafeterías")
        print("2. Gestionar campus")
        print("3. Gestionar usuarios")
        print("4. Gestionar proveedores")
        print("5. Gestionar marcas")
        print("6. Gestionar ventas")
        print("7. Salir")

        opcion = input("Ingrese una opción (1-7): ")

        if opcion == "1":
            Cafeteria.main()
        elif opcion == "2":
            Campus.main()
        elif opcion == "3":
            TipoUsuario.obtener_estado()
        elif opcion == "4":
            Proveedores.main()
        elif opcion == "5":
            GestionMarca.opcion()
        elif opcion == "6":
            GestionUsuarios.sistema_usuarios()    
        elif opcion == "7":
            GestionArticulos.opcion()
        elif opcion == "8":
            GestionEmpleados.opcion()
        elif opcion == "9":
            GestionMarca.main_marcas()
        elif opcion == "10":
            VentaArticulo.main_ventas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
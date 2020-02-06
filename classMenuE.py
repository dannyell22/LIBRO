from classLibroE import Libro
class Menu:
    
    def __init__(self):
        self.libro1 = Libro()
    def menu(self): 
        print("ELIJA LA OPCIÓN QUE DESEE" , "\n")
        print("\t1 - Guardar")
        print("\t2 - Consultar")
        print("\t3 - Eliminar")
        print("\t4 - Buscar")
        print("\t9 - salir" , "\n")
    def menu2(self):
        while True:
            opcionMenu = input("ELIJA LA OPCIÓN >> ")

            if opcionMenu == "1":
                self.libro1.guardar()
            elif opcionMenu == "2":
                self.libro1.consultar() 
                input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            elif opcionMenu == "3":
                self.libro1.eliminar()
                input("SU LIBRO HA SIDO...¡¡ELIMINADO!!...\npulsa una tecla para continuar")
            elif opcionMenu == "4":
                self.libro1.buscar()
                input("Has pulsado la opción 4...\npulsa una tecla para continuar")
            elif opcionMenu == "9":
                break
            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
                #falta crear los objetos de la clase menu para llamar a los prin  de opciones
            
menu1 = Menu()
menu1.menu()  
libro1 = Menu()              
libro1.menu2()

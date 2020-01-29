import os   
#EMPIEZA LA CLASE
class Libro:
    titulo = ''
    autor = ''
#1º METODO PARA GUARDAR
    def guardar(self):
        print(self.titulo)
        print(self.autor)
        f = open("text.txt", "a")
        f.write(libro1.titulo + "-")
        f.write(libro1.autor + "\n")
        f.close()

    def consultar(self):
        f = open("text.txt", "r")
        print(f.read())
    
    """def limpiar(self):
        l = open("text.txt", "r")
        print("\n"*50)
        l.clear()
        """
#METODO DE MENU

def menu():
    os.system('cls')  
    print("Elige la opción")
    print("\t1 - Guardar")
    print("\t2 - Consultar")
    print("\t3 - tercera opción")
    print("\t9 - salir")
#ITERACION PARA QUE VUELVA A PREGUNTAR POR EL MENU
while True:
        # Mostramos el menu
    menu()

# solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
#CONDICIONES
    libro1 = Libro()
    if opcionMenu == "1":
        libro1.titulo = input("Indica el título de un libro: ")
        libro1.autor = input("Indica el autor: ")
        libro1.guardar()
    elif opcionMenu == "2":
        libro1.consultar() 
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        #libro1.limpiar()
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

os.system('cls')


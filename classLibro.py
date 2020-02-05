import os   
#EMPIEZA LA CLASE
class Libro:
    titulo = ''
    autor = ''

#1º METODO PARA GUARDAR
    def guardar(self):
        self.titulo = input("Indica el título de un libro: ")
        self.autor = input("Indica el autor: ")
        f = open("text.txt", "r")
        lectura=f.read()
        resultado=lectura.find(self.titulo)
       
        
        if resultado<0:
            print("no existe")
            f = open("text.txt", "a")
            f.write(self.titulo + "-")
            f.write(self.autor + "\n")
        else:
            print("libro ya existe")
        
        f.close()

    def consultar(self):
        f = open("text.txt", "r")
        print(f.read())
    
    def eliminar(self):
        f = open("text.txt", "r")
        lineas = f.readlines()#lineas en un array / 
        i =0
        while i<len(lineas):
            print(i , lineas[i])
            i= i+1
        indice = int(input("Indicar indice que desea borrar"))

        del lineas [indice]
        f = open("text.txt", "w")
        for valor in lineas:
            f.write(valor)
    
    def buscar(self):
        archivo = open ("text.txt", "r")
        palabra = input("Que titulo deseas buscar? ")
        linea = " "
        count = 1
        existe= False
        while (linea):
            f = open("text.txt", "r")
            linea = f.readline()
            L = linea.split()
            if palabra in L:
                print("Se Encuentra en ", count, ":", "s")
            count += 1
            existe=True
        if existe==False:
            print("No existe")
        archivo.close()
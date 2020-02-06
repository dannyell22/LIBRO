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
            print("NO EXISTE, GUARDADO CORRECTAMENTE")
            f = open("text.txt", "a")
            f.write(self.titulo + " - ")
            f.write(self.autor + "\n")
        else:
            print("ESTE LIBRO YA EXISTE")
        
        f.close()

    def buscar(self):
        f = open("text.txt", "r")
        lineas = f.readlines()
        a = input('¿QUE TE BUSCO?  ')
        i =0
        print(len(lineas) ,("ES EL TAMAÑO DE TU BIBLIOTECA"))
        while i<len(lineas):
            
            c1 = lineas[i].split()
            
            for j in range(len(c1)):
                if c1[j] == a:
                    #print(lineas[i])
                    print("Posición nº" , i , lineas[i])
            i= i+1
    
    def eliminar(self):
        f = open("text.txt", "r")
        lineas = f.readlines()#lineas en un array / 
        i =0
        while i<len(lineas):
            print(i , lineas[i])
            i= i+1
        indice = int(input("INDICAR EL INDICE QUE DESEA BORRAR "))

        del lineas [indice]
        f = open("text.txt", "w")
        for valor in lineas:
            f.write(valor)
            
    def consultar(self):
        
        f = open("text.txt", "r")
        print(f.read())
            
    
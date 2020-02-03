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
        
        
        """f.read(self.titulo + "-")
        f.read(self.autor + "\n")
        x = txt.find("text.txt", "a")
        if self.libro1.read == self.libro1.write:
            print("existe")
        else:"""
        
            
        f.close()

    def consultar(self):
        f = open("text.txt", "r")
        print(f.read())
    
    def validar(self):
        f = open("text.txt")
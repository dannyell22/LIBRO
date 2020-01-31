import os   
#EMPIEZA LA CLASE
class Libro:
    titulo = ''
    autor = ''
#1º METODO PARA GUARDAR
    def guardar(self):
        print("Registro guardado")

        f = open("text.txt", "a")
        f.write(self.titulo + "-")
        f.write(self.autor + "\n")
        f.close()

    def consultar(self):
        f = open("text.txt", "r")
        print(f.read())
    
    def validar(self):
        f = open("text.txt")
class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))
    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Desaprobado")

alumno1 = Alumno()
alumno1.inicializar("juan",8)
alumno1.imprimir()
alumno1.mostrar_estado()
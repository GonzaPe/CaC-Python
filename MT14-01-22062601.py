class persona:
    piernas = 2
    def inicializar(self, nombre):
        self.nombre = nombre
        
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))


persona1=persona()
persona1.inicializar("Pedro")
persona1.imprimir()
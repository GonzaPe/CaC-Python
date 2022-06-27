class Empleado:
    def __init__(self):
        print("Método delete llamado")
        self.nombre = input("Ingrese el nombre: ")
        self.sueldo = float(input("Ingrese el sueldo: "))
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Sueldo: {}".format(self.sueldo))
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Paga impuestos")
        else:
            print("No paga impuestos")
    def __del__(self):
        print("Método delete llamado")

empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
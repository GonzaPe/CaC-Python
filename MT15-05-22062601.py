class Operaciones:
    def __init__(self):
        self.valor1 = float(input("Ingrese el primer valor: "))
        self.valor2 = float(input("Ingrese el segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    
    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es {}".format(suma))
    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es {}".format(resta))
    def multiplicar(self):
        producto=self.valor1*self.valor2
        print("El producto es {}".format(producto))
    def dividir(self):
        division=self.valor1/self.valor2
        print("la suma es {}".format(division))

    def __del__(self):
        print("Método delete llamado")

operación1 = Operaciones()
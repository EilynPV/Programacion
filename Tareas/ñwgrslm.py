import random

class NumerosFlotantes:
    def __init__(self):
        self.numero1 = 0.0
        self.numero2 = 0.0

    def insertar_numero1(self, numero):
        self.numero1 = numero

    def insertar_numero2(self, numero):
        self.numero2 = numero

    def obtener_suma(self):
        return self.numero1 + self.numero2

    def obtener_resta(self):
        return self.numero1 - self.numero2

    def obtener_multiplicacion(self):
        return self.numero1 * self.numero2

    def obtener_division(self):
        return self.numero1 / self.numero2

numeros = NumerosFlotantes()

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numeros.insertar_numero1(numero1)
numeros.insertar_numero2(numero2)

opcion = 0
while opcion != 5:
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input())

    if opcion == 1:
        print("La suma es:", numeros.obtener_suma())
    elif opcion == 2:
        print("La resta es:", numeros.obtener_resta())
    elif opcion == 3:
        print("La multiplicación es:", numeros.obtener_multiplicacion())
    elif opcion == 4:
        print("La división es:", numeros.obtener_division())

print("Los números ingresados fueron:", numero1, numero2)
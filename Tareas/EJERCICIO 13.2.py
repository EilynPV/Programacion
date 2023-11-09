import math

class Circulo:
    PI = 3.1416

    def __init__(self, radio):
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * Circulo.PI * self.radio

    def calcular_area(self):
        return Circulo.PI * self.radio**2

    def calcular_volumen(self):
        return (4/3) * Circulo.PI * self.radio**3

def main():
    cantidad_circulos = int(input("Ingrese la cantidad de círculos: "))

    for i in range(cantidad_circulos):
        radio = float(input(f"Ingrese el radio del círculo {i + 1}: "))
        circulo = Circulo(radio)

        perimetro = circulo.calcular_perimetro()
        area = circulo.calcular_area()
        volumen = circulo.calcular_volumen()

        print(f"\nCírculo {i + 1}:")
        print(f"Perímetro: {perimetro}")
        print(f"Área: {area}")
        print(f"Volumen: {volumen}\n")

if __name__ == "__main__":
    main()

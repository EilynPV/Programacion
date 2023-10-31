class Circulo:
    
    PI = 3.1416

    def __init__(self, radio):
        
        self.radio = radio

    def obtener_perimetro(self):
        
        return 2 * Circulo.PI * self.radio

    def obtener_area(self):
        
        return Circulo.PI * self.radio ** 2

    def obtener_volumen(self):
        
        return (4 / 3) * Circulo.PI * self.radio ** 3

radio = float(input("ingrese un valor para el radio"))
mi_circulo = Circulo(radio)

perimetro = mi_circulo.obtener_perimetro()
area = mi_circulo.obtener_area()
volumen = mi_circulo.obtener_volumen()

print(f"Radio del círculo: {radio}")
print(f"Perímetro del círculo: {perimetro}")
print(f"Área del círculo: {area}")
print(f"Volumen de la esfera: {volumen}")

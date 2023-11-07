class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo: int):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio: float):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca: str):
        self.marca = unaMarca

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio:.2f}. {self.MostrarDisponibilidad()}."

    def AplicarDescuento(self, miDescuento: float):
        self.descuentoAplicado = miDescuento
        self.precio -= self.descuentoAplicado  # Restar el descuento al precio

miAuto = Automovil()

miAuto.DefinirModelo(2023)
miAuto.DefinirPrecio(25000.0)
miAuto.DefinirMarca("Toyota")

miAuto.AplicarDescuento(1000.0)

miAuto.CambiarDisponibilidad()

print(miAuto.MostrarInformacion())

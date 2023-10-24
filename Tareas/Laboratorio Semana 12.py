import datetime

class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = ""

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        return f"{self.apellidos} {self.apellido_casada}" if self.apellido_casada else self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def devolver_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def devolver_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if hoy.month < self.fecha_nacimiento.month or (hoy.month == self.fecha_nacimiento.month and hoy.day < self.fecha_nacimiento.day):
            edad -= 1
        return edad

persona = Persona()
persona.insertar_nombres("Lissy")
persona.insertar_apellidos("Parada")
persona.insertar_apellido_casada("Vasquez")
persona.insertar_fecha_nacimiento(datetime.date(1985, 6, 19))

print("Nombre completo:", persona.devolver_nombre_completo())
print("Apellidos:", persona.obtener_apellidos())
print("Fecha de nacimiento:", persona.obtener_fecha_nacimiento())
print("Edad:", persona.devolver_edad())

from random import randint

class Tablero:
    def __init__(self):
        self.oculto = [[" "] * 10 for _ in range(10)]
        self.supuesto = [[" "] * 10 for _ in range(10)]

    def imprimir(self):
        print("  A B C D E F G H I J")
        print(" +-+-+-+-+-+-+-+-+-+-+")
        numero_fila = 1
        for fila in self.supuesto:
            print("%2d|%s|" % (numero_fila, "|".join(fila)))
            numero_fila += 1

class Barco:
    def __init__(self, tamano, nombre):
        self.tamano = tamano
        self.nombre = nombre

class Jugador:
    def __init__(self):
        self.tablero = Tablero()
        self.barcos = [Barco(3, "Pequeño"), Barco(3, "Pequeño"), Barco(3, "Pequeño"),
                       Barco(5, "Grande"), Barco(5, "Grande")]

    def colocar_barcos(self):
        for barco in self.barcos:
            print(f"Ingrese la ubicación para el barco {barco.nombre} ({barco.tamano} casillas)")
            fila, columna = obtener_ubicacion_barco()
            orientacion = input("Ingrese la orientación del barco (H para horizontal, V para vertical): ").upper()

            while not self.es_ubicacion_valida(fila, columna, barco.tamano, orientacion):
                print("Ubicación inválida. Intente nuevamente.")
                fila, columna = obtener_ubicacion_barco()
                orientacion = input("Ingrese la orientación del barco (H para horizontal, V para vertical): ").upper()

            self.colocar_barco_en_tablero(fila, columna, barco.tamano, orientacion)

    def es_ubicacion_valida(self, fila, columna, tamano, orientacion):
        if orientacion == 'H':
            return columna + tamano <= 10 and all(self.tablero.oculto[fila][i] == " " for i in range(columna, columna + tamano))
        elif orientacion == 'V':
            return fila + tamano <= 10 and all(self.tablero.oculto[i][columna] == " " for i in range(fila, fila + tamano))

    def colocar_barco_en_tablero(self, fila, columna, tamano, orientacion):
        if orientacion == 'H':
            for i in range(columna, columna + tamano):
                self.tablero.oculto[fila][i] = "X"
        elif orientacion == 'V':
            for i in range(fila, fila + tamano):
                self.tablero.oculto[i][columna] = "X"

    def disparar(self, oponente):
        print('Adivina la ubicación del barco')
        oponente.tablero.imprimir()
        fila, columna = obtener_ubicacion_barco()
        
        if oponente.tablero.supuesto[fila][columna] == "~":
            print("Ya adivinaste eso.")
        elif oponente.tablero.oculto[fila][columna] == "X":
            print("¡Acertaste!")
            oponente.tablero.supuesto[fila][columna] = "X"
        else:
            print("¡FALLO!")
            oponente.tablero.supuesto[fila][columna] = "~"

def obtener_ubicacion_barco():
    fila = int(input("Ingrese la fila del barco (1-10): ")) - 1
    while fila not in range(10):
        print('No es una opción válida, por favor seleccione una fila válida')
        fila = int(input("Ingrese la fila del barco (1-10): ")) - 1
    columna = input("Ingrese la columna del barco (A-J): ").upper()
    while columna not in "ABCDEFGHIJ":
        print('No es una opción válida, por favor seleccione una columna válida')
        columna = input("Ingrese la columna del barco (A-J): ").upper()
    letras_a_numeros = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    return fila, letras_a_numeros[columna]

def contar_barcos_acertados(tablero):
    contador = 0
    for fila in tablero:
        for columna in fila:
            if columna == "X":
                contador += 1
    return contador

if __name__ == "__main__":
    jugador1 = Jugador()
    jugador2 = Jugador()

    jugador1.colocar_barcos()
    jugador2.colocar_barcos()

    turnos = 10
    turno_jugador1 = True

    while turnos > 0:
        if turno_jugador1:
            print("Turno del Jugador 1:")
            jugador1.disparar(jugador2)
        else:
            print("Turno del Jugador 2:")
            jugador2.disparar(jugador1)

        if contar_barcos_acertados(jugador2.tablero.supuesto) == 5:
            print("¡Jugador 1 ganó!")
            break
        elif contar_barcos_acertados(jugador1.tablero.supuesto) == 5:
            print("¡Jugador 2 ganó!")
            break

        turno_jugador1 = not turno_jugador1
        turnos -= 1

    print("Fin del juego")



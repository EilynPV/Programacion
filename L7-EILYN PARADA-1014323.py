# Función para realizar las operaciones aritméticas
def realizar_operaciones(numero1, numero2, operacion):
    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'multiplicacion':
        resultado = numero1 * numero2
    elif operacion == 'division':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "Error: División por cero"
    elif operacion == 'modulo':
        resultado = numero1 % numero2
    elif operacion == 'exponenciacion':
        resultado = numero1 ** numero2
    elif operacion == 'cociente':
        if numero2 != 0:
            resultado = numero1 // numero2
        else:
            resultado = "Error: División por cero"
    else:
        resultado = "Operación no válida"
    return resultado

while True:
    print("Ejercicio 1: Operaciones Aritméticas")
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("¡Error! Debe ingresar números válidos.")
        continue
    
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponenciación")
    print("7. Cociente")
    print("8. Salir")
    
    opcion = input("Seleccione una operación (1-8): ")
    
    if opcion == '8':
        break
    
    if opcion not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Opción no válida. Por favor, seleccione una opción válida.")
        continue
    
    opciones = {
        '1': 'suma',
        '2': 'resta',
        '3': 'multiplicacion',
        '4': 'division',
        '5': 'modulo',
        '6': 'exponenciacion',
        '7': 'cociente'
    }
    
    operacion_elegida = opciones[opcion]
    resultado = realizar_operaciones(numero1, numero2, operacion_elegida)
    
    print(f"{numero1} {operacion_elegida} {numero2} = {resultado}")
    
# ejercicio 3: Jerarquía de operaciones
def realizar_operaciones(a, b, c):
    resultado1 = a * b + c
    resultado2 = a * (b + c)
    resultado3 = a / (b * c)
    resultado4 = (3 * a + 2 * b) / (c ** 2)

    print(f"Resultado de a * b + c: {resultado1}")
    print(f"Resultado de a * (b + c): {resultado2}")
    print(f"Resultado de a / (b * c): {resultado3}")
    print(f"Resultado de (3a + 2b) / c^2: {resultado4}")

print("Ejercicio 3: Jerarquía de Operaciones")
try:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
except ValueError:
    print("¡Error! Debe ingresar números válidos.")
else:
    if b * c == 0:
        print("¡Error! La expresión a / (b * c) involucra una división por cero.")
    elif c == 0:
        print("¡Error! La expresión (3a + 2b) / c^2 involucra una división por cero.")
    else:
        realizar_operaciones(a, b, c)

def calcular_expresion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if a != 0 and discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)
    else:
        return "Error: Condiciones ideales no cumplidas (a ≠ 0 o b^2 - 4ac < 0)"

# ejercicio 3: Jerarquía de operaciones
def realizar_operaciones(a, b, c, opcion):
    if opcion == 1:
        resultado = a * b + c
    elif opcion == 2:
        resultado = a * (b + c)
    elif opcion == 3:
        resultado = a / (b * c)
    elif opcion == 4:
        resultado = (3 * a + 2 * b) / (c ** 2)
    elif opcion == 5:
        resultado = calcular_expresion_cuadratica(a, b, c)
    else:
        resultado = "Operación no válida"
    return resultado

while True:
    print("Ejercicio 3: Jerarquía de Operaciones")
    try:
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
    except ValueError:
        print("¡Error! Debe ingresar números válidos.")
        continue

    print("Operaciones disponibles:")
    print("1. a * b + c")
    print("2. a * (b + c)")
    print("3. a / (b * c)")
    print("4. (3a + 2b) / c^2")
    print("5. Expresión Cuadrática")
    print("6. Salir")
    
    opcion = input("Seleccione una operación (1-6): ")
    
    if opcion == '6':
        break
    
    if opcion not in ('1', '2', '3', '4', '5'):
        print("Opción no válida. Por favor, seleccione una opción válida.")
        continue
    
    opcion = int(opcion)
    resultado = realizar_operaciones(a, b, c, opcion)
    
    print("Resultado:")
    if opcion == 5:
        if isinstance(resultado, tuple):
            x1, x2 = resultado
            print(f"x1 = {x1}, x2 = {x2}")
        else:
            print(resultado)
    else:
        print(resultado)
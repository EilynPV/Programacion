def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

while True:
    print("\nMenú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    opcion = input("\nPor favor, ingresa el número de la opción que deseas ejecutar: ")

    if opcion == "1":
        numero = int(input("\nPor favor, ingresa un número: "))
        resultado = factorial(numero)
        print(f"\n{numero} = {numero} * ... * 2 * 1 = {resultado}")

    elif opcion == "2":
        numero = int(input("\nPor favor, ingresa un número: "))
        secuencia = fibonacci(numero)
        print(f"\nFibonacci({numero}) =", end=" ")
        for i in range(len(secuencia)):
            if i == len(secuencia) - 1:
                print(secuencia[i])
            else:
                print(secuencia[i], end=", ")

    elif opcion == "3":
        break

    else:
        print("\n¡Opción inválida! Por favor, elige una opción válida.")
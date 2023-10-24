cadena = input("Ingrese una cadena de caracteres: ")

contador = {"1": 0, "0": 0, "otros": 0}

for caracter in cadena:
    if caracter == '1':
        contador["1"] += 1
    elif caracter == '0':
        contador["0"] += 1
    else:
        contador["otros"] += 1
resultado = "La cadena tiene " + str(contador["1"]) + " 1's, " + str(contador["0"]) + " 0's y " + str(contador["otros"]) + " otros caracteres."

print(resultado)
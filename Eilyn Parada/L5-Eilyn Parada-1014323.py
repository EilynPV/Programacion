#Ejercicio 1#
x = input("ingresar un numero entero")
x = int(x)
n= ""
if x < 0:
    n="negativo"
elif x > 0:
    n="positivo"
else:
    n="numero igual a 0"


print("Resultado:" +n)


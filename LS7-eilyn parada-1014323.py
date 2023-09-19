
print("Ejercicio 1: operaciones aritméticas")
x=input("ingrese un numero: ")
y=input("ingrese un numero: ")
z=input("Ingrese la operación que desea (suma, resta, multiplicacion, division, módulo, exponencial o cociente) si desea que finalice ingresa (fin): ")
x=int(x)
y=int(y)
suma=x+y
resta=x-y
multiplicacion=x*y
division=x/y
módulo=x%y
exponencial=x**y
cociente=x//y
if z=="suma":
    print(str(x)+"+"+str(y)+"="+str(suma))
elif z=="resta":
    print(str(x)+"-"+str(y)+"="+str(resta))
elif z=="multiplicación":
    print(str(x)+"*"+str(y)+"="+str(multiplicacion))
elif z=="división":
    print(str(x)+"/"+str(y)+"="+str(division))
elif z=="módulo":
    print(str(x)+"%"+str(y)+"="+str(módulo))
elif z=="exponencial":
    print(str(x)+"**"+str(y)+"="+str(exponencial))
elif z=="cociente":
    print(str(x)+"//"+str(y)+"="+str(cociente))
else:
    print("error: no se puede dividir por cero")




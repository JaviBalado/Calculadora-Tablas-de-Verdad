"""
Este ejercicio ha sido realizado para comprobar la correcta realización de las tablas
de verdad en la asignautra de lógica
"""

#Coleccionamos información
letras = ""
almacenLetras = []
while letras != "fin":
    letras = input("¿Qué letras vas a usar? (Cuando termines escribe fin): ")
    almacenLetras.append(letras)
almacenLetras.remove("fin")
tamañoLetras = len(almacenLetras)
filas = 2**tamañoLetras
cantidad = 2
todasLetras=[]
z = 1

#Calculamos y almacenamos valores
for letra in almacenLetras:
    letraResultado = []
    w = 0
    f = 0
    verdaderas = filas/cantidad
    
    letraResultado.append(letra)
    i=1
    for i in range(z):
        while w < verdaderas:
            letraResultado.append(True)
            
            w+=1
        
        while f < verdaderas:
            letraResultado.append(False)
            
            f+=1
        w = 0
        f = 0
    z = z*2
    

    cantidad = cantidad * 2

    todasLetras.append(letraResultado)
# print(todasLetras)
# Empezamos con los tipos de cálculos
# ^ = y; v = o; ~ = no; -> = -
calculo = input("¿qué cálculo quieres hacer?: (^ = y; v = o; ~ = no; -> = -) ")
letra1 = input("Letra 1: ")
letra2 = input("Letra 2: ")
print(letra1 + " " + calculo + " " + letra2)
valor1 = []
valor2 = []
#almacenamos los valores de las letras que vamos a calcular
for a in todasLetras:
    
    if (a[0] == letra1):
        valor1 = a
        valor1.pop(0)
        
    if (a[0] == letra2):
        valor2 = a
        valor2.pop(0)
        
# print("Valor1: " + str(valor1))
# print("Valor2: " + str(valor2))
tamaño = len(valor1)
contador = 0
final = []
if (calculo == "y"):
    while contador < tamaño:
        if(valor1[contador] == True and valor2[contador] == True):
            final.append(True)
        else:
            final.append(False)
        contador +=1
if (calculo == "o"):
    while contador < tamaño:
        if(valor1[contador] == False and valor2[contador] == False):
            final.append(False)
        else:
            final.append(True)
        contador +=1
if (calculo == "no"):
    while contador < tamaño:
        if(valor1[contador] == True):
            final.append(False)
        else:
            final.append(True)
        contador +=1
if (calculo == "-"):
    while contador < tamaño:
        if(valor1[contador] == True and valor2[contador] == False):
            final.append(False)
        else:
            final.append(True)
        contador +=1

contador = 1
for x in final:
    print(str(contador) + ". " + str(x))
    contador+=1
    
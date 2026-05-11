import matplotlib.pyplot as plt 
from itertools import permutations
from itertools import combinations, combinations_with_replacement 
from collections import Counter 
import random 
import math

#funcion para permut visual
def permut_visual(palabra,r): 
    palabra = palabra.lower().replace(" ","") # para volver mayusculas y quitar espacios
    n = len(palabra) #longitud de la palabra 

    if r > n : 
        return "valor invalido"

    #genera las permutaciones 
    perms = permutations(palabra,r)

    if len(set(palabra)) != n: 
        perms = set(perms)

        return perms

#funcion para calculos permut 
def permut_numero(palabra, r): 
    palabra = palabra.lower().replace(" ","")
    n = len(palabra)

    #para el valor cuando r es mayor 
    if r > n : 
        return "valor invalido"
    conteo = Counter(palabra)
        
    #para cuando se quiere poner la permutacion normal
    if len(conteo) == n: 
        return math.factorial(n) // math.factorial(n-r)

    if r == n: 
        prod = 1 
        for i in conteo.values():  #los valores del conteo 
            prod *= math.factorial(i)   #para poner en factorial los valores de counter
        return math.factorial(n)// prod 
    return "caso de repeticion sin condicion de permutacion normal"

#funcion para combinacion visual 
def comb_visual(palabra, r, opcion): 
    palabra = palabra.lower().replace(" ","")        #seria mejor hacer una funcion que limpie la entrada
    opcion = opcion.lower().replace(" ","")

    if r > len(palabra): 
        return "no esta dentro del rango"
    elif opcion == "no":
        comb = combinations(palabra,r)
        return comb
    elif opcion == "si": 
        return combinations_with_replacement(palabra,r)
    else:
        return "opcion invalida"
#funcion combinatoria calculo 
def comb_calculo(palabra, r, opcion):
    palabra = palabra.lower().replace(" ","")        
    opcion = opcion.lower().replace(" ","")
    n=len(palabra)

    if r > n: 
        return "no esta dentro del rango"
    
    elif opcion == "no": 
        return math.comb(n,r)
    
    elif opcion == "si": 
        return math.factorial(n+r-1)//(math.factorial(r)*math.factorial(n-1))
    else : 
        return "opcion no valida"
def dados(n): 

    y = [0,0,0,0,0,0]
    x = [1,2,3,4,5,6]

    for i in range(n): 
        decision = random.randint(1,6)
        y[decision-1] += 1  # para guardar los valores en el contador 

    plt.bar(x,y)
    plt.title("simulacion del dado")
    plt.show()
def moneda(n):
    numca = 0 
    numcru = 0 

    for i in range(n): 
        decision = random.choice(["cara","cruz"])
        if decision == "cara":
            numca += 1 
        else: 
            numcru +=1 
    
    x = ["cara","cruz"]
    y = [numca,numcru]
    plt.bar(x,y)
    plt.title("simulacion de la moneda")
    plt.show()

while True: 
    m = int(input(""" 
    1. permutaciones
    2. combinatoria
    3. dado
    4. moneda
    5. salir...
    Elige una opcion """))

    if m == 1: 
        palabra = input("Escribir una palabra: ")
        r = int(input("escribir la subpermutacion"))
        perms = permut_visual(palabra, r)
        if isinstance(perms, str):
            print(perms)
        else:
            perms = ["".join(p) for p in perms]
            print("Permutaciones: ")
            print(perms)
        print("Numero de permutaciones:")
        print(permut_numero(palabra, r))
    elif m == 2:
        palabra = input("Escribir una palabra: ")
        r = int(input("escribir la subpermutacion: "))
        opcion = input(" con repeticion? (si / no): ")

        comb = comb_visual(palabra, r, opcion)

        if isinstance(comb, str):
            print(comb)
        else:
            combVisual = ["".join(c) for c in comb]
            print("Combinaciones:")
            print(comb_calculo(palabra, r, opcion))
    elif m == 3: 
        n = int(input("numero de muestras: "))
        dados(n)
    elif m == 4:
        n = int(input("numero de muestras: "))
        moneda(n)
    elif m == 5:
        print("saliendo...")
        break
    else: 
        print("opcion invalida")

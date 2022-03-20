import math
'''
1. Escriba una función de Python para encontrar el máximo de tres números. 
'''
def max3Num(a,b,c):
    x = [a,b,c]
    resultado = max(x)
    return resultado

'''
2. Escriba una función de Python para sumar todos los números en una lista.
'''
def sumaLista(lista):
    resultado = 0
    for i in lista:
      resultado = resultado + i
    return resultado

'''
3. Escribe una función de Python para multiplicar todos los números de una lista. 
'''
def multLista(lista):
    resultado = 1
    for i in lista:
        resultado = resultado*i
    return resultado

'''
Escriba un programa en Python para invertir una cadena.
'''
def invCadena(cadena):
    longitudCadena = len(cadena)-1
    cadenaResultado = ""
    while longitudCadena > -1:
        cadenaResultado += cadena[longitudCadena]
        longitudCadena-=1
    return cadenaResultado

'''
5. Escriba una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.
'''
def factorial(n):
    if (n == 0 || n == 1):
        return 1
    else:
        return n * factorial(n - 1)

'''
6. Escriba una función de Python para verificar si un número cae en un rango dado. 
'''
def rango(r1, r2, num):
    if num >= r1 and num <= r2:
        print(num, " dentro del rango")
    else:
        print(num, " fuera del rango")

'''
7. Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 
'''
def MinMay(cadena):
    contMay = 0
    contMin = 0
    for i in cadena:
        if i.isupper():
            contMay+=1
        elif i.islower():
            contMin+=1
        else: # Es claro que esta y la siguiente línea se pueden omitir.
            pass
    print("Cantidad de mayúsculas", contMay)
    print("Cantidad de minúsculas", contMin)

'''
8. Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista.
'''
def sinRep(lista):
    listAux = []
    for i in lista:
        if i not in listAux:
            listAux.append(i)
        else: # Es claro que esta y la siguiente línea se pueden omitir.
            pass
    return listAux

'''
9. Escribe una función de Python que tome un número como parámetro y verifique si el número es primo o no.
'''
def esPrimo(n):
    raiz = math.ceil(math.sqrt(n))
    while raiz > 1:
        if n%raiz == 0:
            return False
        else:
            raiz -= 1
    return True  

'''
10. Escriba un programa en Python para imprimir los números pares de una lista dada.
'''
def imprimirPares(lista):
    listAux = []
    for i in lista:
        if i%2 == 0:
            print(i)
        else: # Es claro que esta y la siguiente línea se pueden omitir.
            pass

'''
11. Escribe una función de Python para comprobar si un número es perfecto o no.
'''
def esPerfecto(numero):
  n = numero - 1
  resultado = 0
  while n > 0:
    if numero % n == 0:
      resultado += n
    n -= 1
  return resultado == numero

'''
12. Escriba una función de Python que verifique si una cadena pasada es palíndromo o no.
'''
def esPalindromo(cadena):
    return cadena == invCadena(cadena)

'''
13. Escriba una función de Python que imprima las primeras n filas del triángulo de Pascal.
'''
def trianguloPascal(n):
    pass # Sin implementar.

'''
14. Escriba una función de Python para verificar si una cadena es un pangrama o no.
'''
def esPangrama(cadena):
    pass

'''
15. Escriba un programa Python que acepte una secuencia de palabras separadas por guiones como entrada e imprima las palabras en una secuencia separada por guiones después de ordenarlas alfabéticamente.
'''
def ordenarPalabras(cadena):
    pass

'''
16. Escriba una función de Python para crear e imprimir una lista donde los valores sean cuadrados de números entre 1 y 30 (ambos incluidos).
'''
def losCuadrados(param1, param2):
    pass

'''
17. Escriba un programa en Python para crear una cadena de decoradores de funciones (negrita, cursiva, subrayado, etc.) en Python. 
'''
def decoradores():
    pass

'''
18. Escriba un programa Python para ejecutar una cadena que contenga código Python. 
'''
def ejecucion():
    pass

'''
19. Escriba un programa Python para acceder a una función dentro de una función.
'''
def acceder():
    pass

'''
20. Escriba un programa en Python para detectar el número de variables locales declaradas en una función. 
'''
def detectaLocales():
    pass

'''
21. Escriba un programa de Python que invoque una función dada después de milisegundos específicos.
'''
def invoqueMilisegundos():
    pass

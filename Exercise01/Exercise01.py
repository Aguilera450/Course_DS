def max3Num(a,b,c):
    x = [a,b,c]
    resultado = max(x)
    return resultado

def sumaLista(lista):
    resultado = 0
    for i in lista:
      resultado = resultado + i
    return resultado

def multLista(lista):
    resultado = 1
    for i in lista:
      resultado = resultado*i
    return resultado

def invCadena(cadena):
    longitudCadena = len(cadena)-1
    cadenaResultado = ""
    while longitudCadena > -1:
      cadenaResultado += cadena[longitudCadena]
      longitudCadena-=1
    return cadenaResultado

def rango(r1, r2, num):
    if num >= r1 and num <= r2:
        print(num, " dentro del rango")
    else:
        print(num, " fuera del rango")

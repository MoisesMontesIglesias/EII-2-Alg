#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      moise
#
# Created:     16/04/2024
# Copyright:   (c) moise 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

numeroSoluciones = 0

def CuadradoNumerico(fich):
    inicio = time.time()
    hx = 0
    hy = 0
    numerosPosibles = 10 ##Combinacion de número que podemos generar (0-9)
    tab, h = leerFichero(fich)
    BackTracking(tab, h, hx, hy, numerosPosibles, inicio)
    print("El numero total de soluciones encontradas es: ", numeroSoluciones)

def leerFichero(fich):
    h = 0
    with open(fich, 'r') as f:
        linea = f.readline().strip()
        tamaño = int(linea)
        tab = []
        for i in range(tamaño * 2 + 1):
            fila = []
            for j in range(tamaño * 2 + 1):
                fila.append("x")
            tab.append(fila) ## Creamos una matriz de un valor cualquiera en este caso x
        espacios = ""
        for i, linea in enumerate(f):
            espacios = linea.strip().split(" ") ## Espacios guarda los valores del fichero dado
            if i % 2 == 0 and i != tamaño * 2:
                for j in range(len(espacios)):
                    ## En la matriz que creamos de valores x, sustituimos por los
                    ## valores de la matriz del fichero y si es igual a ?, sumamos uno a la cantidad de espacios
                    ## que tenemos que rellenar
                    tab[i][j] = espacios[j]
                    if tab[i][j] == "?":
                        h += 1
            else:
                ##Aquí cambiamos los símbolos intermedios, +,-,*,/
                for j in range(0, len(espacios) * 2,2):
                    tab[i][j] = espacios[j//2]

    return tab, h

def BackTracking(tab, h, hx, hy, numerosPosibles, inicio):
    solucionEncontrada, hx, hy = EsSolucion(tab,hx,hy)
    if(solucionEncontrada == True): ## Si encontramos una fila válida
        if(h == 0): ## Y ademas los huecos están completos (es decir, que sean 0)
                ## se calcula el tiempo que se tarde y mostramos la matriz por pantalla
                ## ademas de sumar 1 al número de soluciones
            final = time.time()
            tiempoSolucion = final - inicio
            printMatriz(tab, tiempoSolucion)
            global numeroSoluciones ## Lo utilizo como variable global del programa
                                    ## para contabilizar las soluciones sin editar los return
            numeroSoluciones += 1
            return
        else:
            h -= 1 ## Eliminamos un hueco
            i = 0
            while i < numerosPosibles:
                valor = str(i)
                tab[hx][hy] = valor
                BackTracking(tab, h, hx, hy, numerosPosibles, inicio) ##Repetimos el proceso
                i+=1
            incognita = "?"
            tab[hx][hy] = incognita ## Si no se encuentra solución, volvemos a poner el ? y aumentamos el numero de huecos
            h+=1
    else:
        return ## Fila no válida


def EsSolucion(numeroGenerado, matriz, valor, tamaño, resultadoFila, resultadoColumna, podar):
    podar -= 1
    if(valor > tamaño*2-1):
        estadoColumna = SaberSiColumnaValida(tamaño, numeroGenerado, 0, matriz, resultadoColumna)
        if(estadoColumna == False):
            return False, hx, hy, podar
        else:
            podar = tamaño
            return True, hx, hy, podar
    else:
        estadoFila = SaberSiFilaValida(tamaño, numeroGenerado, valor, matriz, resultadoFila)
        if(estadoFila == False):
            return False, hx, hy, podar
        else:
            return EsSolucion(numeroGenerado, matriz, valor+2, tamaño, resultadoFila, resultadoColumna, podar)

def SaberSiFilaValida(tab, hx, hy):
    for i in range(0,len(tab) - 2, 2):
        for j in range(0,len(tab[i]) - 2, 2):
            if(tab[i][j] == "?"): ##Posición sin rellenar
                return True, i, j
        numero = int(tab[i][0]) ## Realizamos la suma de toda la fila
        for j in range(1,len(tab[i]) - 2, 2):
            if(tab[i][j] == "+"):
                numero += int(tab[i][j+1])
            elif(tab[i][j] == "-"):
                numero -= int(tab[i][j+1])
            elif(tab[i][j] == "*"):
                numero *= int(tab[i][j+1])
            else:
                if(tab[i][j+1] == "0"):
                    return False, hx, hy
                else:
                    numero /= int(tab[i][j+1])
            numero = int(numero)
        if (numero != int(tab[i][len(tab[0])-1])): ## Comprobamos el resultado de la fila
            return False, hx, hy

    return True, hx, hy

def SaberSiColumnaValida(tab, hx, hy):
    for i in range(0,len(tab)-2,2):
        numero = int(tab[0][i])
        for j in range(1,len(tab[0]) - 2, 2):
            if(tab[j][i] == "+"):
                numero += int(tab[j+1][i])
            elif(tab[j][i] == "-"):
                numero -= int(tab[j+1][i])
            elif(tab[j][i] == "*"):
                numero *= int(tab[j+1][i])
            elif(tab[j][i] == "/"):
                if(tab[j][i+1] == "0" ):
                    return False, hx, hy
                else:
                    numero /= int(tab[j+1][i])
            else:
                return False, hx, hy
            int(numero)
        if (numero != int(tab[len(tab) - 1][i])):
            return False, hx, hy

    return True, hx, hy


def printMatriz(tab, tiempoSolucion):
    print("Matriz con solucion hallada en el instante: " + str(round(tiempoSolucion,10)) + " " + "---" * len(tab))
    for i in range(len(tab)):
        cadena = ""
        for j in range(len(tab[i])):
            if(tab[i][j] == "x"):
                    cadena += ""
            else:
                if(i % 2 == 0):
                    if (i != len(tab[i]) -1):
                        if(j == len(tab[i]) - 1):
                            cadena += tab[i][j]
                        else:
                            cadena += tab[i][j] + "\t"
                    else:
                        cadena += tab[i][j] + "\t\t"
                else:
                    if(tab[i][j] == "x"):
                        cadena += " "
                    else:
                        if(j == len(tab[i]) - 1):
                            cadena += tab[i][j]
                        else:
                            cadena += tab[i][j] + "\t\t"

        print(cadena)
    print("\n")

##fichero = input("Dame el nombre del fichero: ")
##CuadradoNumerico(fichero)

CuadradoNumerico('test01.txt')
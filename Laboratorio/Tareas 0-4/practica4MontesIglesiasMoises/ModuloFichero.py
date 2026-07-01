#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      moise
#
# Created:     18/03/2024
# Copyright:   (c) moise 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random as random
import math
import AlgoritmoPrim

def PrimMatrizFichero(fichero):
    m = matrizTriangularDesdeFichero(fichero)
    longitudMatriz = len(m)
    aristas = []
    visitados = [False] * longitudMatriz
    visitados[0] = True
    costeValor = []
    costeTotal = 0
    for i in range(longitudMatriz-1):
        valor = 99999999
        fila = -1
        columna = -1
        for j in range(longitudMatriz):
            if(visitados[j] == True):
                for k in range(longitudMatriz):
                    if(visitados[k] == False and m[j][k] < valor and m[j][k] > 0):
                        fila = j
                        columna = k
                        valor = m[j][k]

        visitados[columna] = True
        aristas.append((fila, columna))
        costeValor.append(valor)
        costeTotal += valor

    printPrim(aristas, costeTotal, costeValor)

def printPrim(aristas, costeTotal, costeValor):
    print("COSTE TOTAL ÓPTIMO= ", costeTotal, "")
    print("**************************")
    print("ARISTAS SELECCIONADAS=")
    for i in range(len(aristas)):
        if(aristas[i] == aristas[len(aristas[0]) - 1]):
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", aristas[i][0], " HASTA NODO", aristas[i][1], "*** COSTE=", costeValor[i])


##m=matrizTriangularDesdeFichero("grafo4.txt")
##PrimMatrizFichero(m)
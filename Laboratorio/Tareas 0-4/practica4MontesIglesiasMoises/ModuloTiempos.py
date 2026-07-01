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
from AlgoritmoPrim import *

def PrimMatriz(m):
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

def PrimTiempos():
    n = 256
    while n < 1000000:
        m =  matrizTriangularEnterosAleatorios(n,100,1000)
        start_time = time.time()
        PrimMatriz(m)
        end_time = time.time()
        print("Tiempo de computación: ", end_time - start_time)
        n*=2

PrimTiempos()
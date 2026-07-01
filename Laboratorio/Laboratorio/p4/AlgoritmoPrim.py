#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO296102
#
# Created:     12/03/2024
# Copyright:   (c) UO296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random as random
import math
import time

def crearMatriz(n,valor):
    """Crea en memoria principal una matriz
    cuadrada de orden n, con elementos igual
    a valor.
    Al final retorna dicha matriz  """
    m=[]
    for i in range(n):
        m.append(n*[valor])
    return m


def escribirMatriz(m):
    """Recibe una matriz y la escribe por
    pantalla de forma clásica"""
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j],end="\t")
        print()
    print()

##m=crearMatriz(16,0)
##escribirMatriz(m)


def matrizTriangularEnterosAleatorios(n,inf,sup):
    """Genera y devuelve una matriz triangular (i<j) de
    orden n, con enteros aleatorios entre [inf..sup]"""
    m=crearMatriz(n,0)
    for i in range(n):
        for j in range(i+1,n):
            m[i][j]=random.randint(inf,sup)
    return m

##m=matrizTriangularEnterosAleatorios(16,100,999)
##escribirMatriz(m)


def matrizTriangularDesdeFichero(fich):
    """Genera un matriz triangular (i<j) que lee
    desde un fichero de entrada, con formato visto"""
    fi=open(fich,"r")
    n=int(fi.readline())
#    print(n)
    m=crearMatriz(n,0)
#    escribirMatriz(m)
    i=0
    for linea in fi:
        lista=linea.strip().split(",")
#        print(lista)
        k=0
        for j in range(i+1,n):
            m[i][j]=int(lista[k])
            k=k+1
        i=i+1
    fi.close()
    return(m)

##m=matrizTriangularDesdeFichero("grafo16.txt")
##escribirMatriz(m)

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

    print("COSTE TOTAL ÓPTIMO= ", costeTotal, "")
    print("**************************")
    print("ARISTAS SELECCIONADAS=")
    for i in range(len(aristas)):
        if(aristas[i] == aristas[len(aristas[0]) - 1]):
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", aristas[i][0], " HASTA NODO", aristas[i][1], "*** COSTE=", costeValor[i])
        else:
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", aristas[i][0], " HASTA NODO", aristas[i][1], "*** COSTE=", costeValor[i])

##m=matrizTriangularDesdeFichero("grafo4.txt")
##PrimMatriz(m)

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



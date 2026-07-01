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

import random
import math


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

def Prim(fichero):
    m = matrizTriangularDesdeFichero(fichero)
    visitados = [len(m)]
    for i in range(len(m)):
        if(i == 0):
            visitados[i] = True
        else:
            visitados[i] = False
    aristas = []
    costes = []
    costeTotal = 0
    while len(aristas) < len(m):
        for i in range(len(m)):
            valorMaximo = max(m[i]) + 1
            fila = -1
            columna = -1
            for j in range(len(m)):
                if(m[i][j] > 0 and valorMaximo > m[i][j]):
                    valorMaximo = m[i][j]
                    fila = i
                    columna = j
            costes.append(valorMaximo)
            aristas.append([fila, columna])

        if(fila == -1 and columna == -1):
            aristas.append([fila])
            visitados[columna] = True
            costeTotal += valorMaximo

    return valorMaximo

##fichero = input("Dame el nombre del fichero: ")
fichero = "grafo4.txt"
Prim(fichero);

##m=crearMatriz(16,0)
##escribirMatriz(m)

##m=matrizTriangularEnterosAleatorios(16,100,999)
##escribirMatriz(m)

##m=matrizTriangularDesdeFichero("grafo16.txt")
##escribirMatriz(m)
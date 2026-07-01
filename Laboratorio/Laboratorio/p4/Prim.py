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

def prim(fichero):
    matrix = matrizTriangularDesdeFichero(fichero)
    n = len(matrix)
    selected = [False] * n
    selected[0] = True
    edges = []
    costeValor = []
    total_cost = 0

    while len(edges) < n - 1:
        min_cost = float('inf')
        fila = -1
        columna = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and matrix[i][j] < min_cost and matrix[i][j] > 0:
                        min_cost = matrix[i][j]
                        fila = i
                        columna = j

        if fila != -1 and columna != -1:
            edges.append((fila, columna))
            selected[columna] = True
            costeValor.append(min_cost)
            total_cost += min_cost

    print("COSTE TOTAL ÓPTIMO= ", total_cost, "")
    print("**************************")
    print("ARISTAS SELECCIONADAS=")
    for i in range(len(edges)):
        if(edges[i] == edges[len(edges[0]) - 1]):
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", edges[i][0], " HASTA NODO", edges[i][1], "*** COSTE=", costeValor[i])
        else:
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", edges[i][0], " HASTA NODO", edges[i][1], "*** COSTE=", costeValor[i])


prim("grafo4.txt")


def primEjemplo(w,n,s):
    v = []
    while (len(v)!=n):
        v.append(0)
    v[s] = 1
    E = []
    for i in range(0,n-1):
        minimo = 9
        agregar_vertice = 0
        e = []
        for j in range(n):
            if(v[j] == 1):
                for k in range(n):
                    if(v[k] == 0 and w[j][k] < minimo):
                        agregar_vertice = k
                        e = [j,k]
                        minimo = w[j][k]

        v[agregar_vertice] = 1
        E.append(e)
    return E



def PrimMAl(m): ##def Prim(fichero):
    ## m = matrizTriangularDesdeFichero(fichero):
    longitudMatriz = len(m)
    visitados = [False] * longitudMatriz
    visitados[0] = True
    aristas = []
    costeValor = []
    costeTotal = 0

    while len(aristas) < longitudMatriz - 1:
        valor = 99999999999
        fila = -1
        columna = -1

        for i in range(longitudMatriz):
            if (visitados[i] == True):
                for j in range(longitudMatriz):
                    if (visitados[j]==False and m[i][j] > 0 and m[i][j] < valor):
                        valor = m[i][j]
                        fila = i
                        columna = j

        if (fila != -1 and columna != -1):
            visitados[columna] = True
            aristas.append((fila, columna))
            costeValor.append(valor)
            costeTotal += valor

    print("COSTE TOTAL ÓPTIMO= ", costeTotal, "")
    print("**************************")
    print("ARISTAS SELECCIONADAS=")
    for i in range(len(aristas)):
        if(i == len(aristas) - 1):
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", aristas[i][0], " HASTA NODO", aristas[i][1], "*** COSTE=", costeValor[i])
        else:
            print("ARISTA NÚMERO",i + 1,":  DESDE NODO=", aristas[i][0], " HASTA NODO", aristas[i][1], "*** COSTE=", costeValor[i])

##fichero = input("Dame el nombre del fichero con su extensión: ")
##Prim(fichero)
##m=matrizTriangularDesdeFichero("grafo16.txt")
##Prim(m)

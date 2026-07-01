#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO296102
#
# Created:     19/03/2024
# Copyright:   (c) UO296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def progDin(texto, patron):
    copiaTexto = " " + texto
    copiaPatron = " "+ patron
    n = len(copiaTexto)
    m = len(copiaPatron)
    mat = crearMatriz(n,m)
    mat[0][0] = True
    ##printResultado(mat)
    for i in range(1 ,n):
        for j in range(1, m):
            #print(i,j)
            #caracteres iguales en posicion i y posicion j
            if(copiaTexto[i] == copiaPatron[j]):
                if(mat[i-1][j-1]):
                    mat[i][j] = True

            if(copiaPatron[j] == '?'):
                if(mat[i][j-1] or mat[i-1][j-1]):
                    mat[i][j] = True

            if(copiaPatron[j] == '*'):
                if(mat[i][j-1] or mat[i-1][j-1] or mat[i-1][j]):
                    mat[i][j] = True
    printResultado(mat, texto, patron)
    return mat[n-1][m-1]

def leerFichero(fich):
    patrones = []
    resultados = []
    fi=open(fich,"r")
    for linea in fi:
        lista = linea.strip().split(" ")
        if(len(lista) == 1):
            texto = lista
        else:
            patrones.append(lista[0])
            resultados.append(lista[1])
    fi.close()
    return(texto, patrones, resultados)

def crearMatriz(n,m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(False)
        matriz.append(fila)
    return matriz

def printResultado(m, texto, patron):
    texto = list(texto)
    patron = list(patron)
    for i in range(len(patron)+2):
        camino = ""
        if(i == 0):
            camino += "   "
        elif(i == 1):
            camino += "  T"
        else:
            camino += str(patron[i-2]) + " F"
        for j in range(len(texto)):
            if(i == 0 and j < len(texto)):
                camino += " " + texto[j]
            elif(i == 1):
                camino += " " + "F"
            elif(i > 1):
                camino += " " + str(m[j][i-2])[0]
            else:
                pass
        print(camino)

def ejemplo1():
    texto = "casa"
    patrones = "casa"
    print(progDin(texto, patrones))

def ejemplo2():
    texto = "casa"
    patrones = "cosa"
    print(progDin(texto, patrones))

def ejemplo3():
    texto = "casa"
    patrones = "ca?a"
    print(progDin(texto, patrones))

def ejemplo4():
    texto = "casa"
    patrones = "**a"
    print(progDin(texto, patrones))

def apartadoC():
    texto = "o**?o"
    patrones = "oviedo"
    print(progDin(texto, patrones))

def main():
    ejemplo1()
    ##ejemplo2()
    ##ejemplo3()
    ##ejemplo4()

    ##texto, patrones, resultados = leerFichero("test1.txt")
    ##texto, patrones, resultados = leerFichero("test2.txt")
    ##texto, patrones, resultados = leerFichero("test3.txt")
    ##for i in range(len(patrones)):
    ##    print(progDin(texto[0], patrones[i]))

main()
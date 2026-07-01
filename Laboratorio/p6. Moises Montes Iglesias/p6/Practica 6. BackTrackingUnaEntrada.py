#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      uo296102
#
# Created:     09/04/2024
# Copyright:   (c) uo296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time

def main():
    inicio = time.time()
    tamaño, matriz, resultadoFila, resultadoColumna, numeroPorDefecto = leerFichero('test02.txt')
    BackTracking(numeroPorDefecto, tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna)
    fin = time.time()
    tiempoTotal = fin-inicio
    print("El tiempo que se tarda en hallar la primera solución al cuadrado es: ", tiempoTotal),##round(tiempoTotal,4)," segundos")

def leerFichero(fich):
    matriz = []
    resultadoFila = []
    resultadoColumna =[]
    fi=open(fich,"r")
    for linea in fi:
        lista = linea.strip().split(" ")
        if(len(lista) == 1):
            tamaño = int(lista[0])
        else:
            fila = []
            for i in range(len(lista)):
                if(lista[i] == "="):
                    resultadoFila.append(lista[i+1])
                    break
                elif(len(resultadoFila) > 0):
                    if(resultadoFila[len(resultadoFila) -1] == "="):
                        resultadoColumna.append(lista[i])
                    else:
                        fila.append(lista[i])
                else:
                    fila.append(lista[i])
            if(len(fila) > 0):
                matriz.append(fila)

    fi.close()
    resultadoFila.pop()
    numeroPorDefecto = ValorPorDefecto(matriz)
    return tamaño, matriz, resultadoFila, resultadoColumna, numeroPorDefecto

def ValorPorDefecto(matriz):
    valor = []
    for i in range(0,len(matriz),2):
        for j in range(0,len(matriz[i]),2):
            if(matriz[i][j] != '?'):
                valor.append(matriz[i][j])
            else:
                valor.append('0')

    return valor

def IteradorNumero(NumeroGenerado, numeroPorDefecto, valor):
    NumeroGenerado[valor] = str(int(NumeroGenerado[len(NumeroGenerado)-1])+1)
    for i in range(len(NumeroGenerado)-1, -1, -1):
        if NumeroGenerado[i] == '10':
            if(i == 0):
                NumeroGenerado[i] = '10'
                return NumeroGenerado
            else:
                numero = str(int(NumeroGenerado[i-1])+1)
                NumeroGenerado[i-1] = numero
                NumeroGenerado[i] = '0'
    print(NumeroGenerado)
    return NumeroGenerado

def NumeroPosible(NumeroGenerado, matriz, numeroPorDefecto):
    for i in range(len(numeroPorDefecto) -1, -1, -1):
        if(numeroPorDefecto[i] != '0' and NumeroGenerado[i] != numeroPorDefecto[i]):
            NumeroGenerado[i] = numeroPorDefecto[i]
            ##return NumeroPosible(NumeroGenerado, matriz, numeroPorDefecto)
    return NumeroGenerado

def BackTracking(numeroGenerado, tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna):
    SolucionEncontrada = False
    if(EsSolucion(numeroGenerado, matriz, 0, tamaño, resultadoFila, resultadoColumna) == True):
        printMatriz(tamaño, matriz, resultadoFila, resultadoColumna, numeroGenerado)
        SolucionEncontrada = True
        return SolucionEncontrada
    else:
        numeroGenerado = NumeroPosible(numeroGenerado, matriz, numeroPorDefecto)
        while(numeroGenerado[0] != '10' and SolucionEncontrada == False):
            numeroGenerado = IteradorNumero(numeroGenerado, numeroPorDefecto, len(numeroGenerado)-1)
            SolucionEncontrada = BackTracking(numeroGenerado, tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna)
        if( SolucionEncontrada == False):
            print("No se ha encontrado solución")
            return SolucionEncontrada

def EsSolucion(numeroGenerado, matriz, valor, tamaño, resultadoFila, resultadoColumna):
    estadoFila = False
    estadoColumna = False
    if(valor > tamaño*2-1):
        return True
    else:
        estadoFila = SaberSiFilaValida(tamaño, numeroGenerado, valor, matriz, resultadoFila)
        estadoColumna = SaberSiColumnaValida(tamaño, numeroGenerado, valor, matriz, resultadoColumna)
        if(estadoFila == False or estadoColumna == False):
            return False
        else:
            return EsSolucion(numeroGenerado, matriz, valor+2, tamaño, resultadoFila, resultadoColumna)

def SaberSiColumnaValida(tamaño, numeroGenerado, columna, matriz, resultadoColumna):
    ##columna-=2
    posicion = int(columna/2)
    numero = int(numeroGenerado[posicion])
    contador = int(columna/2)
    for i in range(1,len(matriz[columna]),2):
        posicion += tamaño
        if(matriz[i][contador] == '+'):
            numero += int(numeroGenerado[posicion])
        elif(matriz[i][contador] == '-'):
            numero -= int(numeroGenerado[posicion])
        elif(matriz[i][contador] == '*'):
            numero *= int(numeroGenerado[posicion])
        else:
            if(numero == 0 or int(numeroGenerado[posicion]) == 0 or numero < int(numeroGenerado[posicion])):
                numero = 0
            else:
                numero /= int(numeroGenerado[posicion])
        contador+=1
        numero = int(numero)
    if (int(numero) == int(resultadoColumna[int(columna/2)])):
        return True
    else:
        return False

def SaberSiFilaValida(tamaño, numeroGenerado, fila, matriz, resultadoFila):
    ##fila-=2
    posicion = int(int(fila/2)*tamaño)
    numero = int(numeroGenerado[posicion])
    for i in range(1,len(matriz[fila]),2):
        posicion += 1
        if(matriz[fila][i] == "+"):
            numero += int(numeroGenerado[posicion])
        elif(matriz[fila][i] == "-"):
            numero -= int(numeroGenerado[posicion])
        elif(matriz[fila][i] == "*"):
            numero *= int(numeroGenerado[posicion])
        else:
            if(numero == 0 or int(numeroGenerado[posicion]) == 0):
                numero = 0
            else:
                numero /= int(numeroGenerado[posicion])
    if (int(numero) == int(resultadoFila[int(fila/2)])):
        return True
    else:
        return False

def printMatriz(tamaño, matriz, resultadoFila, resultadoColumna, numero):
    ListaNumero = list(numero)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j] in ("0123456789?")):
                matriz[i][j] = ListaNumero[0]
                ListaNumero.pop(0)
    for i in range(len(matriz)):
        if(i%2 == 0):
            cadena = str(matriz[i][0]) + "\t"
            for j in range(1,len(matriz[i])):
                if(j == len(matriz[i])-1):
                    cadena += str(matriz[i][j]) + "\t = \t" + str(resultadoFila[int(i/2)])
                else:
                    cadena += str(matriz[i][j]) + "\t"
            print(cadena)
        else:
            cadena2 = ""
            for k in range(len(matriz[i])):
                if(k == len(matriz[i]) - 1):
                    cadena2 += str(matriz[i][k])
                else:
                    cadena2 += str(matriz[i][k]) + "\t\t"
            print(cadena2)

    cadena = ""
    for i in range(int(len(matriz[i])/2)+1):
        if(len(matriz)-1 == i):
            cadena += "="
        else:
            cadena += "=\t\t"
    print(cadena)
    cadena = ""
    for i in range(len(resultadoColumna)):
        if(i == len(resultadoColumna) - 1):
            cadena += str(resultadoColumna[i])
        else:
            cadena += str(resultadoColumna[i]) + "\t\t"
    print(cadena)

main()
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

def main():
    inicio = time.time()
    tamaño, matriz, resultadoFila, resultadoColumna, numeroPorDefecto, bucle, listaPosiciones = leerFichero('test00.txt')
    CuadradoNumerico(tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna, bucle, listaPosiciones)
    fin = time.time()
    tiempoTotal = fin-inicio
    print("El tiempo que se tarda en hallar la primera solución al cuadrado es: ", tiempoTotal) ##round(tiempoTotal,4)," segundos")

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
    numeroPorDefecto, bucle, listaPosiciones = ValorPorDefecto(matriz)
    return tamaño, matriz, resultadoFila, resultadoColumna, numeroPorDefecto, bucle, listaPosiciones

def ValorPorDefecto(matriz):
    valor = []
    listaPosiciones = []
    contador = 0
    for i in range(0,len(matriz),2):
        for j in range(0,len(matriz[i]),2):
            if(matriz[i][j] != '?'):
                valor.append(matriz[i][j])
            else:
                valor.append('0')
                contador+=1

    for i in range(len(valor)):
        if(valor[i] != '0'):
            listaPosiciones.insert(0,i)

    bucle = contador
    return valor, bucle, listaPosiciones

def NumeroPosible(NumeroGenerado, matriz, numeroPorDefecto):
    for i in range(len(numeroPorDefecto)):
        if(numeroPorDefecto[i] != '0' and numeroPorDefecto[i] != NumeroGenerado[i]):
            return False
    return True

def GenerarNumero(numeroPorDefecto, numero, bucle, listaPosiciones):
    nuevoNumero = []
    for i in range(bucle):
        if(numero > 0):
            digito = numero % 10
            nuevoNumero.insert(0, str(digito))
            numero = numero // 10
        else:
            nuevoNumero.insert(0,'0')

    contador = 0
    for i in range(len(numeroPorDefecto)-1, -1, -1):
        if(numeroPorDefecto[i] != '0'):
            nuevoNumero.insert(listaPosiciones[contador], numeroPorDefecto[i])
            contador+=1

    return nuevoNumero

def CuadradoNumerico(tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna, bucle, listaPosiciones):
    i = 0
    while i <(10**bucle):
        print(i)
        numeroGenerado = GenerarNumero(numeroPorDefecto, i, bucle, listaPosiciones)
        print(numeroGenerado)
        SolucionEncontrada, podar = BackTracking(numeroGenerado, tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna)
        #print(podar)
        if(SolucionEncontrada == True):
            return
        elif(SolucionEncontrada == False and numeroGenerado[0] == '10'):
            print("No se ha encontrado solución")
            return
        elif (SolucionEncontrada == False and podar != tamaño+1):
            x = (podar - 1) * tamaño
            if(x < 0):
                x = 0
            print(i)
            i += 10 ** x
            print(i)
        else:
            i+=1

def BackTracking(numeroGenerado, tamaño, matriz, numeroPorDefecto, resultadoFila, resultadoColumna):
    solucionEncontrada, podar = EsSolucion(numeroGenerado, matriz, 0, tamaño, resultadoFila, resultadoColumna, tamaño+1)

    if(solucionEncontrada == True):
        printMatriz(tamaño, matriz, resultadoFila, resultadoColumna, numeroGenerado)
        podar = tamaño +1

    return solucionEncontrada, podar

def EsSolucion(numeroGenerado, matriz, valor, tamaño, resultadoFila, resultadoColumna, podar):
    podar -= 1
    if(valor > tamaño*2-1):
        estadoColumna = SaberSiColumnaValida(tamaño, numeroGenerado, 0, matriz, resultadoColumna)
        if(estadoColumna == False):
            return False, podar
        else:
            podar = tamaño
            return True, podar
    else:
        estadoFila = SaberSiFilaValida(tamaño, numeroGenerado, valor, matriz, resultadoFila)
        if(estadoFila == False):
            return False, podar
        else:
            return EsSolucion(numeroGenerado, matriz, valor+2, tamaño, resultadoFila, resultadoColumna, podar)

def SaberSiColumnaValida(tamaño, numeroGenerado, columna, matriz, resultadoColumna):
    ##columna-=2
    for j in range(columna, tamaño*2-1, 2):
        posicion = int(j/2)
        numero = int(numeroGenerado[posicion])
        contador = int(j/2)
        for i in range(1,len(matriz[j]),2):
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
            numero = int(numero)
        if (int(numero) != int(resultadoColumna[int(j/2)])):
            return False
        j+=1;
    return True;


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







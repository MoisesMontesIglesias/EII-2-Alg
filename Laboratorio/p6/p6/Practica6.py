#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO296102
#
# Created:     02/04/2024
# Copyright:   (c) UO296102 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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
    return(tamaño, matriz, resultadoFila, resultadoColumna)

def ValorPorDefecto(matriz):
    valor = []
    posiciones = []
    posicion = 0
    for i in range(0,len(matriz),2):
        for j in range(0,len(matriz[i]),2):
            if(matriz[i][j] != '?'):
                valor.append(matriz[i][j])
                posiciones.append(posicion)
            else:
                valor.append('0')
            posicion+=1

    cadena = TransformarListaATexto(valor)
    return cadena, posiciones


def TransformarListaATexto(ListaValores):
    cadena = ""
    for i in range(len(ListaValores)):
        cadena+=str(ListaValores[i])
    return cadena

def SepararLista(valor, numero):
    x = str(valor)
    y = ""
    while(len(x) + len(y) < len(numero)):
        y+="0"

    return y+x

def SaberSiValor(numero, valor, posicion):
    contador = 0
    for i in range(len(numero)):
        for j in range(len(posicion)):
            if(numero[i] == valor[i] and i == posicion[j]):
                contador += 1

    if(contador == len(posicion)):
        return True
    else:
        return False

def CuadradoNumerico(tamaño, matriz, resultadoFila, resultadoColumna, valor, posicion):
    NumerosAGenerar = int(10**(tamaño**2))
    for k in range(NumerosAGenerar):
        numero = SepararLista(k, valor)
        if (SaberSiValor(numero, valor, posicion) == True):
            fila = True
            columna = True
            for i in range(0, len(matriz[0]), 2):
                fila = SaberSiFilaCorrecta(tamaño, i, matriz, resultadoFila, numero)
                columna = SaberSiColumnaCorrecta(tamaño, i, matriz, resultadoColumna, numero)
                if(fila == False or columna == False):
                    break
            if(fila == True and columna == True):
                printMatriz(tamaño, matriz, resultadoFila, resultadoColumna, valor, numero)
                return True
    return False

def SaberSiColumnaCorrecta(tamaño, posicion, matriz, resultadoColumna, numero):
    ListaNumero = list(numero)
    ListaSignos = []
    for i in range(1,len(matriz),2):
        ListaSignos.append(str(matriz[i][int(posicion/2)]))

    contador = int(ListaNumero[int(posicion/2)])
    for i in range(len(ListaSignos)):
        if(ListaSignos[i] == "+"):
            contador += int(ListaNumero[tamaño*(i+1)+ int(posicion/2)])
        elif(ListaSignos[i] == "-"):
            contador -= int(ListaNumero[tamaño*(i+1) + int(posicion/2)])
        elif(ListaSignos[i] == "*"):
            contador *= int(ListaNumero[tamaño*(i+1)+ int(posicion/2)])
        else:
            if(int(ListaNumero[tamaño*(i+1)]) == 0):
                contador = 0
            else:
                contador /= int(ListaNumero[tamaño*(i+1)+ int(posicion/2)])

    if(int(contador) == int(resultadoColumna[int(posicion/2)])):
        return True
    else:
        return False

def ListaSignos(ListaSignos, ListaNumero, tamaño, posicion):
    contador = int(ListaNumero[0])
    for i in range(len(ListaSignos)):
        if(ListaSignos[i] == "+"):
            contador += int(ListaNumero[tamaño*(i+1)+ posicion])
        elif(ListaSignos[i] == "-"):
            contador -= int(ListaNumero[tamaño*(i+1)] + posicion)
        elif(ListaSignos[i] == "*"):
            contador *= int(ListaNumero[tamaño*(i+1) + posicion])
        else:
            if(int(ListaNumero[tamaño*(i+1)] + posicion) == 0):
                contador = 0
            else:
                contador /= int(ListaNumero[tamaño*(i+1)] + posicion)

def SaberSiFilaCorrecta(tamaño, posicion, matriz, resultadoFila, numero):
    ListaNumero = list(numero)
    ListaSignos = []
    for i in range(1,len(matriz[posicion]),2):
        ListaSignos.append(str(matriz[posicion][i]))
    contador = int(ListaNumero[0])
    for i in range(len(ListaSignos)):
        if(ListaSignos[i] == "+"):
            contador += int(ListaNumero[i+1])
        elif(ListaSignos[i] == "-"):
            contador -= int(ListaNumero[i+1])
        elif(ListaSignos[i] == "*"):
            contador *= int(ListaNumero[i+1])
        else:
            if(int(ListaNumero[posicion+i+1]) == 0):
                contador = 0
            else:
                contador /= int(ListaNumero[posicion+i+1])

    contador = int(contador)
    x = 0
    if(posicion == 0):
        x = int(resultadoFila[posicion])
    else:
        x = int(resultadoFila[int(posicion/2)])

    if(contador == x):
        return True
    else:
        return False

def printMatriz(tamaño, matriz, resultadoFila, resultadoColumna, valor, numero):
    ListaNumero = list(numero)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j] in ("0123456789?")):
                matriz[i][j] = ListaNumero[0]
                ListaNumero.pop(0)
    for i in range(len(matriz)):
        if(i%2 == 0):
            cadena = matriz[i][0] + "\t"
            for j in range(1,len(matriz[i])):
                if(j == len(matriz[i])-1):
                    cadena += matriz[i][j] + "\t = \t" + resultadoFila[int(i/2)]
                else:
                    cadena += matriz[i][j] + "\t"
            print(cadena)
        else:
            cadena2 = ""
            for k in range(len(matriz[i])):
                if(k == len(matriz[i]) - 1):
                    cadena2 += matriz[i][k]
                else:
                    cadena2 += matriz[i][k] + "\t\t"
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
            cadena += resultadoColumna[i]
        else:
            cadena += resultadoColumna[i] + "\t\t"
    print(cadena)

def main():
    tamaño, matriz, resultadoFila, resultadoColumna = leerFichero('test00.txt')
    valor, posiciones = ValorPorDefecto(matriz)
    CuadradoNumerico(tamaño, matriz, resultadoFila, resultadoColumna, valor, posiciones)

main()





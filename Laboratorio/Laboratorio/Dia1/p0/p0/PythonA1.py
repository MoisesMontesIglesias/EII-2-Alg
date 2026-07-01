from time import time
from PythonA1v1 import listadoPrimos


def main():
    print("TIEMPOS DEL ALGORITMO A1")
    n=10000
    for casos in range(8):
        t1=time()  # da el tiempo en seg. y con decimales(real)
        lPrimos=listadoPrimos(n)
        t2=time()
        print("n=",n,"***","tiempo =",int(1000*(t2-t1)), "milisegundos)")
        #print(lPrimos)
        n=n*2


main()
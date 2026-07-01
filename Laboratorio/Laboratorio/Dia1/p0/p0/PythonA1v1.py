from time import time
from PythonA1v0 import primoA1


def listadoPrimos(n):
    """ calcula y devuelve todos los primos hasta n"""
    lSal=[]
    for i in range (2,n+1):
        if primoA1(i):
            lSal.append(i)
    return lSal


def main():
    n=10000
    t1=time()  # da el tiempo en seg.

    lPrimos=listadoPrimos(n)
    t2=time()
    print(t1,"///",t2)
    print("n=",n,"***","tiempo =",int(1000*(t2-t1)), "milisegundos")
    # print(lPrimos)

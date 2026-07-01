from time import time

def primoA1(m):
    """ Devuelve si m es primo o no,
    mediante un algorirmo sencillo
    que etiquetamos como A1"""
    p=True
    for i in range (2,m):
        if m%i==0:
            p=False
    return p


def main():
    t1=time()  # da el tiempo en seg.
    print(t1)
    print(10000,primoA1(10000),"***",10007,primoA1(10007))
    t2=time()
    print(t2)
    print("tiempo =",int(1000*(t2-t1)), "milisegundos")


###main()   # a borrar










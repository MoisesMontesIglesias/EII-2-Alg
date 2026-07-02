#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio 4
"""
import numpy as np
import matplotlib.pyplot as plt
#np.set_printoptions(precision = 5) 
#%%
def busquedaIncremental(f,a,b,n):
    x = np.linspace(a,b,n+1)
    intervalos = np.zeros((n,2))
    y = f(x)
    contador = 0
    
    for i in range(n):
        if y[i]*y[i+1] < 0:
            intervalos[contador,:] = x[i:i+2]
            contador += 1
            
    intervalos = intervalos[:contador,:]    
    return intervalos
#%%
def biseccion(f,a,b,tol=1.e-6,n=100):
    if f(a)*f(b) > 0.0: 
        print('La función tiene el mismo signo en los extremos')
    
    for i in range(n):
        m = 0.5*(a + b)
                
        if f(a)*f(m) < 0: 
            b = m;
        elif f(m)*f(b) < 0:  
            a = m
        else:
            break
        
        if b - a < tol:
            break
    
    return m,i+1
#%%
def todas(f,a,b):
    rf = busquedaIncremental(f,a,b,100)
    r = np.zeros(len(rf))
    for i in range(len(rf)):
        r[i] = biseccion(f,rf[i,0],rf[i,1],tol=1.e-6,n=100)[0]
    x = np.linspace(a,b,200)
    
    plt.figure()
    plt.plot(x,f(x),x,0*x,'k')
    plt.plot(r,0*r,'ro')    
    plt.show()
    
    print(r)
    
    return r
#%%
f1 = lambda x: np.cos(x)**2+x/10
f2 = lambda x: x**5-3*x**4+x+1.1
#%%
a = -10.; b = 0.
f = f1
todas(f,a,b)
#%%
a = -1.; b = 3.1
f = f2
todas(f,a,b)










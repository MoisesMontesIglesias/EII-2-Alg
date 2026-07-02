#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio 6
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc
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
def todas(f,a,b):
    rf = busquedaIncremental(f,a,b,100)
    r = np.zeros(len(rf))
    for i in range(len(rf)):
        r[i] = sc.bisect(f,rf[i,0],rf[i,1],xtol=1.e-6,maxiter=100)
    x = np.linspace(a,b,200)
    
    plt.figure()
    plt.plot(x,f(x),x,0*x,'k')
    plt.plot(r,0*r,'ro') 
    plt.show()
    
    print(r)
    
    return r
#%%
f1 = lambda x: 3*x*np.sin(3*x)+x**2-7
f2 = lambda x: (x**2+5*x-1)/(1+x**2)
#%%
a = -5.; b = 5
f = f1
todas(f,a,b)
#%%
a = -7; b = 2
f = f2
todas(f,a,b)









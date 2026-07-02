#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio 5
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
def newton(f,df,x0,tol=1.e-6,n=100):
    
    for i in range(n):
        x1 = x0 - f(x0)/df(x0)
       
        if abs(x1 - x0) < tol:
            break
        x0 = x1    
    
    return x1,i+1
#%%
def todas2(f,df,a,b):
    rf = busquedaIncremental(f,a,b,100)
    r = np.zeros(len(rf))
    for i in range(len(rf)):
        r[i] = newton(f,df,rf[i,0],tol=1.e-6,n=100)[0]
    x = np.linspace(a,b,200)
    
    plt.figure()
    plt.plot(x,f(x),x,0*x,'k')
    plt.plot(r,0*r,'ro')    
    plt.show()
    
    print(r)
    
    return r
#%%
P4  = lambda x: x**4 + 2*x**3 - 7*x**2 + 3
dP4 = lambda x: 4*x**3 + 6*x**2 -14*x
P6  = lambda x: x**6 - 0.1*x**5 - 17*x**4 + x**3 +73 *x**2 - 4*x - 68
dP6 = lambda x: 6*x**5 - 0.5*x**4 -17*4*x**3 + 3*x**2 + 73*2*x - 4
#%%
a = -4.; b = 2
f = P4
df = dP4
todas2(f,df,a,b)
#print('**************************')
#%%
a = -3.5; b = 3.5
f = P6
df = dP6
todas2(f,df,a,b)










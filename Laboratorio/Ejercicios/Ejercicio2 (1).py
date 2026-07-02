#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
L5 ex2
"""
import numpy as np
import matplotlib.pyplot as plt

def bisection(f,a,b,tol=1e-6,maxiter=100):

    error = np.inf
    k = 0
    x = a
    
    while error > tol and k < maxiter:
        
        xant = x
        x = (a + b) / 2
        
        if   f(a) * f(x) < 0:
            b = x
        elif f(x) * f(b) < 0: 
            a = x
        else:
            return x, k+1
        
        error = np.abs(x - xant)
        k += 1
        
    return x, k 
#------------------------  
def main():
    f = lambda x: x**5 - 3 * x**2 + 1.6   
       
    sol = np.zeros(3)
    
    a = -0.7; b = -0.6
    sol[0], i0 = bisection(f,a,b)
    print(sol[0], i0)
    
    a = 0.8; b = 0.9
    sol[1], i1 = bisection(f,a,b)
    print(sol[1], i1)
    
    a = 1.2; b = 1.3
    sol[2], i2 = bisection(f,a,b)
    print(sol[0], i2)
    
    x = np.linspace(-1,1.5,100)
    
    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.plot(sol,np.zeros(3),'ro')
    plt.show()
    
    #-------------------------
    print('')
    f = lambda x: np.cos(x)*(x**3+1)/(x**2+1)
      
    sol = np.zeros(3)
    
    a = -2.; b = -1.5
    sol[0], i0 = bisection(f,a,b)
    print('%.5f' % sol[0])
    
    a = -1.5; b = 0.
    sol[1], i1 = bisection(f,a,b)
    print('%.5f' % sol[1])
    
    a = 1.; b = 2.
    sol[2], i2 = bisection(f,a,b)
    print('%.5f' % sol[2])
    
    x = np.linspace(-3,3,100)
    
    plt.figure()
    plt.plot(x,f(x))
    plt.plot(x,0*x,'k')
    plt.plot(sol,np.zeros(3),'ro')
    plt.show()

if __name__ == "__main__":
    main()


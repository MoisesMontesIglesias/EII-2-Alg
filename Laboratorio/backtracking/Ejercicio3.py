#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taylor
"""
import numpy as np         
     

x = np.pi/4

fact = 1.

si = 0.
error = 1.
k = 0
signo = 1

while error > 1.e-8:    
    
    term = x**(2*k+1)/fact
    si += term*signo

    
    error = abs(term)
    
    k += 1
    fact *= 2*k * (2*k+1)
    signo *= -1
    
print('Valor aprox           = ', si)
print('Valor exacto          = ', np.sin(x)) 
print('Número de iteraciones = ', k) 
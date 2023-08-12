# -*- coding: utf-8 -*-
"""
Função restrita à N = 2n + 1 numero de pontos para se calcular a derivada,
sendo n a ordem da derivada requerida
"""

import numpy as np



h = 0.001



#%% Funções construtoras das matrizes

def matrixbdip(n,h=0.001):    
    t = int((n-1)/2)
    arr = np.zeros((t,t))
    for e in range(1,int(t+1)):
        for m in range(1,int(t+1)):
            arr[e-1,m-1] = (2*((e*h)**(2*m-1)))/np.math.factorial((2*m)-1)
    return arr
   

def matrixbdpa(n,h=0.001):    
    t = int((n-1)/2)
    arr = np.zeros((t,t))
    for e in range(1,int(t+1)):
        for m in range(1,int(t+1)):
            if m==1:
                arr[e-1,m-1] = 2*e
            else:
                arr[e-1,m-1] = (2*((e*h)**(2*(m-1)))/np.math.factorial(2*(m-1)))
    return arr

#%% Funções construtoras dos deltas

def deltpa(n,func,x0,h=0.001):
    l = []
    t = (n-1)/2
    for e in range(1,int(t+1)):
        dlt = func(x0+(e*h)) + func(x0-(e*h))
        l.append(dlt)
    l = np.array(l)
    return l
        

def deltip(n,func,x0,h=0.001):
    l = []
    t = (n-1)/2
    for e in range(1,int(t+1)):
        dlt = func(x0+(e*h)) - func(x0-(e*h))
        l.append(dlt)
    l = np.array(l)
    return l

        
def func1(x):
    return 3*x**3

def func2(x):
    return x**5
        

def dervad(orde,func,x0,n,h=0.001):
    if ((orde%2)==0):
        dlt = deltpa(n, func, x0)
        mat = matrixbdpa(n)
        print(mat)
        mat = np.linalg.inv(mat)
        print(mat)
        der = np.matmul(mat,dlt)
        print(der)
        return der[int((orde/2)-1)]
    else:
        dlt = deltip(n, func, x0)
        mat = matrixbdip(n)
        mat = np.linalg.inv(mat)
        der = np.matmul(mat,dlt)
        return der[int((orde-1)/2)]
        

dervad(2,func2,2,17)


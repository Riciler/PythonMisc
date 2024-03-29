# -*- coding: utf-8 -*-
"""
O código a seguir define uma função para se calcular as derivadas de uma função
no ponto x0 dado usando n pontos em torno de x0 (com x0 incluso)

A função derivada(orde,func,x0,n) é dividida em duas partes, sendo uma para derivadas de ordem
par (com matrixbcpa e deltapa) e outra para derivadas de ordem impar (com matrixbdip
e deltaip)

Os parametros de entrada são a ordem da derivada (orde), função (func), ponto a ser
calculada a derivada (X0) e numero de pontos com que sera calculada a derivada (n),
sendo n OBRIGATÓRIAMENTE ímpar

o parametro termos (t) também foi utilizado a fim de nos dar quantos termos teremos na array
dos deltas para fins de inicialização e preenchimento das matrizes
"""
#%%imports

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

#%% Funções construtoras das matrizes

def matrixbdip(n,h=0.001):
  '''Função construtora da matriz para 'n' pontos das derivadas ímpares.
     Sendo n o número de pontos e h=0.001 o diferencial a ser usado'''
  t = int((n-1)/2)                   #t = numero de deltas para n pontos
  arr = np.zeros((t,t))              #cria a array a ser percorrida pelos loops
  for e in range(1,int(t+1)):        #este loop percorre as linhas (a modificação no range acontece para a função não multiplicar por zero)
      for m in range(1,int(t+1)):    #este loop percorre as colunas
          arr[e-1,m-1] = (2*((e*h)**(2*m-1)))/np.math.factorial((2*m)-1)  #aqui ocorre a definição de cada termo da matriz
  return arr


def matrixbdpa(n,h=0.001):
  '''Função construtora da matriz para 'n' pontos das derivadas pares.
     Sendo n o número de pontos e h=0.001 o diferencial a ser usado'''
  t = int((n-1)/2)                 #t = numero de deltas para n pontos
  arr = np.zeros((t,t))
  for e in range(1,int(t+1)):
      for m in range(1,int(t+1)):
          arr[e-1,m-1] = (2*((e*h)**(2*(m)))/np.math.factorial(2*(m)))
  return arr

#%% Funções construtoras dos deltas

def deltpa(n,func,x0,h=0.001):
  '''Função construtora dos deltas para derivadas de ordem par.
     Recebe 'n' pontos, uma função e um ponto x0 a ser calculado'''
  l = []
  t = (n-1)/2           #Ambas funções delta utilizam o mesmo tamanho de 't' termos
  for e in range(1,int(t+1)):
      dlt = func(x0+(e*h)) + func(x0-(e*h)) - 2*func(x0)        #Este loop calcula o delta para cada par simétrico e o insere na lista l
      l.append(dlt)
  l = np.array(l)
  l = l.reshape((int(t),1))    #Aqui a lista é transformada em uma array posteriormente transposta
  return l


def deltip(n,func,x0,h=0.001):
  '''Função construtora dos deltas para derivadas de ordem ímpar.
     Recebe 'n' pontos, uma função e um ponto x0 a ser calculado'''
  l = []
  t = (n-1)/2
  for e in range(1,int(t+1)):
      dlt = func(x0+(e*h)) - func(x0-(e*h))
      l.append(dlt)
  l = np.array(l)
  l = l.reshape((int(t),1))
  return l

#%% Função derivada

def derivada(orde,func,x0,n,h=0.001):
  '''Recebe a ordem da derivada requerida (orde), função a ser derivada (func),
  ponto a ser calculada a derivada (x0) e 'n' pontos a ser utilizados no calculo'''
  if type(orde)!=int and type(orde)!=float:
    return(print('TypeError: a ordem precisa ser int ou float'))                       #Aqui um pequeno controle de erros (nem de perto a forma mais eficiente)
  #if type(x0)!=int and type(x0)!=float:                                               #nem muito funcional
  #  return(print('TypeError: x0 precisa ser int ou float'))
  #if ((n%2)==0): #or type(n)!=int:
  # return(print('O número n de pontos deve ser OBRIGATORIAMENTE ímpar e inteiro'))
  if ((orde%2)==0):            #Confere se n é ímpar
    dlt = deltpa(n, func, x0)
    mat = matrixbdpa(n)        #Aqui as duas funções anteriormente construídas são chamadas
    #print(mat)
    mat = np.linalg.inv(mat)   #Inversão da matriz de h
    #print(mat)
    der = np.matmul(mat,dlt)   #Multiplicação das matrizes
    #print(der)
    return float(der[int((orde/2)-1)])  #Agora a variavel 'orde' fornecida nos diz qual derivada retornar da array gerada,
  else:                                 #tendo uma regra para o caso par e outra para o caso ímpar.
    dlt = deltip(n, func, x0)           #Como a quantidade de ordens que podemos calcular depende de 't' só podemos calcular
    mat = matrixbdip(n)                 #derivadas na ordem de t == (n-1)/2, por exemplo, precisamos de 'n' pontos == 5 para
    mat = np.linalg.inv(mat)            #se calcular a segunda derivada, pois neste caso t == (5-1)/2 == 2.
    der = np.matmul(mat,dlt)
    return float(der[int((orde-1)/2)])

#%% Funções para teste

def func1(x):
    return 3*x**3

def func2(x):
    return x**5

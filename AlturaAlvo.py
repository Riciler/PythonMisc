# -*- coding: utf-8 -*-
'''
O programa abaixo calcula a altura em que um objeto no céu se encontra 2 horas
antes de sua culminação superior quando a declinação varia entre seus valores
maximos.

A formula abaixo foi calculada fixando se a latitude de -30° e o ângulo horario
de 30° ou -30° (2h antes ou 2h depois de sua culminação superior) na equação:
    
    sen_h = sen_dec * sen_lat + cos_dec * cos_lat * cos_hor
'''
#%% módulos
import math
import numpy as np
import matplotlib.pyplot as plt 

#%% declaração listas
sen_h = []
h = []

#%% processamento

dec_var = np.linspace(math.pi/2, -math.pi/2, 3000) #gera uma array de -pi à pi com 3000 elementos

for e in dec_var:                                  #calcula o sen da altura para cada declinação
    a = -(np.sin(e)/2) + 0.75*np.cos(e)
    sen_h.append(a)
    
for e in sen_h:                                    #extrai o valor da altura
    a = math.asin(e)
    h.append(a)

#%% geração gráfico


plt.plot(np.degrees(dec_var),np.degrees(h), color='midnightblue') #gera a curva
plt.xlabel('Declinação (Deg)')
plt.ylabel('Altura (Deg)')

plt.axhline(y=35, color='blue', linestyle='--') #gera os limites
plt.axvline(x=-84, color='blue', linestyle='--')
plt.axvline(x=16, color='blue', linestyle='--')

#Alvos
plt.axvline(x=-37, color='silver', linestyle='-', label='NGC 5986') #NGC 5986
plt.axvline(x=-67, color='silver', linestyle='-', label='NGC 6633') #NGC 6633
plt.axvline(x=-48, color='darkgreen', linestyle='-', label='NGC 6462') #NGC 6462
plt.axvline(x=-40, color='darkgreen', linestyle='-', label='NGC 6386') #NGC 6386
plt.axvline(x=-22, color='purple', linestyle='-', label='NGC 6354') #NGC 6354

'''
As barras azuis são referentes ao valor minimo e ao maximo da declinação para o
caso em questão, os valores foram encontrados a partir da analise da array gerada

Os alvos são marcados no gráfico e separados por tipo de objeto, cada um
referente à uma cor, sendo prata para aglomerados, verde para galáxias e roxo
para asterismos
'''

plt.legend()
plt.show()





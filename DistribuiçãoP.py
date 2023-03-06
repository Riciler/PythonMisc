import numpy as np
import matplotlib.pyplot as plt
import math

def maxwell_boltzmann(v, T, m):
    k = 1.38e-23   # constante de Boltzmann
    m_kg = m*1.66e-27   # converte a massa de u para kg
    return (m/(2*np.pi*k*T))**(3/2) * 4*np.pi*v**2 * np.exp(-m_kg*v**2/(2*k*T))


v = np.linspace(0, 8000)
###############################################################################
# Plot 1
T1 = 200   # temperatura em Kelvin
m1 = 2   # massa em unidades atômicas (u) 


# Plot 2
T2 = 400   # temperatura em Kelvin
m2 = 2   # massa em unidades atômicas (u)
###############################################################################

vmed1 = 157* math.sqrt(T1/m1)
vmed2 = 157* math.sqrt(T2/m2)

#Gerando o gráfico

plt.plot(v, maxwell_boltzmann(v, T1, m1),color='b')
plt.plot(v, maxwell_boltzmann(v, T2, m2),color='r')
plt.axvline(x=vmed1, color='b', linestyle='--')
plt.axvline(x=vmed2, color='r', linestyle='--')

plt.xlabel('Velocidade (m/s)')
plt.ylabel('Distribuição de Probabilidade')
plt.show()

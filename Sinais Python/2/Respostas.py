#Considere o sinal x(t) de tempo contínuo dado conforme a Figura 1 abaixo.
#a) Determine, de forma analítica, uma expressão matemática para o sinal x(t) para todo t.
# x(t) = 2[u(t + 1,5) - u(t)] + 2e^-t/2[u(t) - u(t - 3)]
#b) Plote o sinal x(t)

import numpy as np
import matplotlib.pyplot as plt

t_inicio = -6
t_fim = 7
npoints = 2000
t = np.linspace(t_inicio, t_fim, npoints)

def sinal_x(t):
    u1 = 1.0 * (t >= -1.5) 
    u2 = 1.0 * (t >= 0)
    u3 = 1.0 *(t >= 3)

    pulso1 = 2 * (u1 - u2) 
    pulso2 = 2 * np.exp(-t/2) * (u2 - u3)
    return pulso1 + pulso2

#b

x = sinal_x(t)

plt.figure(figsize=(12,8))
plt.subplot(3,2,1)
plt.plot(t, x, 'k')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Sinal x(t) = 2[u(t + 1,5) - u(t)] + 2e^-t/2[u(t) - u(t - 3)]')
plt.xlim([t_inicio, t_fim])
plt.grid()


#c
x1 = sinal_x(-t)
x2 = sinal_x(t + 4)
x3 = sinal_x(t - 2)
x4 = sinal_x(2 * t)
x5 = sinal_x(t / 2)

plt.subplot(3,2,2)
plt.plot(t,x1, 'b')
plt.xlabel('$t$')
plt.title('$(i):x(-t)$ reflexão temporal')
plt.grid()
plt.xlim([t_inicio, t_fim])

plt.subplot(3,2,3)
plt.plot(t,x2, 'r')
plt.xlabel('$t$')
plt.title('$(ii):x(t + 4)$ avanço de 4 unidades')
plt.grid()
plt.xlim([t_inicio, t_fim])

plt.subplot(3,2,4)
plt.plot(t,x3, 'g')
plt.xlabel('$t$')
plt.title('$(iii):x(t-2)$ atraso de 2 unidades')
plt.grid()
plt.xlim([t_inicio, t_fim])

plt.subplot(3,2,5)
plt.plot(t,x4, 'm')
plt.xlabel('$t$')
plt.title('$(iv):x(2t)$ compressão temporal fator 2')
plt.grid()
plt.xlim([t_inicio, t_fim])

plt.subplot(3,2,6)
plt.plot(t,x5, 'orange')
plt.xlabel('$t$')
plt.title('$(v):x(t/2)$ expansão temporal fator 2')
plt.grid()
plt.xlim([t_inicio, t_fim])

plt.tight_layout()
plt.show()
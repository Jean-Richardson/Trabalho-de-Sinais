#x(t) = (t^2 - 1)[u(t - 1) - u(t - 2)]
#a) Plote o sinal x(t) para 0 <= t <= 3
#b) Calcule de forma analítica a energia do sinal x(t)
#c) Determine, de forma numerica, a energia do sinal x(t). Compare com o resultado do item anterior.

import numpy as np 
import matplotlib.pyplot as plt

t_inicio = 0
t_fim = 3
npoints = 10000 #quanto mais pontos, mais preciso
t = np.linspace(t_inicio, t_fim, npoints)
dt = (t_fim - t_inicio)/npoints

u1 = 1.0 * (t >= 1)
u2 = 1.0 * (t >= 2)

pulso = u1 - u2

x = ((t**2) - 1) * pulso

plt.figure(figsize=(7,3))
plt.plot(t,x, 'k')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Sinal x(t) = (t^2 - 1)[u(t - 1) - u(t - 2)]')
plt.xlim([t_inicio, t_fim])
plt.grid()
plt.show()

Energia = dt * np.sum(x**2)

print('Energia (analítica) = ',38/15) #b)
print('Energia (computacional) = ', Energia) #c)

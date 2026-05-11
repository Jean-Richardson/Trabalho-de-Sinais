import numpy as np
import matplotlib.pyplot as plt

t_inicio = 0
t_fim = 3
npoints = 1000

t = np.linspace(t_inicio, t_fim, npoints)

h = np.exp(-2*t) * (t >= 0)

plt.figure(figsize=(7,3))
plt.plot(t, h, 'k')

plt.xlabel('$t$')
plt.ylabel('$h(t)=e^{-2t}u(t)$')

plt.xlim([t_inicio, t_fim])

plt.grid()

plt.show()
import numpy as np
import matplotlib.pyplot as plt

t_inicio = 0
t_fim = 0.1

npoints = 5000

t = np.linspace(t_inicio, t_fim, npoints)

# Parametros
A = 1.5
fm = 50
fc = 500

# Sinal de entrada
x = np.cos(2*np.pi*fm*t)

# Sinal AM
y = (A + x) * np.cos(2*np.pi*fc*t)

# Plot
plt.figure(figsize=(10,4))

plt.plot(t, y, 'k')

plt.xlabel('$t$')
plt.ylabel('$y(t)$')

plt.xlim([t_inicio, t_fim])

plt.grid()

plt.show()
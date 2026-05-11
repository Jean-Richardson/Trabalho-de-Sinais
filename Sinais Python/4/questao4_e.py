import numpy as np
import matplotlib.pyplot as plt

t_inicio = -1
t_fim = 4

npoints = 2000

t = np.linspace(t_inicio, t_fim, npoints)

dt = t[1] - t[0]

# Entrada
x = 1.0*((t >= 0) & (t < 2))

# Resposta ao impulso
h = np.exp(t) * (t >= 0)

# Convolução numérica
y_num = np.convolve(x, h) * dt

# Tempo convolução
t_conv = np.linspace(
    2*t_inicio,
    2*t_fim,
    len(y_num)
)

# Solução analítica
y_ana = np.zeros_like(t)

# 0 <= t < 2
idx1 = (t >= 0) & (t < 2)

y_ana[idx1] = np.exp(t[idx1]) - 1

# t >= 2
idx2 = (t >= 2)

y_ana[idx2] = np.exp(t[idx2]) * (1 - np.exp(-2))

# Plot
plt.figure(figsize=(8,4))

plt.plot(t,
         y_ana,
         'k',
         linewidth=2,
         label='Analítico')

plt.plot(t_conv,
         y_num,
         '--',
         label='Numérico')

plt.xlabel('$t$')
plt.ylabel('$y(t)$')

plt.xlim([t_inicio, t_fim])

plt.grid()

plt.legend()

plt.show()
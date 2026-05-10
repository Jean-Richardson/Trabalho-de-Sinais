import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
#a = (44/3) * np.exp(-2*t) + (1/3) * np.exp(-5*t) - 9 * np.exp(-3*t)

#b
t_inicio = 0
t_fim = 2
npoints = 1000
t = np.linspace(t_inicio, t_fim, npoints)

y = (44/3) * np.exp(-2*t) + (1/3) * np.exp(-5*t) - 9 * np.exp(-3*t)


plt.figure(figsize=(7,4))
plt.plot(t, y, 'k') 
plt.xlabel('$t$')
plt.ylabel('$v_o(t)$')
plt.title('Saída do Sistema para $0 <= t <= 2$')
plt.grid()
plt.xlim([t_inicio, t_fim])
plt.show()

#c
t = sp.symbols('t')
y = sp.Function('y')
x = 6 * sp.exp(-3*t)

lado_direito = sp.diff(x, t) + 6*x

eq = sp.diff(y(t), t, t) + 7*sp.diff(y(t), t) + 10*y(t) - lado_direito

condicoes_iniciais = {
    y(t).subs(t, 0): 6,
    y(t).diff(t).subs(t, 0): -4
}

solucao = sp.dsolve(eq, ics=condicoes_iniciais)
print(solucao.rhs)
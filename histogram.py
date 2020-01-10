import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#import seaborn as sns

fig, ax = plt.subplots()

x =[]

numbins =  # Numero de barras verticais
n, bins, patches = ax.hist(x, numbins, color='#0504aa', edgecolor='black', linewidth=1.5, facecolor='firebrick', alpha=0.7, rwidth=0.85)

plt.savefig("histograma.png", bbox_inches='tight')
plt.show()

bincenters = 0.5*(bins[1:]+bins[:-1]) # Centro de cada barr vertical do histograma

f = interp1d(bincenters, n, kind="cubic") # Interpolando com uma spline cubica
x = np.linspace(0.00029091, 0.011, num=25000)
n_interpol = f(x)
plt.plot(x, n_interpol,'-', color='firebrick', alpha=0.95, linewidth=2.0)

# Grid horizontal
plt.grid(axis='y', alpha=0.4)

# Legendas nos eixo e titulos
plt.xlabel('Tempo (s)')
plt.ylabel('Quantidade')

plt.savefig("spline.png", bbox_inches='tight')
plt.show()

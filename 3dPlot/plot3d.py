import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Artificial Data
N = 100

xRange = 10
yRange = 10
zRange = 10

xSplit = 0.4
ySplit = 0.7
zSplit = 0.5

alpha = 0.3
beta = 0.2

x = xRange * xSplit
y = yRange * ySplit
z = zRange * zSplit

c1 = (x + alpha * np.random.rand(N), y + alpha * np.random.rand(N),z + alpha * np.random.rand(N))
c2 = (x - beta * np.random.rand(N), y - beta * np.random.rand(N),z - beta * np.random.rand(N))

clusters = (c1, c2)
colors = ("red", "green")
groups = ("cluster1", "cluster2") 

# Create plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')

for data, color, group in zip(clusters, colors, groups):
    x, y, z = data
    ax.scatter(x, y, z, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('3D Plot')
plt.legend(loc=2)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

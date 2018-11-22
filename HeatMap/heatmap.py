import matplotlib.pyplot as plt
from numpy import *

with open('data.txt') as f:
    lines = f.readlines()
    x = [int(line.split()[0]) for line in lines]
    y = [int(line.split()[1]) for line in lines]
    error = [float(line.split()[2]) for line in lines]

sortedX = [i for _,i in sorted(zip(error,x))]
sortedY = [i for _,i in sorted(zip(error,y))]

eSorted = error[:]
eSorted.sort()

print('Max: ', max(error))
print('Avg: ', mean(error))

for i in range(len(eSorted)-30, len(eSorted)):
    print sortedX[i],sortedY[i],eSorted[i]

plt.hexbin(x, y, error)
plt.colorbar()
plt.show()



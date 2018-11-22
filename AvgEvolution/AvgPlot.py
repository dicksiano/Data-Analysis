import matplotlib.pyplot as plt

with open('data.txt') as f:
    lines = f.readlines()
    kick = [int(line.split()[0]) for line in lines]
    x = [float(line.split()[1]) for line in lines]
    y = [float(line.split()[2]) for line in lines]

sum = 0
for i in range(0,len(x)):
    sum += x[i]
    x[i] = sum / (i + 1)

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.set_title("Data")
ax1.set_xlabel('Number')
ax1.set_ylabel('Avg')
ax1.plot(kick,x, linewidth=0.7)

fig1=plt.gcf()
plt.show()
plt.draw()
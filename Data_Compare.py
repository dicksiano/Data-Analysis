import matplotlib.pyplot as plt

with open('data1.txt') as f:
    lines = f.readlines()
    data_01 = [int(line.split()[0]) for line in lines]
    x_01 = [float(line.split()[1]) for line in lines]
    y = [float(line.split()[2]) for line in lines]

x_01.sort()

with open('data2.txt') as f:
    lines = f.readlines()
    data_1 = [int(line.split()[0]) for line in lines]
    x_1 = [float(line.split()[1]) for line in lines]
    y = [float(line.split()[2]) for line in lines]

x_1.sort()

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.plot(data_01,x_01,data_1,x_1)

ax1.set_title("Data")
ax1.set_xlabel('Number')
ax1.set_ylabel('X (m)')

fig1=plt.gcf()
plt.show()
plt.draw()

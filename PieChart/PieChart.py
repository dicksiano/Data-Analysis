import matplotlib.pyplot as plt

with open('data.txt') as f:
    lines = f.readlines()
    kick = [int(line.split()[0]) for line in lines]
    x = [float(line.split()[1]) for line in lines]
    y = [float(line.split()[2]) for line in lines]

a = 1.0 * len(list(i for i in x if i <= 1.0))/len(x)
b = 1.0 * len(list(i for i in x if 1 < i <= 4.0))/len(x)
c = 1.0 * len(list(i for i in x if 4 < i <= 7.0))/len(x)
d = 1.0 * len(list(i for i in x if 7 < i <= 8.0))/len(x)
e = 1.0 * len(list(i for i in x if 8 < i <= 9.0))/len(x)
f = 1.0 * len(list(i for i in x if 9 < i ))/len(x)

labels = '0', '1 - 4', '4 - 7', '7 - 8', '8 - 9', '> 9'
sizes = [a, b, c, d, e, f]
explode = [0.5, 0.5, 0.5, 0.5, 0, 0]
colors = colors = ['red', 'gold', 'lightskyblue', 'lightcoral',  'green', 'blue']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
from matplotlib import pyplot as plt


# считывание с файла
fig, ax = plt.subplots(constrained_layout=True)
with open("out.txt", "r") as f:
    [amplitude, s_width, coord] = [float(x) for x in f.readline().split()]
    t = [float(x) for x in f.readline().split()]
    y = [float(x) for x in f.readline().split()]

# украшение графиков
ax.minorticks_on()
ax.set(xlabel='время (с)', ylabel='cигнал (б/р)')
ax.grid(b=True, which='major', color='#666666', linestyle='-')
ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# постройка 3 графиков горизонтально
plt.plot(t, y)
plt.title('одиночный прямоугольный импульс' + '\nширина = ' + str(s_width) + '\nсреднее х = ' + str(coord) + '\nамплитуда = ' + str(amplitude))

plt.show()

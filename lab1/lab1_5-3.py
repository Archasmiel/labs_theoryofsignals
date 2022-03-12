import numpy as np
from matplotlib import pyplot as plt

print('Введите 3 амплитуды для графиков частоты 1, 10 и 50 Гц (задавая их через enter друг после друга):')

# переменные
amplitude = [float(input()) for i in range(3)]
fig, axs = plt.subplots(3, constrained_layout=True)
freqs = [1, 10, 50]
colors = ['red', 'orange', 'green']
discret = 256
last_s = 1

# задание х и у для отрисовки
x = np.linspace(0, last_s, discret)
y = [(amplitude[i] * np.sin(2 * np.pi * freqs[i] * x)) for i in range(3)]

# украшение графиков
for ax in axs.flat:
    ax.minorticks_on()
    ax.set(xlabel='x', ylabel='y')
    ax.grid(b=True, which='major', color='#666666', linestyle='-')
    ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# общая легенда для оси х (не будет повторения по горизонтали и вертикали)
for ax in axs.flat:
    ax.label_outer()

# постройка 3 графиков горизонтально
for i in range(3):
    axs[i].plot(x, y[i], 'tab:' + colors[i])
    axs[i].set_title('f = ' + str(freqs[i]) + 'Гц      A = ' + str(amplitude[i]))

plt.show()

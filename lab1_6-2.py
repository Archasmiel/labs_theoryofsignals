import random
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


# функция значения одиночого прямоугольного импульса с заданной амплитудой, средней координатой и шириной
def singlepulse(ampl, width, mid_x, x):
    return abs(ampl * signal.square(np.pi*x/width)) if (mid_x-width/2) <= x <= (mid_x+width/2) else 0


# переменные
print('Введите амплитуду сигнала:')
amplitude = float(input())
print('Введите ширину сигнала:')
s_width = float(input())

fig, ax = plt.subplots(constrained_layout=True)
# рандомная точка от 0 до 10 с проверкой на ширину графика
coord = (random.random() * (10-s_width) + s_width/2)
discret = 256
last_s = 10

# задание х и у для отрисовки
t = np.linspace(0, last_s, discret)
y = [singlepulse(amplitude, s_width, coord, i) for i in t]

# украшение графиков
ax.minorticks_on()
ax.set(xlabel='время (с)', ylabel='cигнал (б/р)')
ax.grid(b=True, which='major', color='#666666', linestyle='-')
ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# постройка 3 графиков горизонтально
plt.plot(t, y)
plt.title('одиночный прямоугольный импульс' + '\nширина = ' + str(s_width) + '\nсреднее х = ' + str(coord) + '\nамплитуда = ' + str(amplitude))

plt.show()

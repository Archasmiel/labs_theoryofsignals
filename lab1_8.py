import math
import numpy as np
from matplotlib import pyplot as plt


# функция значения синусоидального сигнала с заданной амплитудой, частотой; длительность задана через t
def sinus(ampl, freq, x):
    return ampl * math.sin(2*np.pi * freq * x)


# переменные
print('Введите амплитуду сигнала (б/р):')
amplitude = float(input())
print('Введите частоту сигнала (Гц):')
frequency = float(input())
print('Введите длительность сигнала (с):')
last_s = float(input())


fig, ax = plt.subplots(constrained_layout=True)
discret = 256

# задание х и у для отрисовки
t = np.linspace(0, last_s, discret)
y = [sinus(amplitude, frequency, i) for i in t]

# украшение графиков
ax.minorticks_on()
ax.set(xlabel='время (с)', ylabel='cигнал (б/р)')
ax.grid(b=True, which='major', color='#666666', linestyle='-')
ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# постройка 3 графиков горизонтально
plt.plot(t, y)
plt.title('одиночный прямоугольный импульс' + '\nчастота = ' + str(frequency) + '\nдлительность = ' + str(last_s) + '\nамплитуда = ' + str(amplitude))

plt.show()

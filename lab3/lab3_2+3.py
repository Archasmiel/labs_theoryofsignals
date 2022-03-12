import math
import time
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


def create_ab(date):
    d1 = float(date[0])
    d2 = float(date[1])
    m1 = float(date[2])
    m2 = float(date[3])
    p1 = float(date[4])
    p2 = float(date[5])
    p3 = float(date[6])
    p4 = float(date[7])
    a_raw = [1, (d1 + d2) / 140, (p2 - d2) / 130, 0, -d1 / 150, -(m1 - d1) / 150]
    b_raw = [m1 / 10, (p3 - d2) / 20, -(m2 - m1) / 20, -p4 / 30, d2 / 20, -m2 / 20]
    return [np.array(a_raw), np.array(b_raw)]


def axs_config(axs):
    for ax in axs.flat:
        ax.minorticks_on()
        ax.set(xlabel='x', ylabel='y')
        ax.grid(b=True, which='major', color='#666666', linestyle='-')
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        ax.label_outer()
    return axs


def hsum(arr, mode, frequ):
    sum = 0
    if mode == 0:
        for i in arr:
            sum += i*math.cos(frequ)
    if mode == 1:
        for i in arr:
            sum += i*math.sin(frequ)
    return sum


start_time = time.time()
dot = 26

ampl = 1
last_s = 1
freq = 10
discr = 256
date = "12032002"
a = create_ab(date)[0]
b = create_ab(date)[1]

# пункти 2.1 та 2.2 і їх графіки
rng = np.random.default_rng()
t = np.linspace(0, last_s, discr)

x = ampl * np.sin(2 * np.pi * freq * t)
xn = x + rng.standard_normal(len(t)) * 0.08
y_final = signal.lfilter(b, a, x)
yn_final = signal.lfilter(b, a, xn)

arrays = [x, y_final, xn, yn_final]
arrays_name = ['2.1 вхідний сигнал', '2.1 вихідний сигнал', '2.2 вхідний сигнал', '2.2 вихідний сигнал']
arrays_color = ['-g', '.k']


fig, axs = plt.subplots(2, 2)
axs = axs_config(axs)
t_temp = [t[i] for i in range(discr)]
for m in range(2):
    for n in range(2):
        a_temp = [arrays[2*m+n][i] for i in range(discr)]
        axs[n][m].set_title(arrays_name[2*m+n])
        axs[n][m].plot(t_temp, a_temp, arrays_color[0])
        axs[n][m].plot(t_temp, a_temp, arrays_color[1])

plt.figure(1)
fig, axs = plt.subplots(2, 2)
axs = axs_config(axs)
t_temp = [t[i] for i in range(dot)]
for m in range(2):
    for n in range(2):
        a_temp = [arrays[2 * m + n][i] for i in range(dot)]
        axs[n][m].set_title(arrays_name[2 * m + n])
        axs[n][m].plot(t_temp, a_temp, arrays_color[0])
        axs[n][m].plot(t_temp, a_temp, arrays_color[1])


# пункт 3 - Коеф. Перед. Напруги
freq1 = 10
H = math.sqrt(hsum(b, 0, freq1)**2 + (hsum(b, 1, freq1)**2)/(hsum(a, 0, freq1)**2 + (hsum(a, 1, freq1)**2)))
print("Коефіцієнт передачі напруги на частоті " + str(freq1) + " Гц дорівнює " + str(H))


print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()




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
        #ax.label_outer()
    return axs


start_time = time.time()
dot = 26

ampl = 1
last_s = 1
freq1 = 3
freq2 = 20
discr = 256
date = "12032002"
a = create_ab(date)[0]
b = create_ab(date)[1]

rng = np.random.default_rng()
t = np.linspace(0, last_s, discr)

x1 = ampl * np.sin(2 * np.pi * freq1 * t)
x2 = ampl * np.sin(2 * np.pi * freq2 * t)
x3 = ampl * np.sin(2 * np.pi * freq1 * t) + ampl * np.sin(2 * np.pi * freq2 * t)

y_final1 = signal.lfilter(b, a, x1)
y_final2 = signal.lfilter(b, a, x2)
y_final3 = signal.lfilter(b, a, x3)

y_final4 = y_final1 + y_final2


fig, axs = plt.subplots(2, 4)
axs = axs_config(axs)
axs[0][0].set_title("вхідний сигнал синусоїди 3 гц")
axs[0][0].plot(t, x1, '-g')
axs[0][0].plot(t, x1, '.k')
axs[0][1].set_title("вхідний сигнал синусоїди 20 гц")
axs[0][1].plot(t, x2, '-g')
axs[0][1].plot(t, x2, '.k')
axs[0][2].set_title("вхідний сигнал суми синусоїд")
axs[0][2].plot(t, x3, '-g')
axs[0][2].plot(t, x3, '.k')
axs[0][3].set_title("вхідний сигнал суми синусоїд")
axs[0][3].plot(t, x3, '-g')
axs[0][3].plot(t, x3, '.k')
axs[1][0].set_title("вихідний сигнал синусоїди 3 гц")
axs[1][0].plot(t, y_final1, '-g')
axs[1][0].plot(t, y_final1, '.k')
axs[1][1].set_title("вихідний сигнал синусоїди 20 гц")
axs[1][1].plot(t, y_final2, '-g')
axs[1][1].plot(t, y_final2, '.k')
axs[1][2].set_title("вихідний сигнал суми синусоїд")
axs[1][2].plot(t, y_final3, '-g')
axs[1][2].plot(t, y_final3, '.k')
axs[1][3].set_title("сигнал суми вихідних сигналів")
axs[1][3].plot(t, y_final3, '-g')
axs[1][3].plot(t, y_final3, '.k')

plt.figure(1)
fig, axs = plt.subplots(1, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("перевірка для виконання адитивності(має бути суцільний графік з зелених ліній та чорних точок)")
axs[0][0].plot(t, y_final3, '-r')
axs[0][0].plot(t, y_final3, '.b')
axs[0][0].plot(t, y_final4, '-g')
axs[0][0].plot(t, y_final4, '.k')
a

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()




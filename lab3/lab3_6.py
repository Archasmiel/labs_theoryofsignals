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


start_time = time.time()

date = "12032002"
a = create_ab(date)[0]
b = create_ab(date)[1]

trans = signal.TransferFunction(b, a, dt=1)
t30, y30 = signal.dimpulse(trans, n=30)
t100, y100 = signal.dimpulse(trans, n=100)

fig, axs = plt.subplots(1, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("імпульсна характеристика (30 значень починаючи з 0)")
axs[0][0].stem(list(t30), list(y30[0]))

plt.figure(1)
fig, axs = plt.subplots(1, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("імпульсна характеристика (100 значень починаючи з 0)")
axs[0][0].stem(list(t100), list(y100[0]))

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()




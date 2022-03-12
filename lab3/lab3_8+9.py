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

ampl = 1
last_s = 1
freq = 10
discr = 256
date = "12032002"
a = create_ab(date)[0]
b = create_ab(date)[1]

# пункт 8 - 100 значень КЧХ
t_f = np.linspace(0, 1, 256)
trans = signal.TransferFunction(b, a, dt=1)
t, y = signal.dimpulse(trans, n=discr)
w, h = signal.freqz([i[0] for i in y[0]], worN=discr)
angles = [np.unwrap(np.angle(h))[i] for i in range(100)]
w = [w[i] for i in range(100)]
h = [abs(h[i]) for i in range(100)]

# пункт 9 - побудова АЧХ та ФЧХ
fig, axs = plt.subplots(1, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("АЧХ")
axs[0][0].plot(w, h, '-g')
axs[0][0].plot(w, h, '.k')
plt.ylim(-0.1, 0.5)

plt.figure(1)
fig, axs = plt.subplots(1, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("ФЧХ")
axs[0][0].plot(w, angles, '-g')
axs[0][0].plot(w, angles, '.k')

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()




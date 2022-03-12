import time
import numpy as np
import scipy.signal.windows
from matplotlib import pyplot as plt
from scipy import signal
from matplotlib import cm

global figura
figura = 0


def axs_config(axises):
    for ax in axises.flat:
        ax.minorticks_on()
        ax.set(xlabel='x', ylabel='y')
        ax.grid(b=True, which='major', color='#666666', linestyle='-')
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        # ax.label_outer()
    return axises


def arr_sqsh(arr, size):
    return [arr[i] for i in range(int(size))]


def spectrograma(t, funct, discret, name):
    global figura

    f, t, sxx = signal.spectrogram(funct, fs=1, window=('tukey', 0.25), scaling='spectrum')

    if figura != 0:
        plt.figure(figura)
    figura += 1
    fig, axs = plt.subplots(1, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Спектрограма сигналу" + str(name))
    axs[0, 0].specgram(funct, Fs=discret, noverlap=discret)
    axs[0, 0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')


def build_window(t, type, time1_s, duration, discr):
    y = []
    w = signal.get_window(type, int(duration*discr)+1)
    w_c = 0
    for i in range(len(t)):
        if int(time1_s/discr) <= i <= int(time1_s/duration) + int(duration*discr):
            if w_c < len(w):
                y.append(w[w_c])
                w_c += 1
            else:
                y.append(0)
        else:
            y.append(0)
    return np.array(y)


start_time = time.time()


discr = 128
ampl = 1
last_s = 3
freq = 20

t = np.linspace(0, last_s, last_s*discr)
y = ampl * np.sin(2*np.pi*freq*t)

y1 = y.copy()
for i in range(len(t)):
    if 1.05 <= t[i] <= 1.05 + 10/discr:
        y1[i] = 0

y2 = y.copy()
for i in range(len(t)):
    if 2 <= t[i] <= 2 + 10/discr:
        y2[i] = 0

wind1 = build_window(t, 'tukey', 0, last_s, discr)
wind2 = build_window(t, 'tukey', 0, 1.7, discr)

spectrograma(t, y*wind1, discr, ' сигналу 1')
spectrograma(t, y1*wind1, discr, ' сигналу 2')
spectrograma(t, y2*wind1, discr, ' сигналу 3')

spectrograma(t, y*wind2, discr, ' сигналу 1')
spectrograma(t, y1*wind2, discr, ' сигналу 2')
spectrograma(t, y2*wind2, discr, ' сигналу 3')

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

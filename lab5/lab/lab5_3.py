import random
import time

import matplotlib.colors as clr
from matplotlib import pyplot as plt
from scipy import signal
import numpy as np

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


""", time1y, time2y, time1ap, time2ap"""


def spectrograma(t, funct, discret):
    global figura

    f, t, sxx = signal.spectrogram(funct, fs=1, window=('tukey', 0.25), scaling='spectrum')

    if figura != 0:
        plt.figure(figura)
    figura += 1
    fig, axs = plt.subplots(1, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Спектрограма сигналу")
    powerSpectrum, freqenciesFound, time, imageAxis = axs[0, 0].specgram(funct, Fs=discret)
    axs[0, 0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
    # axs[0, 0].set_xlim([0, 0.2])


def genrandom(t, ampli):
    y = []
    for i in range(len(t)):
        y.append(ampli * random.random())
    return np.array(y)


def gensquare(t, ampli, freq, start_s, secs):
    y = []
    for i in range(len(t)):
        if start_s <= t[i] <= start_s + secs / 2:
            y.append(ampli * signal.square(2 * np.pi * freq * (t[i] - start_s)))
        else:
            y.append(0)
    return np.array(y)


start_time = time.time()

ampl = 1
discr = 128
last_s = 15
freqs = [40, 1]
t = np.linspace(0, last_s, last_s * discr)
w = signal.get_window('tukey', len(t))
y1 = ampl * np.sin(2 * np.pi * freqs[0] * t)
y2 = gensquare(t, ampl, freqs[1], 10, 1)
y3 = genrandom(t, 2)
y4 = y1 + y2 + y3
print(len(y1))
print(len(w))
sy1 = y1 * w
sy2 = y2 * w
sy3 = y3 * w
sy4 = y4 * w

spectrograma(t, sy1, discr)
spectrograma(t, sy2, discr)
spectrograma(t, sy3, discr)
spectrograma(t, sy4, discr)

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

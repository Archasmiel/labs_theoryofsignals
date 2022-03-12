from scipy import signal
import time
import numpy as np
from matplotlib import pyplot as plt


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


start_time = time.time()

discr = 1000
ampl = 1
last_s = 10
freqs = [1/0.1, 1/1, 1/10]

t = np.linspace(0, last_s, last_s*discr)
freqq = np.fft.fftfreq(len(t), d=1.0/discr)
y1 = [np.random.rand(1) for i in range(len(t))]
y1_fft = np.abs(np.fft.fft(y1).real)

fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0, 0].set_title("Графік сигналу прямок. імпульсів частотою 10 Гц")
axs[0, 0].plot(t, y1)
axs[0, 0].set(xlabel='t', ylabel='signal')
axs[0, 0].set_xlim([0, 2])
axs[1, 0].set_title("Амплітудний спектр сигналу")
axs[1, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y1_fft) * y1_fft, len(y1_fft)/2))
axs[1, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
axs[1, 0].set_xlim([0, 20])


print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

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
last_s = 2
freqs = 3

t = np.linspace(0, last_s, last_s*discr)
freqq = np.fft.fftfreq(len(t), d=1.0/discr)
y1 = np.sin(2*np.pi*freqs*t)
y1_fft = np.fft.fft(y1)
y1_ifft = np.fft.ifft(y1_fft).real

fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0, 0].set_title("Графік сигналу синусоїди частотою 5 Гц")
axs[0, 0].plot(t, y1)
axs[0, 0].set(xlabel='t', ylabel='signal')
axs[1, 0].set_title("Графік сигналу, перетворений зворотнім перетворенням фур'є")
axs[1, 0].plot(t, y1_ifft)
axs[1, 0].set(xlabel='freq', ylabel='amplitudes of IFFT')

print("STD of ifft equals " + str(np.std(y1-y1_ifft)))


print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

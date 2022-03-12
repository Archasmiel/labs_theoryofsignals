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

discr = 128
ampl = 1
last_s = 1
freqs = [2, 2.5, 40, 100, 600]


t = np.linspace(0, last_s, discr)
signals = [ampl * np.sin(2*np.pi*i*t) for i in freqs]
ffts = [np.fft.fft(i) for i in signals]
freq = np.fft.fftfreq(len(t), d=1.0/discr)


for m in range(len(freqs)):
    if m != 0:
        plt.figure(m)
    fig, axs = plt.subplots(2, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0][0].set_title("Графік сигналу синусоїди частотою " + str(freqs[m]) + "Гц")
    axs[0][0].plot(t, signals[m])
    axs[0][0].set(xlabel='t', ylabel='signal')
    axs[1][0].set_title("Амплітудний спектр сигналу")
    axs[1][0].stem(arr_sqsh(freq, len(freq)/2), arr_sqsh(2/len(ffts[m]) * np.abs(ffts[m].real), len(ffts[m]) / 2))
    axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

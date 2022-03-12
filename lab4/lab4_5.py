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

discr = 512
ampl = 1
last_s = 30
freqs = [1/0.1, 1/1, 1/10]

t = np.linspace(0, last_s, last_s*discr)
freqq = np.fft.fftfreq(len(t), d=1.0/discr)
y1 = signal.square(2*np.pi*freqs[0]*t)
y1_fft = np.abs(np.fft.fft(y1).real)
y1_phase = np.unwrap(np.angle(y1))
y2 = signal.square(2*np.pi*freqs[1]*t)
y2_fft = np.abs(np.fft.fft(y2).real)
y2_phase = np.unwrap(np.angle(y2))
y3 = signal.square(2*np.pi*freqs[2]*t)
y3_fft = np.abs(np.fft.fft(y3).real)
y3_phase = np.unwrap(np.angle(y3))

fig, axs = plt.subplots(3, 1, squeeze=False)
axs = axs_config(axs)
axs[0, 0].set_title("Графік сигналу прямок. імпульсів частотою 10 Гц")
axs[0, 0].plot(t, y1)
axs[0, 0].set(xlabel='t', ylabel='signal')
axs[0, 0].set_xlim([0, 2])
axs[1, 0].set_title("Амплітудний спектр сигналу")
axs[1, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y1_fft) * y1_fft, len(y1_fft)/2))
axs[1, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
axs[1, 0].set_xlim([0, 20])
axs[2, 0].set_title("Фазовий спектр сигналу")
axs[2, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y1_phase) * y1_phase, len(y1_phase)/2))
axs[2, 0].set(xlabel='freq', ylabel='phase of FFT')
axs[2, 0].set_xlim([0, 4])

plt.figure(1)
fig, axs = plt.subplots(3, 1, squeeze=False)
axs = axs_config(axs)
axs[0, 0].set_title("Графік сигналу прямок. імпульсів частотою 1 Гц")
axs[0, 0].plot(t, y2)
axs[0, 0].set(xlabel='t', ylabel='signal')
axs[0, 0].set_xlim([0, 5])
axs[1, 0].set_title("Амплітудний спектр сигналу")
axs[1, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y2_fft) * y2_fft, len(y2_fft)/2))
axs[1, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
axs[1, 0].set_xlim([0, 5])
axs[2, 0].set_title("Фазовий спектр сигналу")
axs[2, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y2_phase) * y2_phase, len(y2_phase)/2))
axs[2, 0].set(xlabel='freq', ylabel='phase of FFT')
axs[2, 0].set_xlim([0, 5])

plt.figure(2)
fig, axs = plt.subplots(3, 1, squeeze=False)
axs = axs_config(axs)
axs[0, 0].set_title("Графік сигналу прямок. імпульсів частотою 0.1 Гц")
axs[0, 0].plot(t, y3)
axs[0, 0].set(xlabel='t', ylabel='signal')
axs[0, 0].set_xlim([0, 30])
axs[1, 0].set_title("Амплітудний спектр сигналу")
axs[1, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y3_fft) * y3_fft, len(y3_fft)/2))
axs[1, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
axs[1, 0].set_xlim([0, 2])
axs[2, 0].set_title("Фазовий спектр сигналу")
axs[2, 0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y3_phase) * y3_phase, len(y3_phase)/2))
axs[2, 0].set(xlabel='freq', ylabel='phase of FFT')
axs[2, 0].set_xlim([0, 2])

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

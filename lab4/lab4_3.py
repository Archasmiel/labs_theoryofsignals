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
last_s = 3
freq = 20

t = np.linspace(0, last_s, last_s*discr)
freqq = np.fft.fftfreq(len(t), d=1.0/discr)
y = ampl * np.sin(2*np.pi*freq*t)
y_fft = np.abs(np.fft.fft(y).real)

y1 = y.copy()
for i in range(len(t)):
    if 1.05 <= t[i] <= 1.05 + 10/discr:
        y1[i] = 0
y1_fft = np.abs(np.fft.fft(y1).real)

y2 = y.copy()
for i in range(len(t)):
    if 2 <= t[i] <= 2 + 10/discr:
        y2[i] = 0
y2_fft = np.abs(np.fft.fft(y2).real)

fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу синусоїди частотою 20 Гц")
axs[0][0].plot(t, y)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y_fft) * y_fft, len(y_fft)/2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

plt.figure(1)
fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу синусоїди частотою 20 та розривом в 1.05с")
axs[0][0].plot(t, y1)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Графік синусоїди перетвореної швидким перетворенням фур\'є")
axs[1][0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y1_fft) * y1_fft, len(y1_fft)/2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

plt.figure(2)
fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу синусоїди частотою 20 Гц та розривом в 2с")
axs[0][0].plot(t, y2)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freqq, len(freqq)/2), arr_sqsh(2/len(y2_fft) * y2_fft, len(y2_fft)/2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')


print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

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

discr = 256
ampl = 1
last_s1 = 10
last_s2 = 20
freqs = [10, 100]


t = np.linspace(0, last_s1, last_s1*discr)
freq1 = np.fft.fftfreq(len(t), d=1.0/discr)
signal1 = ampl * np.sin(2*np.pi*freqs[0]*t)
signal1_fft = np.abs(np.fft.fft(signal1).real)
signal2 = ampl * np.sin(2*np.pi*freqs[1]*t)
signal2_fft = np.abs(np.fft.fft(signal2).real)


signal1_fin = signal1 + signal2
signal1_finfft = np.abs(np.fft.fft(signal1_fin).real)
t_fin = np.linspace(0, 2*last_s1, 2*last_s1*discr)
freq2 = np.fft.fftfreq(len(t_fin), d=1.0/discr)
signal2_fin = np.append(signal1, signal2)
signal2_finfft = np.abs(np.fft.fft(signal2_fin).real)
signal3_fin = np.append(signal2, signal1)
signal3_finfft = np.abs(np.fft.fft(signal3_fin).real)


fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу синусоїди частотою " + str(freqs[0]) + "Гц")
axs[0][0].plot(t, signal1)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freq1, len(freq1)/2), arr_sqsh(2/len(signal1_fft) * signal1_fft, len(signal1_fft)/2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

plt.figure(1)
fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу синусоїди частотою " + str(freqs[1]) + "Гц")
axs[0][0].plot(t, signal2)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freq1, len(freq1)/2), arr_sqsh(2/len(signal2_fft) * signal2_fft, len(signal2_fft) / 2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

plt.figure(2)
fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу суми синусоїд частотою " + str(freqs[0]) + "Гц та " + str(freqs[1]) + "Гц")
axs[0][0].plot(t, signal1_fin)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freq1, len(freq1)/2), arr_sqsh(2/len(signal1_finfft) * signal1_finfft, len(signal1_finfft) / 2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

plt.figure(3)
fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу суми синусоїд 10 та 100 Гц")
axs[0][0].plot(t_fin, signal2_fin)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freq2, len(freq2)/2), arr_sqsh(2/len(signal2_finfft) * signal2_finfft, len(signal2_finfft) / 2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

plt.figure(4)
fig, axs = plt.subplots(2, 1, squeeze=False)
axs = axs_config(axs)
axs[0][0].set_title("Графік сигналу суми синусоїд 100 та 10 Гц")
axs[0][0].plot(t_fin, signal3_fin)
axs[0][0].set(xlabel='t', ylabel='signal')
axs[1][0].set_title("Амплітудний спектр сигналу")
axs[1][0].stem(arr_sqsh(freq2, len(freq2)/2), arr_sqsh(2/len(signal3_finfft) * signal3_finfft, len(signal3_finfft) / 2))
axs[1][0].set(xlabel='freq', ylabel='amplitudes of FFT')

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

import random
import moduleslab.labhelp as lh
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def random_array(time, amplitude):
    return np.random.normal(0, amplitude/2, time.shape[-1])


def low_butter_filter(freqp, freqs, freqs_freq):
    n, wn = signal.buttord(freqp*2/freqs_freq, freqs*2/freqs_freq, 3, 20, analog=False)
    b, a = signal.butter(n, wn, btype='lowpass', analog=False)
    return b, a


def gen_rect_signal(time, raw_signal, at_time, length, amplitude):
    for i in range(len(time)):
        if at_time+length >= time[i] >= at_time:
            raw_signal[i] = amplitude
    return raw_signal


rng = np.random.default_rng()

fs_freq = 128
last_s = 5
order = 7
t = np.linspace(0, last_s, last_s * fs_freq)

x = gen_rect_signal(t, [0] * len(t), 3, 0.1, 1)
noise = random_array(t, 0.25)
mix = x + noise


b, a = low_butter_filter(12, 18, fs_freq)
filtered = signal.filtfilt(b, a, mix)

w, h = signal.freqz(b, a)
plt.semilogx(w/2/np.pi, 20 * np.log10(abs(h)))
plt.title('Фільтр Низьких Частот')
plt.xlabel('Нормалізована частота')
plt.ylabel('Амплітуда, dB')
plt.grid(True)


g_names = ['Функція без шуму', 'Шум', 'Функція з шумом', 'Відфільтрована функція']
a_names = [g_names[i] + ' - АЧХ' for i in range(len(g_names))]
names = [g_names, a_names, []]
builds_array = [True, True, False]
times_array = [t, t, t, t]
graph_array = [x, noise, mix, filtered]

lh.multiple_graphs(plt, times_array, graph_array, fs_freq, builds_array, names)

# plt.tight_layout()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as s

d_freq = 128
T = 10
nA = 1
nf = 50

t = np.linspace(0, T - 1 / d_freq, T * d_freq)

pure = np.random.normal(0, 0.05, t.shape[-1])
noise = nA * np.sin(2 * np.pi * nf * t)
mix = pure + noise

sigs = [pure, noise, mix]

plt.figure(figsize=(19, 9))

titles = ('Сигнал', 'Мережевий шум', 'Сигнал з шумом')

for i, sig in enumerate(sigs):
    AS = (np.abs(np.fft.fft(sig)) / (t.shape[-1] / 2))[:int(t.shape[-1] / 2)]
    freq = np.fft.fftfreq(t.shape[-1], 1 / d_freq)[:int(t.shape[-1] / 2)]

    plt.subplot(2, 5, i + 1)
    plt.plot(t, sig)
    plt.grid(True)

    plt.title(titles[i])
    plt.xlabel('Час, с')
    plt.ylabel('Амплітуда, В')

    plt.subplot(2, 5, i + 1 + 5)
    plt.stem(freq, AS, linefmt='-r')
    plt.grid(True)

    plt.title('Амплітудний спектр')
    plt.xlabel('Частота, Гц')
    plt.ylabel('Амплітуда, В')

plt.subplot(1, 5, 4)

fp = np.array([0.9 * nf, 1.1 * nf])
fs = np.array([0.8 * nf, 1.2 * nf])

N, Wn = s.buttord(fp * 2 / d_freq, fs * 2 / d_freq, 3, 20, analog=False)
b, a = s.butter(N, Wn, 'bandstop', analog=False)
w, h = s.freqz(b, a)
plt.semilogx(w / 2 / np.pi, 20 * np.log10(abs(h)))
plt.title('Фільтр Низьких Частот')
plt.xlabel('Нормалізована частота')
plt.ylabel('Амплітуда, dB')
plt.grid(True)

filterd = s.lfilter(b, a, mix)

AS = (np.abs(np.fft.fft(filterd)) / (t.shape[-1] / 2))[:int(t.shape[-1] / 2)]
freq = np.fft.fftfreq(t.shape[-1], 1 / d_freq)[:int(t.shape[-1] / 2)]

plt.subplot(2, 5, 5)
plt.plot(t, filterd)
plt.grid(True)

plt.title('Відфільтрований сигнал')
plt.xlabel('Час, с')
plt.ylabel('Амплітуда, В')

plt.subplot(2, 5, 10)
plt.stem(freq, AS, linefmt='-r')
plt.grid(True)

plt.title('Амплітудний спектр')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплітуда, В')

plt.tight_layout()
plt.show()

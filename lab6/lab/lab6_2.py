import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as s

d_freq = 128
T = 1
f = 10
A = 1

t = np.linspace(0, T - 1 / d_freq, T * d_freq)

pure = A * np.sin(2 * np.pi * f * t)
noise = np.random.normal(0, 1.5, t.shape[-1])
mix = pure + noise

sigs = [pure, noise, mix]
filters = []

# ФНЧ
fp = 1.1 * f
fs = 1.25 * f

N, Wn = s.cheb1ord(fp * 2 / d_freq, fs * 2 / d_freq, 3, 40)
filters.append(s.cheby1(N, 3, Wn, 'lowpass'))

# ФВЧ
fp = 0.9 * f
fs = 0.75 * f

N, Wn = s.cheb1ord(fp * 2 / d_freq, fs * 2 / d_freq, 3, 40)
filters.append(s.cheby1(N, 3, Wn, 'highpass'))

# СФ
fp = np.array([0.9 * f, 1.1 * f])
fs = np.array([0.75 * f, 1.25 * f])

N, Wn = s.cheb1ord(fp * (2 / d_freq), fs * (2 / d_freq), 3, 40)
filters.append(s.cheby1(N, 1, Wn, 'bandpass'))

titles = ('Сигнал', 'Випадковий шум', 'Сигнал з шумом')
f_titles = ('Фільтр Низьких Частот', 'Фільтр Високих Частот', 'Смуговий Фільтр')

for j, [b, a] in enumerate(filters):
    plt.figure(figsize=(19, 9))
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

    w, h = s.freqz(b, a)
    print(h)
    plt.semilogx(w / 2 / np.pi, 20 * np.log10(abs(h)))
    plt.title(f_titles[j])
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

import time
import numpy as np
import scipy.signal.windows
from matplotlib import pyplot as plt
from scipy import signal
from matplotlib import cm

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


def spectrograma(t, funct, discret, name, seconds):
    global figura

    f, t, sxx = signal.spectrogram(funct, fs=1, window=('tukey', 0.25), scaling='spectrum')

    if figura != 0:
        plt.figure(figura)
    figura += 1
    fig, axs = plt.subplots(1, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Спектрограма сигналу" + str(name))
    axs[0, 0].specgram(funct, Fs=discret)
    axs[0, 0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
    axs[0, 0].set_xlim([0, seconds])


def spectrograma_perekr(t, funct, discret, name, perekr, seconds):
    global figura

    f, t, sxx = signal.spectrogram(funct, fs=1, window=('tukey', 0.25), scaling='spectrum')

    if figura != 0:
        plt.figure(figura)
    figura += 1
    fig, axs = plt.subplots(1, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Спектрограма сигналу" + str(name))
    axs[0, 0].specgram(funct, Fs=discret, noverlap=discret*perekr)
    axs[0, 0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')
    axs[0, 0].set_xlim([0, seconds])


def spectrogram3d(funct):
    global figura

    f, t, sxx = signal.spectrogram(funct, fs=1, window=('tukey', 0.25), scaling='spectrum')

    if figura != 0:
        plt.figure(figura)
    figura += 1

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = []
    y = []

    for counter, i in enumerate(f):
        x.append(np.array([i for k in t]))
        y.append(t)

    ax.plot_surface(np.array(x), np.array(y), 10*np.log10(sxx))


def build_window(t, type, time1_s, duration, discr):
    y = []
    w = signal.get_window(type, int(duration*discr)+1)
    w_c = 0
    for i in range(len(t)):
        if int(time1_s/discr) <= i <= int(time1_s/duration) + int(duration*discr):
            y.append(w[w_c])
            w_c += 1
        else:
            y.append(0)
    return np.array(y)


start_time = time.time()

discr = 256
ampl = 1
last_s1 = 10
last_s2 = 20
freqs = [10, 100]


t = np.linspace(0, last_s1, last_s1*discr)
w1 = scipy.signal.windows.get_window('tukey', len(t))
signal1 = ampl * np.sin(2*np.pi*freqs[0]*t)
signal2 = ampl * np.sin(2*np.pi*freqs[1]*t)
signal1_fin = signal1 + signal2


t_fin = np.linspace(0, last_s2, last_s2*discr)
w2 = scipy.signal.windows.get_window('tukey', len(t_fin))
signal2_fin = np.append(signal1, signal2)
signal3_fin = np.append(signal2, signal1)

wind1 = build_window(t, 'tukey', 0, 0.1, discr)
wind11 = build_window(t_fin, 'tukey', 0, 0.1, 2*discr)
wind2 = build_window(t, 'tukey', 0, 2, discr)
wind21 = build_window(t_fin, 'tukey', 0, 2, 2*discr)
wind3 = build_window(t, 'tukey', 0, 1, discr)
wind31 = build_window(t_fin, 'tukey', 0, 1, 2*discr)


# 0.1 sec без перекриття
spectrograma(t, signal1_fin*wind1, discr, ' сигналу 1 (сума сигналів) (вікно 0.1 сек)', 1)
spectrograma(t_fin, signal2_fin*wind11, discr, ' сигналу 2 (s1 + s2) (вікно 0.1 сек)', 1)
spectrograma(t_fin, signal3_fin*wind11, discr, ' сигналу 3 (s2 + s1) (вікно 0.1 сек)', 1)

# 2 sec без перекриття
spectrograma(t, signal1_fin*wind2, discr, ' сигналу 1 (сума сигналів) (вікно 2 сек)', 2)
spectrograma(t_fin, signal2_fin*wind21, discr, ' сигналу 2 (s1 + s2) (вікно 2 сек)', 2)
spectrograma(t_fin, signal3_fin*wind21, discr, ' сигналу 3 (s2 + s1) (вікно 2 сек)', 2)

# 1 sec з перекриттям 1/2
spectrograma_perekr(t, signal1_fin*wind3, discr, ' сигналу 1 перекритий (сума сигналів) (вікно 0.1 сек)', 1/2, 1)
spectrograma_perekr(t_fin, signal2_fin*wind31, discr, ' сигналу 2 перекритий (s1 + s2) (вікно 0.1 сек)', 1/2, 1)
spectrograma_perekr(t_fin, signal3_fin*wind31, discr, ' сигналу 3 перекритий (s2 + s1) (вікно 0.1 сек)', 1/2, 1)

# 3d spectrogram
spectrogram3d(signal1_fin*wind2)
spectrogram3d(signal3_fin*wind21)

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

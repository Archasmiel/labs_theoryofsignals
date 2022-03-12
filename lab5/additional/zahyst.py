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


def spectrograma(t, funct, discret):
    global figura

    f, t, sxx = signal.spectrogram(funct, fs=1, window=('tukey', 0.25), scaling='spectrum')

    if figura != 0:
        plt.figure(figura)
    figura += 1
    fig, axs = plt.subplots(1, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Спектрограма сигналу")
    axs[0, 0].specgram(funct, Fs=discret)
    axs[0, 0].set(xlabel='Time [sec]', ylabel='Frequency [Hz]')


start_time = time.time()

last_s = 5
discr = 380
freq = [5, 10, 30, 50, 100]
t = np.linspace(0, last_s, last_s*discr)
s1 = np.sin(2*np.pi*t*freq[0])
s2 = np.sin(2*np.pi*t*freq[1])
s3 = np.sin(2*np.pi*t*freq[2])
s4 = np.sin(2*np.pi*t*freq[3])
s5 = np.sin(2*np.pi*t*freq[4])
s6 = s1+s2+s3+s4+s5

spectrograma(t, s6, discr)

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

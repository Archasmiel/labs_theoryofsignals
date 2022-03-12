from scipy import signal
import time
import numpy as np
from matplotlib import pyplot as plt

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


def draw_graphics(t, funct, discret, time1y, time2y, time1ap, time2ap):
    global figura
    freqq = np.fft.fftfreq(len(t), d=1.0 / discret)
    yfft = np.fft.fft(funct)
    yphase = np.unwrap(np.angle(yfft))

    if figura != 0:
        plt.figure(figura)
    figura += 1
    fig, axs = plt.subplots(3, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Графік сигналу")
    axs[0, 0].plot(t, funct)
    axs[0, 0].set(xlabel='t', ylabel='signal')
    axs[0, 0].set_xlim([time1y, time2y])

    axs[1, 0].set_title("Амплітудний спектр сигналу")
    axs[1, 0].stem(arr_sqsh(freqq, len(freqq) / 2), arr_sqsh(2 / len(yfft) * yfft, len(yfft) / 2))
    axs[1, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
    axs[1, 0].set_xlim([time1ap, time2ap])

    axs[2, 0].set_title("Фазовий спектр сигналу")
    axs[2, 0].stem(arr_sqsh(freqq, len(freqq) / 2), arr_sqsh(2 / len(yphase) * yphase, len(yphase) / 2))
    axs[2, 0].set(xlabel='freq', ylabel='phase of FFT')
    axs[2, 0].set_xlim([time1ap, time2ap])


start_time = time.time()

discr = 1000
t1 = 0
t2 = 2
ampl = 1
freqs = 3


t = np.linspace(t1, t2, int((t2-t1)*discr))
y = ampl * np.sin(2*np.pi*freqs*t)
draw_graphics(t, y, discr, 0.5, 1, 0, 20)
draw_graphics(t, y, discr, 1, 2, 0, 40)


print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

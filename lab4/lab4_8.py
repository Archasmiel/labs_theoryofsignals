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

vidliks = [0, 10, 100, 1000, 10000]
discr = 1000
ampl = 1
last_s = 1
freqs = 20.5

t1 = np.linspace(0, last_s, last_s*discr)
freq1 = np.fft.fftfreq(len(t1), d=1.0/discr)
y1 = ampl*np.sin(2*np.pi*freqs*t1)
y1_fft = np.abs(np.fft.fft(y1).real)

t2 = np.copy(t1)
y2 = np.copy(y1)
for i in range(vidliks[1]):
    t2 = np.append(t2, last_s + i / discr)
    y2 = np.append(y2, 0)
freq2 = np.fft.fftfreq(len(t2), d=1.0/discr)
y2_fft = np.abs(np.fft.fft(y2).real)

t3 = np.copy(t1)
y3 = np.copy(y1)
for i in range(vidliks[2]):
    t3 = np.append(t3, last_s + i / discr)
    y3 = np.append(y3, 0)
freq3 = np.fft.fftfreq(len(t3), d=1.0/discr)
y3_fft = np.abs(np.fft.fft(y3).real)

t4 = np.copy(t1)
y4 = np.copy(y1)
for i in range(vidliks[3]):
    t4 = np.append(t4, last_s + i / discr)
    y4 = np.append(y4, 0)
freq4 = np.fft.fftfreq(len(t4), d=1.0/discr)
y4_fft = np.abs(np.fft.fft(y4).real)

t5 = np.copy(t1)
y5 = np.copy(y1)
for i in range(vidliks[4]):
    t5 = np.append(t5, last_s + i / discr)
    y5 = np.append(y5, 0)
freq5 = np.fft.fftfreq(len(t5), d=1.0/discr)
y5_fft = np.abs(np.fft.fft(y5).real)

ts = [t1, t2, t3, t4, t5]
ys = [y1, y2, y3, y4, y5]
print(y5)
frequences = [freq1, freq2, freq3, freq4, freq5]
yffts = [y1_fft, y2_fft, y3_fft, y4_fft, y5_fft]

for i in range(len(ts)):
    fig, axs = plt.subplots(2, 1, squeeze=False)
    axs = axs_config(axs)
    axs[0, 0].set_title("Графік сигналу синусоїди частотою 20.5Гц з " + str(vidliks[i]) + " нульовими відліками")
    axs[0, 0].plot(ts[i], ys[i])
    axs[0, 0].set(xlabel='t', ylabel='signal')
    axs[1, 0].set_title("Амплітудний спектр сигналу")
    axs[1, 0].stem(arr_sqsh(frequences[i], len(frequences[i])/2), arr_sqsh(2/len(yffts[i]) * yffts[i], len(yffts[i])/2))
    axs[1, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
    axs[1, 0].set_xlim([18, 23])


print("--- Runtime was %s seconds ---" % (time.time() - start_time))
plt.show()

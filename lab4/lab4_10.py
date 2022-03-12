import matplotlib.pyplot as plt
import scipy.signal as sign

figura = 0

def PSD(filename):
    global figura
    if figura != 0:
        plt.figure(figura)
    figura += 1
    with open("out.txt", "r") as f:
        t = [float(x) for x in f.readline().split()]
        y = [float(x) for x in f.readline().split()]

    f, psd_den = sign.periodogram(y)
    plt.semilogy(f, psd_den)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD density [V**2/Hz]')
    plt.show()


PSD("out.txt")
import time
from scipy import signal
import numpy as np
from moduleslab import labhelp


start_time = time.time()

ampl = 1
discr = 128
last_s = 1
freqs = [2, 2.5]
t = np.linspace(0, last_s, discr)
w = signal.get_window('tukey', len(t))
y1 = ampl * np.sin(2*np.pi*freqs[0]*t)
y2 = ampl * np.sin(2*np.pi*freqs[1]*t)
sfft_y1 = y1 * w
sfft_y2 = y2 * w

labhelp.draw_graphics(t, y1, discr, 0, t[len(t)-1], 0, discr / 2, True, True, False, "Синусоїда частотою 2 Гц", "АЧХ синусоїди", "ФЧХ синусоїди")
labhelp.draw_graphics(t, sfft_y1, discr, 0, t[len(t)-1], 0, discr / 2, True, True, False, "Синусоїда з вікном частотою 2 Гц", "АЧХ синусоїди", "ФЧХ синусоїди")
labhelp.draw_graphics(t, y2, discr, 0, t[len(t)-1], 0, discr / 2, True, True, False, "Синусоїда частотою 2.5 Гц", "АЧХ синусоїди", "ФЧХ синусоїди")
labhelp.draw_graphics(t, sfft_y2, discr, 0, t[len(t)-1], 0, discr / 2, True, True, False, "Синусоїда з вікном частотою 2.5 Гц", "АЧХ синусоїди", "ФЧХ синусоїди")

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
import time
from scipy import signal
import numpy as np
from lab5.moduleslab import labhelp

discr = 256

start_time = time.time()

labhelp.draw_graphics(np.linspace(0, discr, discr), signal.get_window('tukey', 256), discr, 0, 256, 0, discr / 2, True, True, False, "Віконна функція Тьюкі", "АЧХ віконної функції Тьюкі", "ФЧХ віконної функції Тьюкі")

print("--- Runtime was %s seconds ---" % (time.time() - start_time))
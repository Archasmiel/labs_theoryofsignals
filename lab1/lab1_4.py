import numpy as np
from matplotlib import pyplot as plt

# переменные
fig, axs = plt.subplots(constrained_layout=True)

# задание х и у для отрисовки
x = np.linspace(-10, 10, 256)

# украшение графиков

axs.minorticks_on()
axs.set(xlabel='x', ylabel='y')
axs.grid(b=True, which='major', color='#666666', linestyle='-')
axs.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# общая легенда для оси х (не будет повторения по горизонтали и вертикали)
axs.label_outer()

axs.plot(x, x, 'tab:green')
axs.set(label='график')


plt.show()

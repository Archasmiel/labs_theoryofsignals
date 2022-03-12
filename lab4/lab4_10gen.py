import numpy as np

ampl = 1
freqs = 12
discr = 256
t1 = 0
t2 = 2

t = np.linspace(t1, t2, int((t2-t1)*discr))
y = ampl * np.sin(2*np.pi*freqs*t)

with open("out.txt", "w") as f:
    for i in t:
        f.write(str(i) + " ")
    f.write("\n")
    for i in y:
        f.write(str(i) + " ")
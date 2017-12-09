import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update():
    # xdata.append(frame)
    # ydata.append(np.sin(frame))
    xdata = [random.random]
    ydata = [np.sin(frame)]
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, init_func=init, blit=True)
plt.show()
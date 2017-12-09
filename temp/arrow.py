import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata = [0]
ydata = [0]
# arrow = ax.arrow(xdata, ydata, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
# ln, = plt.arrow(xdata, ydata, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k', animated=True)
ln, = plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro', animated=True)

def init():
    # ax.set_xlim(0, 2*np.pi)
    # ax.set_ylim(-1, 1)
    return ln,

def update(frame, xdata, ydata):
    xdata += frame
    ydata += frame
    # arrow = ax.arrow(xdata, ydata, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k', animated=True)
    ln.set_data(xdata, ydata)
    return ln,


# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    # init_func=init, blit=True)

animation = FuncAnimation(fig, update, frames=1, fargs = [xdata, ydata],init_func=init, blit=True)
plt.show()
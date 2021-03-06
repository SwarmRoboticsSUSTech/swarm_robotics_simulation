import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches

robot_nums = 4

class Robot: #TODO
    def __init__(self, x_init, y_init, k, speed_init):
        self.x = x_init
        self.y = y_init
        self.dx = 1/math.sqrt(1+k**2)
        self.dy = self.dx * k
        self.speed = speed_init
    
    def random_walk():
        pass

    def follow():
        pass
    
    def talk():
        pass

    def update_self():
        pass

robots = []
for i in range(robot_nums):
    robots.append(Robot(random.randint(0, 10), random.randint(0, 10), random.randint(-10, 10), 1))



fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    # xdata.append(frame)
    # ydata.append(np.sin(frame))
    xdata = [random.randint(0, 10)]
    ydata = [random.randint(0, 10)]
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=None, init_func=init, blit=True)
plt.show()

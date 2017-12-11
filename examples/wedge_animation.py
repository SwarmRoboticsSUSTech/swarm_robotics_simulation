import random
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches

robot_nums = 4

class Robot: #TODO
    def __init__(self, x_init, y_init, init_angle, speed_init):
        self.x = x_init
        self.y = y_init
        self.angle = init_angle
        self.k = math.tan(self.angle)
        self.dx = 1 / math.sqrt(1 + self.k ** 2)
        self.dy = math.sqrt(1 - self.dx**2)
        self.speed = speed_init
    
    # def random_walk(self):
        

    def follow(self):
        pass
    
    def talk(self):
        pass

    def update_direction(self): #TODO stuck in corner and border.
        if (self.x + self.dx) < 10 and (self.x + self.dx) > -10 and (self.y + self.dy) < 10 and (self.y + self.dx) > -10:
            self.x += self.dx    
            self.y += self.dy
        else:
            self.angle = self.angle + math.pi / 4
        self.angle = (self.angle + random.uniform(-math.pi/4, math.pi/4)) % (2 * math.pi)
        self.k = math.tan(self.angle)
        self.dx = 1 / math.sqrt(1 + self.k ** 2)
        self.dy = math.sqrt(1 - self.dx**2)
        

robot0 =  Robot(random.randint(-10, 10), random.randint(-10, 10), 0, 1)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
plt.grid(True)
# patch_one = matplotlib.patches.Circle((0, 0), 1)
patch_one = matplotlib.patches.Wedge((robot0.x,robot0.y), 1, robot0.angle - 25, robot0.angle + 25)

# initialization function: plot the background of each frame
def init():
    patch_one.radius = 1
    ax.add_patch(patch_one)
    return patch_one,

# animation function.  This is called sequentially
def animate(frame):
    robot0.update_direction()
    # robot0.random_walk()
    patch_one.set_center((robot0.x, robot0.y))
    patch_one.set_theta1(robot0.angle - 25)
    patch_one.set_theta2(robot0.angle + 25)
    patch_one._recompute_path()
    return patch_one,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=1000, blit=True)

plt.show()
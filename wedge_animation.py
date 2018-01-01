'''
Attention! radians and degrees!
'''
import random
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches
from scipy.spatial import ConvexHull
from matplotlib.path import Path
import sys
# from collections import deque

robot_nums = int(sys.argv[1])
update_interval = 100
speed_init = 1
search_radius = 1
follow_num = 1

class Robot:
    def __init__(self, id, x_init, y_init, init_angle, speed_init):
        self.id = id
        self.speed = speed_init
        self.x = x_init
        self.y = y_init
        self.previous_x = self.x
        self.previous_y = self.y
        self.angle = init_angle
        self.k = math.tan(math.radians(self.angle))
        self.dx = self.speed / math.sqrt(1 + self.k ** 2)
        self.dy = math.sqrt(self.speed**2 - self.dx**2)

        self.is_following = None
        self.follower = None
        
        # self.queue_list = deque(self.id)
        self.queue_list = [self.id]
        self.point_A = (self.x + search_radius * math.cos(math.radians(self.angle - 25)), self.y + search_radius * math.sin(math.radians(self.angle - 25)))
        self.point_B = (self.x + search_radius * math.cos(math.radians(self.angle + 25)), self.y + search_radius * math.sin(math.radians(self.angle + 25)))
        self.point_C = (self.x + search_radius * math.cos(math.radians(self.angle + 90)), self.y + search_radius * math.sin(math.radians(self.angle + 90)))
        self.point_D = (self.x + search_radius * math.cos(math.radians(self.angle + 270)), self.y + search_radius * math.sin(math.radians(self.angle + 270)))

    def follow(self, following_robot):
        self.angle = angle_between((following_robot.previous_x - self.x, following_robot.previous_y - self.y), (1,0))
        self.k = math.tan(math.radians(self.angle))
        self.x = following_robot.previous_x
        self.y = following_robot.previous_y

    def judge_overlaping(self, another_robot):
        points = np.array([(self.x, self.y), self.point_A, self.point_B])
        test_points = np.array([(another_robot.x, another_robot.y), another_robot.point_C, another_robot.point_D])
        hull = ConvexHull( points )
        hull_path = Path( points[hull.vertices] )
        if hull_path.contains_points(test_points).any() and self.queue_list[0] != another_robot.id:
            self.is_following = another_robot.id
            self.queue_list = self.queue_list + another_robot.queue_list
            another_robot.follower = self.id
            # another_robot.queue_list = self.queue_list
            for i in self.queue_list:
                robots[i].queue_list = self.queue_list
            print(self.id, " has find ", another_robot.id)
            global follow_num
            follow_num += 1
            print(self.queue_list)

    def update_previous_coordinates(self):
        self.previous_x = self.x
        self.previous_y = self.y

    def update_itself(self):
        '''
        calculate angle first, then calculate dx and dy
        '''
        if self.is_following is None:
            if (self.x + self.dx) < 10 and (self.x + self.dx) > -10 and (self.y + self.dy) < 10 and (self.y + self.dy) > -10:
                self.x += self.dx
                self.y += self.dy
            else:
                self.angle = self.angle + 45
            self.angle = (self.angle + random.uniform(-45, 45)) % 360
            self.k = math.tan(math.radians(self.angle))
            if self.angle >= 0 and self.angle < 90:
                self.dx = self.speed / math.sqrt(1 + self.k ** 2)
                self.dy = math.sqrt(self.speed**2 - self.dx**2)
            elif self.angle >= 90 and self.angle < 180:
                self.dx = - self.speed / math.sqrt(1 + self.k ** 2)
                self.dy = math.sqrt(self.speed**2 - self.dx ** 2)
            elif self.angle >= 180 and self.angle < 270:
                self.dx = - self.speed / math.sqrt(1 + self.k ** 2)
                self.dy = - math.sqrt(self.speed**2 - self.dx ** 2)
            elif self.angle >= 270 and self.angle < 360:
                self.dx = self.speed / math.sqrt(1 + self.k ** 2)
                self.dy = - math.sqrt(self.speed**2 - self.dx ** 2)
        else:
            self.follow(robots[self.is_following])
        self.point_A = (self.x + search_radius * math.cos(math.radians(self.angle - 25)), self.y + search_radius * math.sin(math.radians(self.angle - 25)))
        self.point_B = (self.x + search_radius * math.cos(math.radians(self.angle + 25)), self.y + search_radius * math.sin(math.radians(self.angle + 25)))
        self.point_C = (self.x + search_radius * math.cos(math.radians(self.angle + 90)), self.y + search_radius * math.sin(math.radians(self.angle + 90)))
        self.point_D = (self.x + search_radius * math.cos(math.radians(self.angle + 270)), self.y + search_radius * math.sin(math.radians(self.angle + 270)))

robots = [Robot(i, random.randint(-10, 10), random.randint(-10,
                                                           10), 0, speed_init) for i in range(robot_nums)]


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(8,8))
ax = plt.axes(xlim=(-12, 12), ylim=(-12, 12))
# plt.grid(True)
patchs = [matplotlib.patches.Wedge(
    (robot_i.x, robot_i.y), search_radius, robot_i.angle - 25, robot_i.angle + 25) for robot_i in robots]
patchs_tail = [matplotlib.patches.Wedge(
    (robot_i.x, robot_i.y), search_radius, robot_i.angle + 90, robot_i.angle + 270) for robot_i in robots]

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def continue_calaulate():
    if follow_num == robot_nums:
        return False
    else:
        return True

def init():
    for i in range(robot_nums):
        patchs[i].radius = search_radius
        patchs_tail[i].radius = search_radius
        ax.add_patch(patchs[i])
        ax.add_patch(patchs_tail[i])
    return patchs + patchs_tail


# animation function.  This is called sequentially
def animate(frame):
    for i in range(robot_nums):
        robots[i].update_itself()
    for i in range(robot_nums):
        robots[i].update_previous_coordinates()
    if continue_calaulate():
        for i in range(robot_nums):
            if robots[i].is_following is None:
                another_robot_list = [robots[j] for j in range(robot_nums) if j!=i and robots[j].follower is None]
                for another_robot in another_robot_list:
                    if robots[i].is_following is None and another_robot.is_following != i:
                        robots[i].judge_overlaping(another_robot)
    for i in range(robot_nums):
        patchs[i].set_center((robots[i].x, robots[i].y))
        patchs_tail[i].set_center((robots[i].x, robots[i].y))

        patchs[i].set_theta1(robots[i].angle - 25)
        patchs[i].set_theta2(robots[i].angle + 25)
        patchs_tail[i].set_theta1(robots[i].angle + 90)
        patchs_tail[i].set_theta2(robots[i].angle + 270)

        patchs[i].set_color('r')
        patchs_tail[i].set_color('b')

        patchs[i]._recompute_path()
        patchs_tail[i]._recompute_path()
    return patchs + patchs_tail


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1, interval=update_interval, blit=True)

plt.show()

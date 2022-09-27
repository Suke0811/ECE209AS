import time

import numpy as np
from rems.typing import DefDict
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.cm import get_cmap

class Grid2DMap:
    def __init__(self, x=5, y=5):
        self.x = int(x)
        self.y = int(y)
        self.grid_keys = self.generate_grid_keys()
        self.grid_world = DefDict(self.grid_keys.flatten().tolist(), dtype=str, shape=(self.y, self.x))
        self.grid_value = DefDict(self.grid_keys.flatten().tolist(), dtype=dict(up=float, down=float, right=float, left=float, stay=float), shape=(self.y, self.x))
        self.grid_index = DefDict(self.grid_keys.flatten().tolist(), shape=(self.y, self.x))
        for k in self.grid_index.keys():
            self.grid_index[k] = (int(k[0]), int(k[1]))
        self.grid_reward = DefDict(self.grid_keys.flatten().tolist(), dtype=int, shape=(self.y, self.x))
        self._goals = {}
        self._obstacles = {}

        self.fig = None
        self.ax = None

    def generate_grid_keys(self):
        xy = np.meshgrid(range(self.x), range(self.y))
        l = [str(v0 ) +str(v1) for v0, v1 in zip(xy[0].flatten(), xy[1].flatten())]
        return np.array([v for v in reversed(np.array(l).reshape(self.y, self.x))])

    def set_goals(self, goal):
        self._goals.update(goal)
        self.grid_world.update(goal)
        self.grid_reward.update(dict.fromkeys(goal, 1))

    def set_obstacles(self, obstacles):
        self._obstacles.update(obstacles)
        self.grid_world.update(obstacles)
        self.grid_reward.update(dict.fromkeys(obstacles, -1))

    def get_goals(self):
        return self._goals

    def get_obstacles(self):
        return self._obstacles

    def if_obstacle(self, x, y):
        if self._obstacles.get(str(int(x))+str(int(y))) is not None:
            return True
        else:
            return False

    def get_location(self, x, y):
        return self.grid_world.get(str(int(x))+str(int(y)))

    def get_index(self, key):
        return self.grid_index[key]



    def show(self, x, y):
        if self.fig is None:
            self.fig, self.ax = plt.subplots()
            self.line, = self.ax.plot([], marker="p", ms=10)
        vmin = -1
        vmax = 1
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)

        grid_plot = np.array([v for v in reversed(self.grid_reward.ndarray())])

        mat = self.ax.matshow(grid_plot, origin='lower', norm=norm, cmap='RdBu')
        self.line.set_data(x,y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


if __name__ == '__main__':
    g = Grid2DMap()
    OBSTACLE = 'obs'
    g.set_obstacles({'11': OBSTACLE, '21': OBSTACLE, '13': OBSTACLE, '23': OBSTACLE})
    g.set_goals({'20': 'Rs', '22': 'Rd'})
    g.show(0, 2)
    plt.show(block=False)
    time.sleep(1)
    g.show(1, 1)
    time.sleep(1)
    g.show(4, 4)
    time.sleep(1)
    pass

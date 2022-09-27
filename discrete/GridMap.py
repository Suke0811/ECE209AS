import time

import numpy as np
from rems.typing import DefDict
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.cm import get_cmap

class Grid2DMap:
    def __init__(self, grid_location, grid_shape):
        self.x = int(grid_shape[0]) # grid x
        self.y = int(grid_shape[1]) # grid y

        self.grid_keys = grid_location
        self.grid_world = DefDict(grid_location, shape=(self.y, self.x)) # dictionary like object

        self.grid_plot = DefDict(list(grid_location.keys()), dtype=float, shape=(self.y, self.x))
        self._goals = []
        self._obstacles = []

        self.fig = None
        self.ax = None
        self.print_info()

    def print_info(self):
        print(f"Your grid map keys: ")
        print(self.grid_keys)


    def generate_grid_keys(self):
        xy = np.meshgrid(range(self.x), range(self.y))
        l = [str(v0 ) +str(v1) for v0, v1 in zip(xy[0].flatten(), xy[1].flatten())]
        return np.array([v for v in reversed(np.array(l).reshape(self.y, self.x))])

    def set_goals(self, goal_lists):
        self._goals.extend(goal_lists)
        self.grid_plot.update(dict.fromkeys(goal_lists, 1))


    def set_obstacles(self, obstacle_lists, obstacle_plot_value=None):
        self._obstacles.extend(obstacle_lists)
        self.grid_plot.update(dict.fromkeys(obstacle_lists, -1))

    def get_goals(self):
        return self._goals

    def get_obstacles(self):
        return self._obstacles

    def if_obstacle(self, state_name):
        if state_name in self._obstacles:
            return True
        else:
            return False

    def get_location(self, state_name):
        if state_name in self.grid_world.keys():
            return self.grid_world.get(state_name)
        else:
            return (-1,-1)

    def show(self, x, y):
        if self.fig is None:
            self.fig, self.ax = plt.subplots()
            self.line, = self.ax.plot([], marker="p", ms=10)
        vmin = -1
        vmax = 1
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)

        grid_plot = np.array([v for v in reversed(self.grid_plot.ndarray())])

        mat = self.ax.matshow(grid_plot, origin='lower', norm=norm, cmap='RdBu')
        self.line.set_data(x,y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


if __name__ == '__main__':
    grid_location = dict(
        s04=(0, 4), s14=(1, 4), s24=(2, 4), s34=(3, 4), s44=(4, 4),
        s03=(0, 3), s13=(1, 3), s23=(2, 3), s33=(3, 3), s43=(4, 3),
        s02=(0, 2), s12=(1, 2), s22=(2, 2), s32=(3, 2), s42=(4, 2),
        s01=(0, 1), s11=(1, 1), s21=(2, 1), s31=(3, 1), s41=(4, 1),
        s00=(0, 0), s10=(1, 0), s20=(2, 0), s30=(3, 0), s40=(4, 0),
    )

    grid_shape = (5, 5)
    g = Grid2DMap(grid_location, grid_shape)
    g.set_obstacles(['s11', 's21', 's13', 's23'])
    g.set_goals(['s20', 's22'])
    g.show(0, 2)
    plt.show(block=False)
    time.sleep(1)
    g.show(1, 1)
    time.sleep(1)
    g.show(4, 4)
    time.sleep(1)
    pass

from rems.outputs import OutputBase
from matplotlib import pyplot as plt

class LineAnimation(OutputBase):
    def __init__(self):
        super().__init__()
        self.fig = None

    def process(self, state, inpt, outpt, timestamp, info):
        super().process(state, inpt, outpt, timestamp, info)
        list_data=list(map(lambda d: d.list(), self._states))
        ret_list = []
        for i in range(2):
            ret_list.append([d[i] for d in list_data])
        self.show(*ret_list)


    def show(self, y, v):
        if self.fig is None:
            self.fig, self.ax = plt.subplots()
            self.line, = self.ax.plot([], marker="p", ms=10)
            self.ax.set(xlabel='y', ylabel='v')
            plt.show(block=False)


        self.line.set_data(y, v)
        self.fig.canvas.draw()
        MARGIN = 1
        self.ax.set_xlim([min(y) - MARGIN, max(y) + MARGIN])
        self.ax.set_ylim([min(v) - MARGIN, max(v) + MARGIN])
        self.fig.canvas.flush_events()

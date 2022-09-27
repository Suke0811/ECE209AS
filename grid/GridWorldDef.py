from rems.robots import RobotDefBase
from rems.typing import DefDict
from rems.typing import MapRule

# input rule
stay_rule = MapRule(['up', 'down', 'right', 'left'],
                    lambda u, d, r, l: not bool(u+d+r+l),
                    ['stay'],
                    to_list=True)


class GridWorldDef(RobotDefBase):
    def __init__(self, grid, prob_error=0):
        super(GridWorldDef, self).__init__()
        self.grid = grid
        self.prob_error = prob_error


    def define(self, *args, **kwargs):
        # action space (up, down, right, left, stay)
        self.inpt.add_def(dict(up=bool, down=bool, right=bool, left=bool, stay=bool)).set_rule([stay_rule])
        # state space (x, y)
        self.state.add_def(dict(x=float, y=float))
        # observation space (o)
        self.outpt.add_def(dict(o=float))
        super().define()

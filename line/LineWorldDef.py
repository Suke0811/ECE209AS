import numpy as np
from rems.robots import RobotDefBase
from rems.typing import DefDict
from rems.typing import MapRule, UnitType

# input rule
rocket_keyboard = MapRule(['up', 'down'],
                    lambda u, d: u-d,
                    ['f'],
                    to_list=True)


class LineWorldDef(RobotDefBase):
    def __init__(self, prob_crash=0.1, mass=1, v_max=10, y_max=100, amp=1):
        super().__init__()
        self.mass = mass
        self.prob_crash = prob_crash
        self.v_max = v_max
        self.y_max = y_max
        self.amp = amp

    def define(self, *args, **kwargs):
        # action space (up, down, right, left, stay)
        self.inpt.add_def(dict(f=float)).set_rule(rocket_keyboard)
        # state space (x, y)
        self.state.add_def(dict(y=float, v=float))
        # outputs
        self.outpt.add_def(dict(y=float))
        super().define()

    # this can be here too
    def potential_field(self, y):
        pot = self._pf * int(self.amp*np.sin(2*np.pi*y/self.y_max))
        return pot

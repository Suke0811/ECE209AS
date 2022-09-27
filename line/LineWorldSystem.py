from rems.robots import RobotBase
import numpy as np


import numpy as np
from rems.robots import RobotDefBase
from rems.typing import DefDict
from rems.typing import MapRule, UnitType

# input rule
rocket_keyboard = MapRule(['up', 'down'],
                    lambda u, d: u-d,
                    ['f'],
                    to_list=True)


class LineWorldSystem(RobotBase):
    def __init__(self,  prob_crash=0.1, mass=1, v_max=10, y_max=50, amp=1,potential_field=True, sensor_noise=True, speed_wobble=True):
        super().__init__()
        self.mass = mass
        self.prob_crash = prob_crash
        self.v_max = v_max
        self.y_max = y_max
        self.amp = amp

        self._pf = potential_field
        self._sn = sensor_noise
        self._sp = speed_wobble

    def define(self, *args, **kwargs):
        # action space (up, down, right, left, stay)
        self.inpt.add_def(dict(f=float)).set_rule(rocket_keyboard)
        # state space (x, y)
        self.state.add_def(dict(y=float, v=float))
        # outputs
        self.outpt.add_def(dict(y=float))
        super().define()

    def drive(self, inpt, t):
        y, v = self.state.list()
        f = self.inpt.get('f')
        y_n = y + v
        v_n = v + 1/self.mass * (f + self.potential_field(y))
        v_n = self.crashes(v_n)
        self.state.update({'y': y_n, 'v': v_n})

    def sense(self):
        y, v = self.state.list()
        y = self.sensor_noise(y, v)
        return self.outpt.update(y)

    def observe_state(self):
        return self.state

    def sensor_noise(self, y, v):
        if v != 0.0:
            add_gauss = np.random.normal(0, 0.5 * np.abs(v))
        else:
            add_gauss = 0.0
        return y + self._sn * add_gauss

    # this can be here too
    def potential_field(self, y):
        pot = self._pf * int(self.amp*np.sin(2*np.pi*y/self.y_max))
        return pot

    def speed_wobble(self, v):
        if v != 0.0:
            add_gauss = np.random.normal(0, 0.1 * np.abs(v))
        else:
            add_gauss = 0.0
        return v + self._sp * add_gauss

    def crashes(self, v):
        rand = np.random.rand()
        if rand <= (self.v_max - np.abs(v)) * (self.prob_crash/self.v_max):
            v = 0.0
        return v



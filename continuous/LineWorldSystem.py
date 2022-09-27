from continuous import ContinuousStateSystem
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

class LineWorldSystem(ContinuousStateSystem):
    def __init__(self,  prob_crash=0.1, mass=1, v_max=10, y_max=50, amp=1, potential_field=True, sensor_noise=True, speed_wobble=True):
        super().__init__()
        self.mass = mass
        self.prob_crash = prob_crash
        self.v_max = v_max
        self.y_max = y_max
        self.amp = amp

        self._pf = potential_field
        self._sn = sensor_noise
        self._sp = speed_wobble

        # action f in float
        self.inpt.add_def(dict(f=float)).set_rule(rocket_keyboard)
        # state (x, y)
        self.state.add_def(dict(y=float, v=float))
        # outputs
        self.outpt.add_def(dict(y=float))

    def drive(self, inpt, t):
        """
        Function to drive a robot with an input
        :param inpt: self.inpt definition
        :param t: time
        :return: None
        """
        y, v, *__ = list(self.state.values())
        f = self.inpt.get('f')
        y_n = y
        v_n = v
        self.state.update({'y': y_n, 'v': v_n})

    def sense(self):
        """
        function for robot sensing
        :return: self.outpt
        """
        y, v, *__ = list(self.state.values())
        y = self.sensor_noise(y, v)
        return self.outpt.update(y)

    def observe_state(self):
        """
        State direct observation.
        :return: self.state
        """
        return self.state

    def sensor_noise(self, y, v):
        """
        a function to add sensor noise to y
        self._sn: bool for turning on and off noise
        :param y: y state
        :param v: v state
        :return: y
        """
        if self._sn:
            # add sensor noise
            pass
        return y

    # this can be here too
    def potential_field(self, y):
        """
        a function to add sensor noise to y
        self._pn: bool for turning on and off potential energy
        :param y: y state
        :return: force
        """
        if self._pf:
            # add potential energy
            pass
        return 0

    def speed_wobble(self, v):
        """
        For speed wobble
        :param v: v state
        :return: wobbled v
        """
        if self._sp:
            # add speed wobble
            pass
        return v

    def crashes(self, v):
        """
        Crash handling
        :param v: state v
        :return:
        """
        self.prob_crash # probability of crash
        return v



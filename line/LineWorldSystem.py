from rems.robots import RobotBase
import numpy as np


class LineWorldSystem(RobotBase):
    def __init__(self, potential_field=True, sensor_noise=True, speed_wobble=True, crash=True):
        super().__init__()
        self._pf = potential_field
        self._sn = sensor_noise
        self._sp = speed_wobble
        self._cr = crash

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
        add_gauss = np.random.normal(0, 0.5 * v)
        return y + self._sn * add_gauss

    def potential_field(self, y):
        return self._pf * 2*np.cos(y)

    def speed_wobble(self, v):
        add_gauss = np.random.normal(0, 0.1 * v)
        return v + self._sp * add_gauss

    def crashes(self, v):
        rand = np.random.rand()
        if self._cr and rand <= (self.v_max - np.abs(v)) * (self.prob_crash/self.v_max):
            v = 0.0
        return v



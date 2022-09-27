from discrete.DiscreteStateSystem import DiscreteStateSystem
from rems.typing import MapRule
import numpy as np

def keyboard_map(o):
    for k, v in o.items():  # k is key name, v is bool
        if v:
            if k == 'space':
                return 'stay'
            elif k == 'up':
                return 'up'
            elif k == 'down':
                return 'dwon'
            elif k == 'right':
                return 'right'
            elif k == 'left':
                return 'left'
            return k
    return 'stay'

key_rule = MapRule(['up', 'down', 'right', 'left', 'space'],
                        keyboard_map,
                        ['a'],)


class GridWorldSystem(DiscreteStateSystem):
    # input rule
    def __init__(self, grid, prob_error=0):
        super().__init__()
        self.grid = grid
        self.prob_error = prob_error



        self.inpt.add_def(dict(a=str)).set_rule([key_rule])  # this is adding keyboard mapping
        # state (x, y)
        self.state.add_def(dict(s=str))
        # observation space (o)
        self.outpt.add_def(dict(o=float))

    def transition_probability(self, s, a, s_n):
        super().transition_probability(s, a, s_n)

    def observation_probability(self, s, a, o):
        super().observation_probability(s, a, o)

    def drive(self, inpt, t):
        """
        Function to drive a robot with an input
        :param inpt: self.inpt definition
        :param t: time
        :return: None
        """
        # drive to a next state (update the state)
        next_state = self.state
        self.state.update(next_state)

    def sense(self):
        """
        function for robot sensing
        :return: self.outpt
        """
        goals = self.grid.get_goals()
        state_x, state_y = self.grid.get_location(self.state['s'])
        for k in goals:
            goal_x, goal_y = self.grid.get_location(k)
        return self.outpt.update({'o': 0.0})

    def observe_state(self):
        """
        State direct observation.
        :return: self.state
        """
        return self.state





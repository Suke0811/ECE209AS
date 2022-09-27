from discrete.DiscreteStateSystem import DiscreteStateSystem
from rems.typing import MapRule
import numpy as np


stay_rule = MapRule(['up', 'down', 'right', 'left'],
                        lambda u, d, r, l: not bool(u + d + r + l),
                        ['stay'],
                        to_list=True)


class GridWorldSystem(DiscreteStateSystem):
    # input rule
    def __init__(self, grid, prob_error=0):
        super().__init__()
        self.grid = grid
        self.prob_error = prob_error

        self.A = {'up', 'down', 'left', 'right', 'stay'}
        self.S = set(self.grid.grid_keys.values())

        # action space (up, down, right, left, stay)
        self.inpt.add_def(dict(up=bool, down=bool, right=bool, left=bool, stay=bool)).set_rule([stay_rule])
        # state space (x, y)
        self.state.add_def(dict(x=float, y=float))
        # observation space (o)
        self.outpt.add_def(dict(o=float))

    def drive(self, inpt, t):
        self.inpt.update(inpt)
        self.state.update(self.transition(self.state, inpt))

    def sense(self):
        goals = self.grid.get_goals()
        state_x, state_y = list(self.state.values())
        h_num = []
        for k in goals.keys():
            goal_x, goal_y = self.grid.get_index(k)
            num = (np.linalg.norm(np.array([goal_x, goal_y]) - np.array([state_x, state_y])))
            if num == 0.0:
                return self.outpt.update(0.0)
            h_num.append(1/num)
        h = 2 / np.sum(h_num)

        if np.random.rand() < (np.ceil(h) - h):
            return self.outpt.update(np.floor(h))
        else:
            return self.outpt.update(np.ceil(h))

    def observe_state(self):
        return self.state

    def transition_probability(self, s, action, s_n):
        p=0
        if action['up']:
            inc = self.action_to_inc('up')
        elif action['down']:
            inc = self.action_to_inc('down')
        elif action['right']:
            inc = self.action_to_inc('right')
        elif action['left']:
            inc = self.action_to_inc('left')
        else:
            inc = self.action_to_inc('stay')

        s_vec = np.array(self.grid.key2xy(s))
        s_n_vec = np.array(self.grid.key2xy(s_n))

        if s_vec + inc == s_n_vec:
            p = 1 - self.prob_error
        else:
            p = self.prob_error / 4

        if not all([v_min <= v and v < v_max for v_min, v, v_max in zip([0, 0], s_n, [self.grid.x, self.grid.y])]) or self.grid.if_obstacle(s_n):
            p = 0

        return p

    @staticmethod
    def action_to_inc(action):
        inc = [0, 0]
        if action == 'up':
            inc = [0, 1]
        elif action == 'down':
            inc = [0, -1]
        elif action == 'right':
            inc = [1, 0]
        elif action == 'left':
            inc = [-1, 0]
        elif action == 'stay':
            inc = [0, 0]
        return np.array(inc)


    def transition(self, state, action):
        next_state = state.ndarray()
        state = state.ndarray()
        inc = [0, 0]
        rand = np.random.rand()
        if rand <= (1 - self.prob_error):
            # successful action
            if action['up']:
                inc = self.action_to_inc('up')
            elif action['down']:
                inc = self.action_to_inc('down')
            elif action['right']:
                inc = self.action_to_inc('right')
            elif action['left']:
                inc = self.action_to_inc('left')
            elif action['stay']:
                inc = self.action_to_inc('stay')
        else:
            pro = rand - (1 - self.prob_error)
            keys = dict(action)
            key_list = list(keys.keys())
            for key, val in action.items():
                if val:
                    keys.pop(key)
                    key_list = list(keys.keys())
                    break

            if pro < self.prob_error/4:
                inc = self.action_to_inc(key_list[0])
            elif pro < 2 * self.prob_error/4:
                inc = self.action_to_inc(key_list[1])
            elif pro < 3 * self.prob_error/4:
                inc = self.action_to_inc(key_list[2])
            elif pro < 4 * self.prob_error/4:
                inc = self.action_to_inc(key_list[3])

        if all([v_min <= v and v < v_max for v_min, v, v_max in zip([0, 0], state + inc, [self.grid.x, self.grid.y])]):
            if not self.grid.if_obstacle(tuple(state+inc)):
                next_state = state + inc

        return next_state










from rems.robots import RobotBase
import numpy as np


class GridWorldSystem(RobotBase):
    def drive(self, inpt, t):
        self.inpt.update(inpt)
        state = self.state
        self.state.update(self.transition(state, inpt))

    def sense(self):
        goals = self.grid.get_goals()
        state_x, state_y = self.state.list()
        h_num = []
        for k in goals.keys():
            goal_x, goal_y = self.grid.get_index(k)
            h_num.append(1/(np.linalg.norm(np.array([goal_x, goal_y]) - np.array([state_x, state_y]))))
        h = 2 / np.sum(h_num)

        if np.random.rand() < (np.ceil(h) - h):
            return self.outpt.update(np.floor(h))
        else:
            return self.outpt.update(np.ceil(h))

    def observe_state(self):
        return self.state

    def transition(self, state, action):
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
            return inc

        next_state = state
        inc = [0, 0]
        rand = np.random.rand()
        if rand <= (1 - self.prob_error):
            # successful action
            if action['up']:
                inc = action_to_inc('up')
            elif action['down']:
                inc = action_to_inc('down')
            elif action['right']:
                inc = action_to_inc('right')
            elif action['left']:
                inc = action_to_inc('left')
            elif action['stay']:
                inc = action_to_inc('stay')
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
                inc = action_to_inc(key_list[0])
            elif pro < 2 * self.prob_error/4:
                inc = action_to_inc(key_list[1])
            elif pro < 3 * self.prob_error/4:
                inc = action_to_inc(key_list[2])
            elif pro < 4 * self.prob_error/4:
                inc = action_to_inc(key_list[3])

        if all([v_min <= v and v < v_max for v_min, v, v_max in zip([0, 0], state + inc, [self.grid.x, self.grid.y])]):
            if not self.grid.if_obstacle(*(state+inc).list()):
                next_state = state + inc

        return next_state










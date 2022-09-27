from rems.robots import RobotBase

class ContinuousStateSystem(RobotBase):
    def __init__(self):
        super().__init__()
        self.inpt.add_def(dict())
        # state (x, y)
        self.state.add_def(dict())
        # outputs
        self.outpt.add_def(dict())

    def transition_probability(self, s, a, s_n):
        raise NotImplementedError

    def observation_probability(self, s, a, o):
        raise NotImplementedError



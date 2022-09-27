from continuous import ContinuousStateSystem


class DiscreteStateSystem(RobotBase):
    def __init__(self):
        super().__init__()
        self.S = set()
        self.A = set()
        self.O = set()



from rems.robots import RobotBase

class ContinuousStateSystem(RobotBase):
    def __init__(self):
        super().__init__()
        self.inpt.add_def(dict())
        # state (x, y)
        self.state.add_def(dict())
        # outputs
        self.outpt.add_def(dict())


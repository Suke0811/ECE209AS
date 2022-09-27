from rems.robots import RobotBase
from rems.typing import DefDict


class DiscreteRobotSystem(RobotBase):
    def __init__(self):
        super().__init__()

    def transition_probability(self, s, action, s_n):
        """
        Transition probability function
        :param s: string of state index ('01' -> x=0, y=1)
        :param action: action string ('up', ''down)
        :param s_n: string of state index ('01' -> x=0, y=1)
        :return: transition probability [0, 1]
        """
        p = 0
        return p

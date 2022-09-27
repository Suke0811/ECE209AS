from rems.process import ProcessSystem


class MdpSystem(ProcessSystem):
    def __init__(self, robot, inpt_feed, S, A, Pfunc, Rfunc, gamma):
        self.robot = robot
        self.inpt_feed = inpt_feed
        self.A = A
        self.S = S
        self.P = Pfunc
        self.R = Rfunc
        self.gamma = gamma
        self.V = S
        self.Q = Q
        self.PI = S


    def value_iteration(self):
        pass

    def policy_iteration(self):
        pass

    def calc_Q(self):
        for s in self.S:
            for a in self.A:
                v = 0.0
                for s_n in self.S:
                    p = self.P(s, a, s_n)
                    v += p * (self.R(s, a, s_n) + self.gamma*self.V[s_n])



    def process(self, t):
        pass




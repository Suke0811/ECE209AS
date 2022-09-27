from continuous import ContinuousStateSystem


class DiscreteStateSystem(ContinuousStateSystem):
    def __init__(self):
        super().__init__()
        # create your own S, A, O
        self.States = {"alice", "bob", "charlie", "eve"} # some random state sets
        self.Actions = {"roommate", "boss"} # some random action sets
        self.Observations = {"blue", "gold"} # some random observation sets

        self.state.add_def({'s': str}) # definition of your state, i.e. {s: 'alice'}
        self.inpt.add_def({'a': str}) # definition of your action, i.e. {a: 'roommate'}
        self.outpt.add_def({'o': str})

    def transition_probability(self, s, a, s_n):
        # Override this method
        assert s in self.States
        assert a in self.Actions
        assert s_n in self.States
        return 1 if s == s_n else 0

    def observation_probability(self, s, a, o):
        # Override this method
        assert s in self.States
        assert a in self.Actions
        assert o in self.Observations
        return 1 if o == list(self.Observations)[0] else 0

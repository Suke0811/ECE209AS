from rems.inputs import InputBase


class MdpInput(InputBase):
    def __init__(self, robot_id=None):
        super().__init__()
        self.robot_id = robot_id

    def get_inputs(self, timestamp=None, prefix='inpt', *args, **kwargs):
        """prefix specify what data to get, if noe"""
        if prefix in self.inpt.prefixes:
            ret_inpt = self.inpt.__dict__[prefix]()
        else:
            ret_inpt = self.inpt
        return ret_inpt

    def set_next_input(self, inpt):
        self.inpt = inpt

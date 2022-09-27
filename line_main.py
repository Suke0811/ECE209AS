from rems import Operator
from rems.Config import SimConfig
from rems.inputs import KeyboardInput
from rems.outputs import FileOutput
from rems.utils import time_str
from line import LineAnimation, LineWorldSystem

o = Operator(debug_mode=True)
i = KeyboardInput(dict(v=0, y=0), enable_keys=['up', 'down'])
o.set_input(i)

o.add_robot(robot=LineWorldSystem,
            robot_args=dict(prob_crash=0.1, mass=1, v_max=10, potential_field=True, sensor_noise=True, speed_wobble=True),
            outputs=(LineAnimation(), FileOutput(filepath='out/line' + time_str() + '.csv')))

o.run(SimConfig(max_duration=20, dt=1, realtime=True, start_time=0, run_speed=1))

from rems import Operator
from rems.Config import SimConfig
from grid import GridWorldSystem, Grid2DMap
from grid import GridWorldDef
from rems.inputs import KeyboardInput
from rems.outputs import GridAnimation, FileOutput
from rems.utils import time_str
from line import LineAnimation, LineWorldSystem, LineWorldDef


o = Operator(debug_mode=True)
i = KeyboardInput(dict(v=0, y=0), enable_keys=['up', 'down'])
o.set_input(i)

o.add_robot(robot_def=LineWorldDef, robot=LineWorldSystem,
            def_args=dict(prob_crash=0.1, mass=1, v_max=10),
            robot_args=dict(potential_field=True, sensor_noise=True, speed_wobble=True, crash=True),
            outputs=(LineAnimation(), FileOutput(filepath='out/line' + time_str() + '.csv')))

o.run(SimConfig(max_duration=20, dt=1, realtime=True, start_time=0, run_speed=1))

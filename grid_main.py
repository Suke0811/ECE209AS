from rems import Operator
from rems.Config import SimConfig
from grid import GridWorldSystem, Grid2DMap, GridAnimation
from rems.inputs import KeyboardInput
from rems.outputs import FileOutput
from rems.utils import time_str


# Init middleware (REMS) operator
# debug_mode = True disable multi-processing for easier debugging
o = Operator(debug_mode=True)

# using keyboard input
# init_state=initial state, enable_keys = keys to use (None will use all)
i = KeyboardInput(init_state=dict(x=0, y=0), enable_keys=['up', 'down', 'right', 'left'])

# set REMS system wide input (all robots added to operator will receive the same input)
o.set_input(i)


# create a grid map
g = Grid2DMap(5, 5)
OBSTACLE = 'X'
# set obstacle
g.set_obstacles({'11': -1, '21': -1, '13': -1, '23': -1})
# set goal
g.set_goals({'20': 1, '22': 1})



# add_robot
# o.add_robot(robot, robot_args,
#               outputs=OutputSystem)
o.add_robot(robot=GridWorldSystem,
            robot_args=dict(grid=g, prob_error=0.1),
            outputs=(GridAnimation(g), FileOutput(filepath='out/grid' + time_str() + '.csv')))
# if no InputSystem is assigned, REMS system wide input is used


o.run(SimConfig(max_duration=10, dt=1, realtime=True, start_time=0, run_speed=1))

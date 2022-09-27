from rems import Operator
from rems.Config import SimConfig
from grid import GridWorldSystem, Grid2DMap, GridAnimation
from grid import GridWorldDef
from rems.inputs import KeyboardInput
from rems.outputs import FileOutput
from rems.utils import time_str
from line import LineAnimation, LineWorldSystem, LineWorldDef


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
g.set_obstacles({'11': OBSTACLE, '21': OBSTACLE, '13': OBSTACLE, '23': OBSTACLE})
# set goal
g.set_goals({'20': 'Rs', '22': 'Rd'})



# add_robot
# o.add_robot(robot_definition, robot_implementation,
#               robot_definition_args, robot_implementation_args,
#               outputs=OutputSystem,
#               inpt=InputSystem)
o.add_robot(GridWorldDef, GridWorldSystem,
            def_args=dict(grid=g, prob_error=0.1),
            outputs=(GridAnimation(g), FileOutput(filepath='out/grid' + time_str() + '.csv')))
# if no InputSystem is assigned, REMS system wide input is used



o.run(SimConfig(max_duration=10, dt=1, realtime=True, start_time=0, run_speed=1))

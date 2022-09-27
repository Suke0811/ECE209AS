from rems import Operator
from rems.Config import SimConfig
from discrete import GridWorldSystem, Grid2DMap, GridAnimation
from rems.inputs import KeyboardInput
from rems.outputs import FileOutput
from rems.utils import time_str


# Init middleware (REMS) operator
# debug_mode = True disable multi-processing for easier debugging
o = Operator(debug_mode=True)

# using keyboard input
# init_state=initial state, enable_keys = keys to use (None will use all)
i = KeyboardInput(init_state=dict(x=0, y=0), enable_keys=['up', 'down', 'right', 'left', 'space'])

# set REMS system wide input (all robots added to operator will receive the same input)
o.set_input(i)


# create a grid map state names: "alice", "bob", "charlie", "eve"
# note that order matters:
grid_location = dict(
        charlie=(0, 1), eve=(1, 1),
        alice=(0, 0), bob=(1, 0),
    )
grid_shape = (2,2)
g = Grid2DMap(grid_location, grid_shape)

# set obstacles for plot
g.set_obstacles(['bob',])
# set goals for plot
g.set_goals(['eve',])


# add_robot
# o.add_robot(robot, robot_args,
#               outputs=OutputSystem)
o.add_robot(robot=GridWorldSystem,
            robot_args=dict(grid=g, prob_error=0.1),
            outputs=(GridAnimation(g), FileOutput(filepath='out/grid' + time_str() + '.csv')))

o.run(SimConfig(max_duration=10, dt=1, realtime=True, start_time=0, run_speed=1))

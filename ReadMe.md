This is repo with skeleton code for grid and number line problems.

___
# Setup

You should fork this repo, clone the fork, and then run:
```shell
pip install -r requirements.txt
```
This will install all dependencies for our system.


___
# Tasks

# Week 1
You need to watch Lec01 videos in [class website](https://comprobo.uclalemur.com/)
## Grid World [Link to Pdf](https://comprobo.uclalemur.com/pdf/gridworld.pdf)
Define S, A, O, transition_probability(s,a,s_n), observation_probability(s, a, o)

Implement drive, sense functions

## Number Line [Link to Pdf](https://comprobo.uclalemur.com/pdf/numberline.pdf)
Implement drive, sense functions.
Add sensor noises, potential_field, speed_wobble, crashes.



## Files
```
root
│   README.md
│   grid_main.py                    (An example run code for gird world)   
│   line_main.py                    (An example run code for number line)   
│
└───continuous
│   │   ContinuousStateSystem.py    (base class)
│   │  
│
└───discrete
    │   DiscreteStateSystem,py      (base class)
    │
```  

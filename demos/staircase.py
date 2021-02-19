from psydapt import Scale
from psydapt.staircase import Staircase

stair = Staircase(
    start_val=0.5,
    n_reversals=3,
    step_sizes=[0.1, 0.01],
    n_trials=20,
    n_up=2,
    n_down=2,
    apply_initial_rule=True,
    stim_scale=Scale.Linear,
    min_val=0
)

not_done = True
while not_done:
    next_stim = stair.next()
    print(f'Stimulus val is {next_stim:.4f}.')
    val = input('Correct (1/0)?')
    not_done = stair.update(int(val))

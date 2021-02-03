```python
import psydapt
import psydapt.staircase as staircase

P = staircase.Params

x = staircase.Staircase(P(
    start_val=0.5,
    n_reversals=3,
    step_sizes=[0.01, 0.001],
    n_trials=20,
    n_up=4,
    n_down=3,
    apply_initial_rule=True,
    stim_scale=psydapt.Scale.Linear,
    min_val=0
))

```

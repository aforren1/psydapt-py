from psydapt import Scale
import psydapt.questplus as qp
from psydapt.questplus import Weibull

intensities = [-3.5, -3.25, -3, -2.75, -2.5,
               -2.25, -2, -1.75, -1.5, -1.25,
               -1, -0.75, -0.5]
wei = Weibull(Weibull.Params(
    stim_scale=Scale.Log10,
    intensity=intensities,
    threshold=intensities,
    slope=[0.5, 4.125, 7.75, 11.375, 15],
    lower_asymptote=[0.01, 0.1325, 0.255, 0.3775, 0.5],
    lapse_rate=[0.01],
    stim_selection_method=qp.StimSelectionMethod.MinEntropy, # only MinEntropy for now
    param_estimation_method=qp.ParamEstimationMethod.Mean, # currently unused
    n=5, # currently unused
    max_consecutive_reps=2, # currently unused
    random_seed=1 # currently unused
))


trial_count = 20
for i in range(trial_count):
    next_stim = wei.next()
    print(f'Stimulus val is {next_stim}.')
    val = input('Correct (1/0)?')
    wei.update(int(val))

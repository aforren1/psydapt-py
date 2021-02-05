import questplus as qp
from psydapt import Scale
from psydapt.questplus import NormCDF
import numpy as np

stim_domain = {'intensity': np.arange(1 / 60, 0.5, step=1 / 60)}

# parameter domain
loc2 = np.linspace(0.05, 0.45, 25)
scale2 = np.linspace(0.0001, 0.2, 20)
lb2 = np.linspace(0, 0.2, 5)
ub2 = np.linspace(0, 0.2, 5)

param_domain = {'mean': loc2, 'sd':scale2, 'lower_asymptote': lb2, 'lapse_rate': ub2}

resp_domain = {'response': ['correct', 'incorrect']}

norm1 = qp.QuestPlus(stim_domain=stim_domain, func='norm_cdf', stim_scale='linear',
                     param_domain=param_domain, outcome_domain=resp_domain)

norm2 = NormCDF(NormCDF.Params(
    stim_scale=Scale.Linear,
    intensity=stim_domain['intensity'],
    location=param_domain['mean'],
    scale=param_domain['sd'],
    lower_asymptote=param_domain['lower_asymptote'],
    lapse_rate=param_domain['lapse_rate']
))

stims = []

for i in range(20):
    n1 = norm1.next_stim
    n2 = norm2.next()

    print(f'Stimuli are {n1["intensity"]} and {n2}')

    val = input('Correct (0/1)?')
    if val == '1':
        o1 = dict(response = 'correct')
        o2 = 1
    else:
        o1 = dict(response = 'incorrect')
        o2 = 0
    norm1.update(stim=n1, outcome=o1)
    norm2.update(o2)
    stims.append(n1['intensity'])

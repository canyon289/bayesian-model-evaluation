"""
Generates datasets for 4.1 plant activity
"""

import pymc3 as pm
import numpy as np
import arviz as az
from scipy import stats

np.random.seed(0)

DATASETS = [{"β":3, "noise_scale":4, "name":"GreenPower.nc"},
            {"β":2, "noise_scale":.1, "name":"RootsGalore.nc"},
            {"β":-1, "noise_scale":1, "name":"BudgetFertilizer.nc"}]

def data_generator(β, noise_scale, points = 50, **kwargs):
    """Generates data sets for use in section 4"""
    
    x = np.random.randint(0,10, points)

    # Constant Noise from noisy sensors
    ϵ = stats.norm(scale=noise_scale).rvs(size=points)
    y = 10 + β*x + ϵ
    return x, y


def inference_generator(x, y, draws=500, tune=500):
    """Assumes linear model in form of data_generator"""
    with pm.Model() as model:
        # These Alpha and Beta are estimators for the givens above
        beta = pm.Normal("beta", 1)

        # Standard deviation can only be positive
        epsilon = pm.HalfCauchy("epsilon", 1)

        y_est = pm.Normal("y_est", mu=10+beta*x, sd=epsilon, observed=y)

        trace = pm.sample(draws=draws, tune=tune)
        return trace

def netcdf_generator():
    """Generates netcdf for use in tutorial"""
    for dataset in DATASETS:
        name = dataset.pop("name")

        x,y = data_generator(**dataset)
        trace = inference_generator(x,y, draws=2000, tune=2000)

        data = az.from_pymc3(trace)
        
        # Delete sample stats to reduce disk size 
        del data.sample_stats
        data._groups.remove("sample_stats")

        data.to_netcdf(name)
    return

if __name__ == "__main__":
    netcdf_generator()


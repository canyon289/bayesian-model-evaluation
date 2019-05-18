"""
Generates datasets for 5.2 plant activity
"""
import pymc3 as pm
import numpy as np
import arviz as az
import pandas as pd
from scipy import stats

np.random.seed(0)

def data_generator(β=10, noise_scale=1, points = 50, **kwargs):
    """Generates data set for use in section 5.1"""
    # TODO Change this to function load
    points = 50
    x = np.random.randint(1,30, points)
    ϵ = stats.norm(scale=1).rvs(size=points)
    y= 10*np.log(x+1)  + ϵ

    return x, y


def linear_model(x, y, draws=500, tune=500):
    """Assumes linear model in form of data_generator"""

    with pm.Model() as linear_model:
        β = pm.Normal("β", mu=0, sd=1)
        α = pm.Normal("α", mu=0, sd=1)
        
        # Standard deviation can only be positive 
        ϵ = pm.HalfCauchy("epsilon", 1)
        
        y_est = pm.Normal("y_est", mu=α + β*x, sd=ϵ, observed=y)
        trace = pm.sample(draws=5000, tune=2000)
        
    return "linear_plant_growth.nc", trace


def log_model(x, y, draws=500, tune=500):
    """Assumes linear model in form of data_generator"""
    # Logarithmic model
    with pm.Model() as log_model:
        β = pm.Normal("β", mu=0, sd=1)
        α = pm.Normal("α", mu=0, sd=1)
        
        # Standard deviation can only be positive 
        ϵ = pm.HalfCauchy("epsilon", 1)
        
        y_est = pm.Normal("y_est", mu= β*np.log(x+α), sd=ϵ, observed=y)
        trace = pm.sample(draws=5000, tune=2000)

    return "log_plant_growth.nc", trace 


def netcdf_generator():
    """Generates netcdf for use in 5.2 tutorial"""

    x,y = data_generator()

    pd.DataFrame({"days":x, "plant_height":y}).to_csv("PlantGrowthData.csv")
       
    for func in (linear_model, log_model):
        name, trace = func(x,y, draws=2000, tune=2000)
        data = az.from_pymc3(trace=trace)

        # Delete sample stats to reduce disk size 
        del data.sample_stats
        data._groups.remove("sample_stats")

        data.to_netcdf(name)
    return

if __name__ == "__main__":
    netcdf_generator()

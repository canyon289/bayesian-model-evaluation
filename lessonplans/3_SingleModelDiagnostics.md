# Section 3: Single Model Diagnostics (~1 hour)
Demonstrate model evaluation and criticism techniques for one model.
Show how to plot diagnostics. Demonstrate the difference between “good” and “bad”
versions of plots so students are able to use and diagnose their own models
Demonstrate how models can be diagnosed
Lightly introduce theory for MCMC and HMC to give context

## Activities
### Instructor Do: Talk through HMC theory (15 minutes)
Lightly explain the theory behind Markov Chain Monte Carlo, with special
emphasis on how MCMC has theoretical guarantees, but those guarantees are asymptotic, and may take literally infinite time to be true.

Due to this there are numerous visual diagnostics for MCMC plots such as
* Autocorrelation
* Traceplot

MCMC is not just one method though, but a set of related methods. For 
Hamiltonian Monte Carlo there are additional diagnoses
* Energy Plot
* Divergences in plot parallel, pair plot, and trace plot

### Students Do: Practice using plots to diagnose models (15 minutes)
Have students fit and evaluate the eight schools models. Using diagnostics
have them explain which model parameterization seems to be getting 
explored more effectively

### Instructor Do: Introduce numerical diagnoses (5 minutes)
Explain intuition and formulas for calculating numerical diagnoses. Mention
how these calculations are still being refined and show references from Gelman
and Aki Vehtari demonstrating this fact
* Effective_sample_size/Rhat 
* Geweke

### Students Do: Practice interpreting numerical diagnoses (10 minutes)
Have students evaluate the model fits from the prior activities with numerical
diagnostics. Ask them to discuss with others to see if the diagnostics seem
to be consistent.

### Instructor Do: Review examples (10 minutes)
Showcase "solved" notebooks of eight schools model parameterization, stopping
to explain how in this case the data is the same but how the parameterization
effects the MCMC algorithms ability to explore the posterior space


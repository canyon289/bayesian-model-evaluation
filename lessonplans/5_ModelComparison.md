# Section 5: Multiple Model Comparison (~30 minutes)
Demonstrate how multiple models can be compared to determine which model is
best suited for analysis and data. Introduce techniques such as
Information Criteria and Leave One Out Validation

## Activities
### Instructor Do. Introduce Model Comparison functions (15 minutes)
* WAIC
* LOO
* Plot_compare

Remind students that there aren't only infinite possibilities for model
fits and parameters, there's also infinite possibilities for model
parametrizations! Just like we can diagnose inference runs, there are tools
to diagnose models themselves. Talk through numerical summarizations 
information criteria and leave one out validation, but there are also
helpful plots like plot_compare. Explain how even in the same parameterization
the choice of prior can affect model fit.


### Students Do: Practice Model Comparison (10 Minutes)
* WAIC
* Plot_compare

Have students fit a linear model, a sinusoidal model, and a polynomial model
to some data. Ask them to judge which fit seems to work best


### Instructor Do: Review Model Comparison (5 Minutes)


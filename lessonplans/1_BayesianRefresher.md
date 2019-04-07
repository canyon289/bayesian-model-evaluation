# Section 1: Bayesian refresher and Introduction to ArviZ

* Walk students through a Bayesian Analysis and showcase all portions of the Bayesian workflow.  
* Have students work together with instructor to gain confidence in seeing a full analysis.
* Showcase mini tutorial on how to setup a bayesian model in PyMC3 and PyStan.
* Explain how model fitting is easy with well written Probabilistic Programming
* Languages, but just because the software fits a model, it doesn’t mean the model is a good one
* Demonstrate how arrays of data are not well suited for communication or understanding

## Activities
### Instructor Do: Introduction to Tutorial (15 minutes)
* End to End model workflow
* Briefly run through 8 schools model non-centered
* Show how model fit may look good but there seem to be lots of divergences.
* Then show centered parametrization and how the plots change.
* Explain why eight schools is so important
* Showcase link to Michael Betancourt's analysis, 8 schools explainer in ArviZ Docs,
and [Everything I need to know about Bayesian Statistics](https://statmodeling.stat.columbia.edu/2014/01/21/everything-need-know-bayesian-statistics-learned-eight-schools/)


### Student Do: Fit your own model (15 minutes)
Ask students to fit their own models. Provide a list of suggestions from easy to complex. 
Students should start from a framework
where the model is either defined in code, or defined in statistics so
they are able to execute the models without needing to define parameterization
or code themselves.

* Standard Coin Flipping
* Coin Flipping where coin is picked from random from set of 3 coins
* Bayesian Linear Regression (Take something from Osvaldo's book)
* [Exoplanet model](https://github.com/dfm/exoplanet)
* Radon model
* Bring your own model

Ask students to try out some ArviZ plots. No need for complete understanding,
moreso allow them time to get familiar with the docs and generally what ArviZ is.
Be sure to fix any technical issues during this time to make sure every student
can run ArviZ and one modeling language


### All Do: Discussion about various modelling libraries, Bayesian Workflow (15 minutes)
Talk through a complete end to end bayesian workflow and how it differs
from the other statistical workflow of frequentism

* "Bayesianism vs frequentism" as "uncertain parameters vs uncertain data"
* MCMC as a way of computing expectations
* In the context of MCMC, a "distribution" is a collection of samples, possibly with more structure

The points above necessitate the use of a Bayesian Workflow
![BayesianWorkflow](img/BayesianWorkflow.jpg)

Explain that unfortunately multiple tools are required to go through all the steps
and the four primary concerns are

1. Calculating the various distributions (prior, posterior, predictive) with technique of choice
2. Storing the results somehow
3. Visualizing various diagnostics and model results
4. Determining the language that will be used for defining the model/definition

Explain how ArviZ is meant to unify points 2 and 3. ArviZ strives to let people
model in their language of choice yet provide a common method for data
exchange  and model visualization. Explain that there are 
integrations outside of python, for example 
* cmdstan 
* [rainier](https://github.com/stripe/rainier) in scala
* [Turing](https://github.com/TuringLang/Turing.jl) in julia
* [Anglican](https://probprog.github.io/anglican/index.html) in clojure
* [Infer.net](https://dotnet.github.io/infer/)
* [Webppl](http://webppl.org/) in javascript
* [Greta](https://greta-stats.org/) in r

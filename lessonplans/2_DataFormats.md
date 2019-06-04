# Section 2: Xarray, Inference Data, NetCDF (45 minutes)
Showcase the power of Xarray and az.InferenceData in handling large models
with many variables. Leave students with understanding of how common data
formats will help them create reproducible experiments and share results with others

* Introduce MCMC basics
* Introduce xarray, InferenceData and NetCDF
* Show basic functionality like indexing and filtering
* Explain relation to InferenceData and NetCDF
* Leave students with understanding of why this dataformat was chosen

## Activities

### Instructor Do: MCMC basics (25 minutes)
* Explain basic MCMC theory 
* Discuss chains, samples, and draws in theory and how they relate to data structures
* Demononstrate how Single Variable Single Chain and how that fits into numpy array
* Demonstrate Single Variable Multiple chain and how that fits into pandas dataframe
* Explain that typical MCMC is done with multiple variables and multiple chains which is why xarray is useful
* Demonstrate how to work with xarray
    * Selecting xarray data with dimensions
    * Selecting xarray data with coordinates
    * Loading inferencedata from ArviZ
* Show how InferenceData is used to maintain references to multiple xarray objects
* Demonstrate how InferenceData can be generated from model fit
* Explain how NetCDF can be used to persist ArviZ Inference data objects to disk.

Emphasize that xarray has a wide array of functionality and is useful in many
contexts. In ArviZ however we only use a subset of the functionality although
we do encourage students to read the xarray docs.

For these examples use chains, draw, and vars, instead of arbitrary names
so you  can interleave in conversations about MCMC and get students used
to what xarrays look like in ArviZ

### Students Do: Xarray practice activities (15 minutes)
Have students
* Load inferencedata from ArviZ
* Selecting xarray data with dimensions
* Selecting xarray data with coordinates
* Getting Xarray dataset from inferencedata
* Generating InferenceData from model fit
* Saving inferencedata locally on disk
* Write down all the various data sets that can come from an MCMC Bayesian Analysis

Before starting activity mention how this activity is the most "copy
and paste" as we're demoing and api, not a mathematical concept. The next
activities will include more creativity.

### Instructor Review: Xarray practice activities (5 Minutes)

# Section 2: Xarray, Inference Data, NetCDF (40 minutes)
Showcase the power of Xarray and az.InferenceData in handling large models
with many variables. Leave students with understanding of how common data
formats will help them create reproducible experiments and share results with others

* Introduce xarray, InferenceData and NetCDF
* Show basic functionality like indexing and filtering
* Explain relation to InferenceData and NetCDF
* Leave students with understanding of why this dataformat was chosen

## Activities
### Instructor Do: Xarray, InferenceData, and NetCDF introduction (5 minutes)
* Start with pandas and explain how xarray allows for more dimensions than just 2
* From Xarray explain how xarray doesn't allow for groups, hence the az.InferenceData wrapper
* Lastly talk about how python objects are stored in memory, and that netcdf to InferenceData
is like sql to pandas

### Instructor Do: Demo functionality Xarray, InferenceData, and NetCDF (15 minutes
Show students how to
* Manually instantiate xarray dataarray and dataset
* Selecting xarray data with dimensions
* Selecting xarray data with coordinates
* Getting Xarray dataset from inferencedata
* Loading inferencedata from ArviZ
* Generating InferenceData from model fit

Emphasize that xarray has a wide array of functionality and is useful in many
contexts. In ArviZ however we only use a subset of the functionality although
we do encourage students to read the xarray docs.

For these examples use chains, draw, and vars, instead of arbitrary names so you  can interleave in conversations about MCMC and get students used to what xarray's look like in ArviZ

### Students Do: Xarray practice activities (10 minutes)
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

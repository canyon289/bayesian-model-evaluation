[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/arviz-devs/bayesian-model-evaluation/master)

# Bayesian Model Evaluation and Criticism

Good statisticians are able to explain their choices, justify their numbers,
evaluate their own models, and share their results (in a reproducible fashion)! 
This tutorial demonstrates how to do all the above, using ArviZ.


# Getting things setup

To get started, first identify whether you:

1. Prefer to use the `conda` package manager (which ships with the [Anaconda distribution of Python](https://www.anaconda.com/)), 
2. Prefer to use `pip`
3. Prefer to use `docker`
4. Do not want to mess around with dev-ops, or
5. Only want to view the website version of the notebooks.

## 1. Clone the repository locally

In your terminal, use `git` to clone the repository locally.

```bash
git clone git@github.com:arviz-devs/bayesian-model-evaluation.git 
```

Alternatively, you can download the zip file of the repository at the top of the main page of the repository. If you prefer not to use git or don't have experience with it, this a good option.

## 2. Download Anaconda (if you haven't already)

If you do not already have the [Anaconda distribution](https://www.anaconda.com/download/) of Python 3, go get it (note: you can also set up your project environment w/out Anaconda using `pip` to install the required packages; however Anaconda is great for data science and we encourage you to use it).

## 3. Set up your environment

### 3a. `conda` users

If this is the first time you're setting up your compute environment, use the `conda` to **create an environment**.

```bash
conda create -n bayes-eval
```

To **activate the environment**, use the `conda activate` command.

```bash
conda activate bayes-eval
```

**If you get an error activating the environment**, use the older `source activate` command.

```bash
source activate bayes-eval
```

Then follow the instructions for `pip` users.

### 3b. `pip` users

Please install all of the packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3c. `Docker` Users

An image can be built from the root directory of the repository using the command.
This will build an image on your computer with all dependencies and environment
```bash
./scripts/container.sh --build
```

Once an image is built a container can be started with the command
```bash
./scripts/container.sh --notebook
```

In your terminal a URL for the notebook server will be displayed. Copy
and paste that into a browser. With that you'll have Jupyter in a container!
If you're using docker you can skip step 4.

### 3d. Don't want to mess with dev-ops

If you don't want to mess around with dev-ops, click the following badge to get a Binder session on which you can compute and write code.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/arviz-devs/bayesian-model-evaluation/master)


### 4. Open your Jupyter notebook in Jupyter Lab!

In the terminal, navigate to this directory and execute `jupyter lab`.

Navigate to the `notebooks` then `1_BayesianWorkflow` and open notebook 
`1_Ins_BayesRefresher.ipynb`.

### 4a. Want to view static HTML notebooks

If you're interested in only viewing the static HTML versions of the notebooks 
you can [view them on github](https://github.com/arviz-devs/bayesian-model-evaluation/tree/master/notebooks)

# Acknowledgements
We would like to thank the whole Bayes community for being open with
learnings and material. For this tutorial in particular we'd like to thank
Ari Hartikainen, Osvaldo Martin, and Eric Ma for providing feedback and content.

# Feedback

Please leave feedback for us [here](https://forms.gle/cUStHUo5k9yZcrUn9)! 
We'll use this information to help improve the teaching and delivery of the material.
[Issues](https://github.com/arviz-devs/bayesian-model-evaluation/issues) and [pull requests](https://github.com/arviz-devs/bayesian-model-evaluation/pulls) are also encouraged if you would like!


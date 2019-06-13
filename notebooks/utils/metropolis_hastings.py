"""
Metropolis Hastings example with simple model

Inspired by Thomas Wiecki's blog post

https://twiecki.io/blog/2015/11/10/mcmc-sampling/
"""

import numpy as np
import scipy.stats as stats
np.random.seed(0)


N_mu_30_sd_1_data = stats.norm.rvs(loc=30, scale=1, size=1000).flatten()


def mh_sampler(data, samples=4, mu_init=.5, proposal_width=.5, mu_prior_mu=0, mu_prior_sd=1., offset=20):
    """Basic Metropolis Hasting Sampler. Optimized a little."""
    mu_current = mu_init
    posterior = []
    prior_logpdf = stats.norm(mu_prior_mu, mu_prior_sd).logpdf
    likelihood_logpdf = stats.norm(offset, 1).logpdf  # transform the inputs by subtracting the mean
    data = np.array(data) # for safety reasons

    for _ in range(samples):
        # Suggest new position
        mu_proposal = np.random.normal(mu_current, proposal_width)

        # Compute likelihood by multiplying probabilities of each data point
        likelihood_current = likelihood_logpdf(data - mu_current).sum()
        likelihood_proposal = likelihood_logpdf(data - mu_proposal).sum()

        # Compute prior probability of current and proposed mu
        prior_current = prior_logpdf(mu_current)
        prior_proposal = prior_logpdf(mu_proposal)

        p_current = likelihood_current + prior_current
        p_proposal = likelihood_proposal + prior_proposal

        # Accept proposal?
        p_accept = np.exp(p_proposal - p_current)

        # Usually would include prior probability, which we neglect here for simplicity
        accept = np.random.rand() < p_accept

        if accept:
            # Update position
            mu_current = mu_proposal

        posterior.append(mu_current)

    return np.array(posterior)




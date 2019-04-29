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
    """Basic Metropolis Hasting Sampler"""
    mu_current = mu_init
    posterior = [mu_current]
    for i in range(samples):
        # Suggest new position
        mu_proposal = stats.norm(mu_current, proposal_width).rvs()

        # Compute likelihood by multiplying probabilities of each data point
        likelihood_current = stats.norm(mu_current+offset, 1).logpdf(data).sum()
        likelihood_proposal = stats.norm(mu_proposal+offset, 1).logpdf(data).sum()

        # Compute prior probability of current and proposed mu
        prior_current = stats.norm(mu_prior_mu, mu_prior_sd).logpdf(mu_current)
        prior_proposal = stats.norm(mu_prior_mu, mu_prior_sd).logpdf(mu_proposal)

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




# Bayesian Inference with Beta Distribution
This repository contains Python code for performing Bayesian inference using the Beta distribution. Bayesian inference is a method of statistical inference in which Bayes' theorem is used to update the probability for a hypothesis as more evidence or information becomes available. The Beta distribution is commonly used as the conjugate prior distribution for the binomial likelihood function, making it well-suited for modeling binary outcomes.
## Overview
The implementation uses Bayesian inference to update prior beliefs about the bias of a coin based on observed outcomes. Here's a brief explanation of the key parts:

1. *Beta Distribution*: The beta distribution is used to represent the prior and posterior beliefs about the bias of the coin. It is characterized by two shape parameters, often denoted as "a" and "b".

2. *Prior Distributions*: Four different prior distributions are considered: Beta(2,5), Beta(5,2), Beta(1,1), and Beta(2,2). These priors represent different initial beliefs about the bias of the coin.

3. *Observed Outcomes*: The coin is tossed 10 times, resulting in 7 heads and 3 tails. These outcomes are used to update the prior distributions.

4. *Likelihood*: The likelihood function calculates the likelihood of observing the outcomes given a specific bias parameter. It is calculated as the product of the probabilities of each individual outcome.

5. *Posterior Distribution*: The posterior distribution represents the updated belief about the bias of the coin after observing the outcomes. It is calculated using Bayes' theorem, which combines the prior distribution and the likelihood function.

6. *Maximum Likelihood Estimate (MLE)*: The MLE is the value of the bias parameter that maximizes the likelihood function given the observed outcomes. It is a point estimate of the true bias of the coin.

7. *Maximum A Posteriori (MAP) Estimate*: The MAP estimate is the value of the bias parameter that maximizes the posterior distribution. It combines the prior belief and the observed data, giving more weight to the prior if the data is limited and more weight to the data if the prior is diffuse.

8. *Plotting*: The code plots the prior distributions, the likelihood, and the posterior distributions for each prior case. It also marks the MLE and MAP estimates on the posterior graphs for visualization.







## Dependencies

- NumPy
- Matplotlib
- Python 3.x

Install dependencies using pip:

## Usage

Run the script `bayesian_inference.py`.
import numpy as np
import matplotlib.pyplot as plt


# Defining the beta distribution function
def beta_distribution(x, a, b):
    return (x * (a - 1) * (1 - x) * (b - 1)) / (np.math.gamma(a) * np.math.gamma(b) / np.math.gamma(a + b))


# Defining the given priors for each case
priors = [(2, 5), (5, 2), (1, 1), (2, 2)]

# Defining the given outcomes
outcomes = ['H', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'T']
num_heads = sum(1 for outcome in outcomes if outcome == 'H')
num_tails = len(outcomes) - num_heads

# Plotting the prior distributions
x_values = np.linspace(0, 1, 100)
plt.figure(figsize=(12, 10))
for i, (a, b) in enumerate(priors, start=1):
    plt.subplot(2, 2, i)
    plt.plot(x_values, beta_distribution(x_values, a, b), label=f'Beta({a},{b})')
    plt.title(f'Prior Distribution (Beta({a},{b}))')
    plt.xlabel('Bias')
    plt.ylabel('Density')
    plt.legend()

# Calculating and plot the likelihood
likelihood = lambda x, num_heads, num_tails: x * num_heads * (1 - x) * num_tails
plt.figure(figsize=(12, 6))
plt.plot(x_values, likelihood(x_values, num_heads, num_tails), label='Likelihood')
plt.title('Likelihood of Observed Outcomes')
plt.xlabel('Bias')
plt.ylabel('Likelihood')
plt.legend()

# Plotting the posterior distributions
plt.figure(figsize=(12, 10))
for i, (a, b) in enumerate(priors, start=1):
    posterior_a = a + num_heads
    posterior_b = b + num_tails
    posterior_values = beta_distribution(x_values, posterior_a, posterior_b)

    # Calculating MLE and MAP estimates
    mle_estimate = x_values[np.argmax(posterior_values)]
    map_estimate = (posterior_a - 1) / (posterior_a + posterior_b - 2)

    plt.subplot(2, 2, i)
    plt.plot(x_values, posterior_values, label=f'Posterior (Beta({posterior_a},{posterior_b}))')
    plt.title(f'Posterior Distribution (Beta({posterior_a},{posterior_b}))')
    plt.xlabel('Bias')
    plt.ylabel('Density')
    plt.axvline(x=mle_estimate, color='r', linestyle='--', label=f'MLE: {mle_estimate:.3f}')
    plt.axvline(x=map_estimate, color='g', linestyle='--', label=f'MAP: {map_estimate:.3f}')
    plt.legend()

plt.tight_layout()
plt.show()

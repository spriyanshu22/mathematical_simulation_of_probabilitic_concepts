# Gaussian Distribution Generator using Inverse Transform Method

## Overview
- First we generate a uniform distribution between 0 and 1
- Then we use the inverse of the cumulative distribution function (CDF) of the Gaussian distribution to transform the uniform distribution into a Gaussian distribution
- We have the PDF of the Gaussian distribution as f(x) = 1/(sigma*sqrt(2*pi)) * exp(-0.5*((x-mu)/sigma)^2)
- From this we can calculate the CDF as F(x) = 1/(sigma*sqrt(2*pi)) * integral(exp(-0.5*((x-mu)/sigma)^2) dx
- We Get F(x) = 1/2 * (1 + erf((x-mu)/(sigma*sqrt(2))))
- We can calculate the inverse of the CDF as F^(-1)(x) = mu + sigma * sqrt(2) * erfinv(2*x - 1)
- Now we can use the inverse of the CDF to transform the uniform distribution into a Gaussian distribution


- Now we first generate a uniform distribution between 0 and 1 say u
- Then we calculate x = F^(-1)(u) = mu + sigma * sqrt(2) * erfinv(2*u - 1) 
- Then we calculate z = mu + sigma * x
- Now z is a Gaussian distributed random variable


## Usage

1. Run the script `gaussian_distribution_generator.py`.
2. Enter the mean (`mu`) and standard deviation (`sigma`) of the Gaussian distribution when prompted.
3. Enter the lower and upper limits of the uniform distribution when prompted.
4. The script generates a histogram of the generated Gaussian distribution along with the actual Gaussian distribution's probability density function (PDF).

## Dependencies

- NumPy
- Matplotlib
- SciPy

Install dependencies using pip:
## Input Validation

- The script validates input to ensure the lower limit is less than the upper limit for the uniform distribution and that the standard deviation is greater than 0.

## Parameters

- `mu`: Mean of the Gaussian distribution.
- `sigma`: Standard deviation of the Gaussian distribution.
- `a`: Lower limit of the uniform distribution.
- `b`: Upper limit of the uniform distribution.
- `n`: Number of samples.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# setting the parameters for the Gaussian distribution
mu = float(input("Enter the mean of the Gaussian distribution: "))
sigma = float(input("Enter the standard deviation of the Gaussian distribution: "))

# taking the parameters for the uniform distribution from the user
a = int(input("Enter the lower limit of the uniform distribution: "))
b = int(input("Enter the upper limit of the uniform distribution: "))

# Checking if the input is valid
if(a >= b):
    print("Invalid input! The lower limit should be less than the upper limit.")
    exit()

if(sigma <= 0):
    print("Invalid input! The standard deviation should be greater than 0.")
    exit()

# Number of samples
n = 10000


arr = []  # array containing new distribution
for _ in range(n):
    v = np.random.uniform(a, b)  # Generate a random number from uniform distribution between a and b
    u = (v-a) / (b-a) # Transform into a uniform distribution between 0 and 1
    x = norm.ppf(u)  # Calculate the inverse cdf of the standard normal distribution
    z = mu + sigma * x  # Transform into required Gaussian distribution
    arr.append(z)

# Plotting pdf of generated Gaussian distribution along with the actual Gaussian distribution
plt.hist(arr, bins=100, density=True, alpha=0.6, color='g')
x = np.linspace(min(arr), max(arr), 1000)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r', linewidth=2)
plt.title("Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

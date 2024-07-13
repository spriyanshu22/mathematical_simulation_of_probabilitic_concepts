# Find the number of students in a class such that the probability that at least two 
# students have the same birthday is greater than 'p' (as discussed in the class). You 
# are allowed to use any language. Your program should input the required probability 
# 'p' and return the number of students (k). You should submit a single zip package 
# containing the source code and a README file that describes how the code can be run.
# You can do the project in a team with at most 5 members (including you).

# /* 
#     Let A be the event that no two students have the same birthday: 
#     P(A) = 365Pn / 365^n  for n <= 365
#            1 for n > 365
#          = 365! / (365^n * (365-n)!) for n <= 365
#            1 for n > 365

#     Let B be the event that at least two students have the same birthday:
#     P(B) = 1 - P(A)
#          = 1 - (365Pn / 365^n) for n <= 365
#            0 for n > 365
#          = 1 - (365! / (365^n * (365-n)!)) for n <= 365
#            0 for n > 365
#     Now the factorial of 365 is a very large number and the value of n varies from 1 to 365 so we can't calculate the value of P(B) for each n directly, so we use logarithms to calculate the value of P(B) for each n.
#     Method: 
#     We know that log(a*b) = log(a) + log(b)
#     So we can use this property to calculate the value of P(B) for each n.
#     P(B) = 1 - (365! / (365^n * (365-n)!))
#         = 1 - exp(log(365!) - log(365^n) - log(365-n)!)
#         = 1 - exp(log(365!) - n*log(365) - log(365-n)!)
#     Now we can calculate the value of P(B) for each n using the above formula.
#     We can also plot the graph of P(B) vs n to see how the probability varies with n.

#     Now we need to find log(n!) we use STIRLING'S APPROXIMATION:
#     log(n!) = 0.5 * log(2*pi) + (n+0.5)* log(n) - n
#     We can use this formula to calculate the value of log(n!) for each n.

#     Now we can vary n from 1 to 365 and calculate P(B) for each n.
#     Then plot the graph of P(B) vs n and store the values in an array
#     Now we can input the value of p and then find required using binary search

# */

import math
import matplotlib.pyplot as plt
import numpy as np

def logFactorialUsingStirlingAprox(n):
    if n <= 0:
        return 0
    return 0.5 * math.log(2 * math.pi) + (n + 0.5) * math.log(n) - n


def calculateProbability(n):
    if n > 365:
        return 0
    return 1 - math.exp(logFactorialUsingStirlingAprox(365) - logFactorialUsingStirlingAprox(365-n) - n * math.log(365))

def plotGraph():
    x = np.arange(1, 366, 1)
    y = [calculateProbability(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('Number of students')
    plt.ylabel('Probability')
    plt.title('Probability of at least two students having the same birthday')
    plt.show()

def findNumberOfStudents(p):
    low = 1
    high = 365
    if p < 0 or p > 1 :
        return 'Error: Invalid probabilty.'
    if p == 0 :
        return 0
    if p == 1 :
        return 366
    while low < high:
        mid = (low + high) // 2
        if calculateProbability(mid) < p:
            low = mid + 1
        else:
            high = mid
    return low

def main():
    p = float(input("Enter the required probability: "))
    plotGraph()
    print(f"The number of students required for the probability to be greater than {p} is {findNumberOfStudents(p)}")

main()
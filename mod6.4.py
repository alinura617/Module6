# Alinura Sultanova
# 08.08.2023
import math

def approximate_pi(n):
    approx_pi = 0
    sign = 1
    
    for i in range(1, n+1, 2):
        approx_pi += sign * (1 / i)
        sign *= -1
    
    return 4 * approx_pi

# Number of terms for approximation
num_terms = 100000

approximated_value = approximate_pi(num_terms)
actual_value = math.pi

# Print the result with a nice message
print("Approximated π:", approximated_value)
print("Actual π from math module:", actual_value)

#finish
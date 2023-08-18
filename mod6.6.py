# Alinura Sultanova
# 08.08.2023

import math

# Function to calculate factorial using a for loop
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Get user input for the value
user_input = int(input("Enter a number: "))

# Calculate factorial using the custom function
factorial_calculated = calculate_factorial(user_input)

# Calculate factorial using the factorial function from the math module
factorial_math_module = math.factorial(user_input)

# Print the results
print("User input value:", user_input)
print("Calculated factorial:", factorial_calculated)
print("Factorial using math module:", factorial_math_module)

#finish
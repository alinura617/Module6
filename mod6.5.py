# Alinura Sultanova
# 08.08.2023

import math

def radians_to_degrees(radians):
    return radians * (180 / math.pi)

# Get user input for radians
radians = float(input("Enter radians: "))

# Calculate degrees using the conversion function
degrees_calculated = radians_to_degrees(radians)

# Calculate degrees using the degrees function from the math module
degrees_math_module = math.degrees(radians)

# Print the results
print("User input radians:", radians)
print("Calculated degrees:", degrees_calculated)
print("Degrees using math module:", degrees_math_module)

#finish
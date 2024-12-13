#program to simulate pythagorean theorems
import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

side_a = 3
side_b = 4
hypotenuse = calculate_hypotenuse(side_a, side_b)

print(f"Hypotenuse: {hypotenuse}")

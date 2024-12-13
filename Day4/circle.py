#Program to calculate the area and circumference of the circle
import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * math.pi * radius

radius = 5
area = calculate_area(radius)
circumference = calculate_circumference(radius)

print(f"Area: {area}")
print(f"Circumference: {circumference}")

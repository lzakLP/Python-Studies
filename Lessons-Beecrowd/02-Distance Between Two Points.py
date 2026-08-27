# Beecrowd 1015 - Distance Between Two Points
#
# Read the coordinates of two points in a two-dimensional plane.
#
# Calculate the distance between the two points using the following formula:
#
# distance = √((x2 - x1)² + (y2 - y1)²)
#
# Input:
# The input contains two lines.
# Each line contains two floating-point values representing
# the coordinates of a point (x, y).
#
# Output:
# Print the distance between the two points with exactly 4 decimal places.

import math

axes = input().split()
x1 = float(axes[0])
y1 = float(axes[1])

axes = input().split()
x2 = float(axes[0])
y2 = float(axes[1])

e_x = x2 - x1
e_y = y2 - y1

result1 = e_x ** 2
result2 = e_y ** 2

total = result1 + result2

distance = math.sqrt(total)

print(f"{distance:.4f}")

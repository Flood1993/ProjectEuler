from scipy.integrate import dblquad
import numpy as np

"""
Suppose we have a triangle like this
      
B(0, 3)
+
+---+
|    +--+
|        +--+
|  P(x, y)   +---+
|                 ++
+--------------------+ C(4, 0)
A(0, 0)

What we want to calculate is the average angle PBC for all possible points P in the triangle, divided by 2*pi.
Note that the area of the triangle is 6.

The hypotenuse is given by x=-4x/3 + 4

Hence, we use the dot product to calculate said angle, and then integrate the arccos of that (so we get the angle)
for all points in the triangle.

Then, we divide the result by 6 (area) and by 2*pi to find the probability, resulting in dividing by 12*pi.
"""

integral = dblquad(lambda x, y: np.arccos((-4*x + x**2 - 3*y + y**2) / ((y**2 + (4 - x)**2)**0.5 * (x**2 + (3-y)**2)**0.5)), 0, 3, lambda x: 0, lambda x: -4*x/3 + 4)

print(integral[0]/(12*np.pi))
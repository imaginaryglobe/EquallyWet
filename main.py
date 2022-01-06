"""this is a program for the extended homework, "Equally Wet"
the main idea of this program is to find the midpoint of three points on the coordinate plane.
finding the midpoint is finding the circumcenter of the  three x coordinates and y coordinates"""

"""
TODO:
1. create three points, in this case they are named A, B, and C                                  done
2. calculate the slope between each of the points (slope ab, slope ac, and slope bc)             done
3. find the perpendicular bisectors of each line segment of the triangle (negative reciprocal)





clean up so it looks nicer TBD
"""


import math 
import random

x1 = random.randint(-100, 100)
x2 = random.randint(-100, 100)
x3 = random.randint(-100, 100)
y1 = random.randint(-100, 100)
y2 = random.randint(-100, 100)
y3 = random.randint(-100, 100)

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)

ab = (y2 - y1) / (x2 - x1)
bc = (y3 - y2) / (x3 - x2)
ac = (y3 - y1) / (x3 - x1)




print(a, b, c)
print(f"the slopes are {ab} for ab, {bc} for bc, and {ac} for ac.")
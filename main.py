"""this is a program for the extended homework, "Equally Wet"
the main idea of this program is to find the midpoint of three points on the coordinate plane.
finding the midpoint is finding the circumcenter of the  three x coordinates and y coordinates"""

"""
TODO:
1. create three points, in this case they are named A, B, and C                                  done
2. calculate the slope between each of the points (slope ab, slope ac, and slope bc)             done
3. find the perpendicular bisectors of each line segment of the triangle (negative reciprocal)   done





clean up so it looks nicer TBD
"""


import math 
import random

# picks random numbers for the random point locations on the grid, in this case the numbers are between -100 and 100, inclusive. 
x1 = random.randint(-100, 100)
x2 = random.randint(-100, 100)
x3 = random.randint(-100, 100)
y1 = random.randint(-100, 100)
y2 = random.randint(-100, 100)
y3 = random.randint(-100, 100)

# put the points into ordered pairs
a = (x1, y1)
b = (x2, y2)
c = (x3, y3)

# this section of code finds the slope of the line by using rise over run equation.
ab = (y2 - y1) / (x2 - x1)
bc = (y3 - y2) / (x3 - x2)
ac = (y3 - y1) / (x3 - x1)


# this section of code finds the negative reciprocal of the slope, which is the slope of the perpendicular bisector
def negative_reciprocal(slope):
    # make it negative
    slope *= -1
    #reciprocal
    slope = 1 / slope

    return slope

# this section of code just tells you what the slopes and perpendicular bisector slopes are
print("--------------------------------------")
print(a, b, c)
print(f"the slopes are {ab} for ab, {bc} for bc, and {ac} for ac.")

nAB = negative_reciprocal(ab)
nBC = negative_reciprocal(bc)
nAC = negative_reciprocal(ac)
print(f"the negative reciprocal slopes are {nAB}, {nBC}, and {nAC} for ab, bc, ac")
print("--------------------------------------")
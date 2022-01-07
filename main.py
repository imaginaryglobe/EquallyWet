"""this is a program for the extended homework, "Equally Wet"
the main idea of this program is to find the midpoint of three points on the coordinate plane.
finding the midpoint is finding the circumcenter of the  three x coordinates and y coordinates"""

"""
TODO:
1. create three points, in this case they are named A, B, and C                                  done
2. calculate the slope between each of the points (slope ab, slope ac, and slope bc)             done
3. find the perpendicular bisectors of each line segment of the triangle (negative reciprocal)   done
4. find the circumcenter
    a. add error cases
        i. these include collinear points
        ii. also points that have the same coordinates





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


# find every single point on each line and check if they intersect
def find_y_int(slope, point):
    #finding the equation of the line is simple.
    # plug in the coordinate pair for y = mx + b as y and then solve for b
    b = point[1] - slope * point[0]
    return b


# this section of code just tells you what the slopes and perpendicular bisector slopes are
print("--------------------------------------")
print(a, b, c)
print(f"the slopes are {ab} for ab, {bc} for bc, and {ac} for ac.")

nAB = negative_reciprocal(ab)
nBC = negative_reciprocal(bc)
nAC = negative_reciprocal(ac)
print(f"the negative reciprocal slopes are {nAB}, {nBC}, and {nAC} for ab, bc, ac")

yint_of_ab = find_y_int(ab, a)
yint_of_bc = find_y_int(bc, b)
yint_of_ac = find_y_int(ac, c)
print(yint_of_ab, yint_of_bc, yint_of_ac)
print("--------------------------------------")
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
    b. somehow check the points on each line and add them to a list 
        i. probably in integer increments of 1, if the distance between all three lines is < 1
        at any point, i will call that an intersection probably





clean up so it looks nicer TBD
"""


import math 
import random
import ast


points = []

# picks random numbers for the random point locations on the grid, in this case the numbers are between -100 a100axi, inclusive. 
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


midpoint_ab = (((x1 + x2) / 2), ((y1 + y2) / 2))
midpoint_bc = (((x3 + x2) / 2), ((y3 + y2) / 2))
midpoint_ac = (((x1 + x3) / 2), ((y1 + y3) / 2))

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

nAB = negative_reciprocal(ab)
nBC = negative_reciprocal(bc)
nAC = negative_reciprocal(ac)

# find every single point on each line and check if they intersect
def find_y_int(slope, point):
    #finding the equation of the line is simple.
    # plug in the coordinate pair for y = mx + b as y and then solve for b
    b = point[1] - slope * point[0]
    return b
#determining the y intercepts by passing in points
yint_of_ab = find_y_int(nAB, midpoint_ab)
yint_of_bc = find_y_int(nBC, midpoint_bc)
yint_of_ac = find_y_int(nAC, midpoint_ac)
# 
ab_data = (midpoint_ab, yint_of_ab)
bc_data = (midpoint_bc, yint_of_bc)
ac_data = (midpoint_ac, yint_of_ac)

equation_ab = f"y = {nAB}x + {yint_of_ab}"
equation_bc = f"y = {nBC}x + {yint_of_bc}"
equation_ac = f"y = {nAC}x + {yint_of_ac}"

def return_y_coordinates(equation):
    formula = equation[4:]
    formula = formula.replace("x", " * x")
    for i in range(100):
        new_equation = formula.replace("x", str(i))
        new_y = eval(new_equation)
        new_coordinate_set = (i, new_y)
        points.append(new_coordinate_set)


return_y_coordinates(equation_ab)


# this section of code just tells you what the slopes and perpendicular bisector slopes are
print("\n----------------------------------------------------------------------------------")
print(a, b, c)
print(f"normal slopes: ab({ab}), bc({bc}), ac({ac}) \n")

print(f"perpendicular slopes: ab({nAB}), bc({nBC}), and ac({nAC})\n")
print(f"y intercepts of perp. slopes ab({yint_of_ab}), bc({yint_of_bc}), and ac({yint_of_ac}) \n")
print(f"equations of perp line: ab({equation_ab}), bc({equation_bc}), ac({equation_ac})")
print(points)
print("------------------------------------------------------------------------------------\n")
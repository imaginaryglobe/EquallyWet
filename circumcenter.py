# https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcenter_coordinates
# formula taken from here

def circumcenter():
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    x = ((x1 * x1 + y1 * y1) * (y2 - y3) + (x2 * x2 + y2 * y2) * (y3 - y1) + (x3 * x3 + y3 * y3) * (y1 - y2)) / d
    y = ((x1 * x1 + y1 * y1) * (x3 - x2) + (x2 * x2 + y2 * y2) * (x1 - x3) + (x3 * x3 + y3 * y3) * (x2 - x1)) / d
    return (x, y)


x1 = int(input('What is x of point 1?'))
y1 = int(input('What is y of point 1?'))
x2 = int(input('What is x of point 2?'))
y2 = int(input('What is y of point 2?'))
x3 = int(input('What is x of point 3?'))
y3 = int(input('What is y of point 3?'))

print(circumcenter())
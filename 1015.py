# 1015 - Distance Between Two Points

'''
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, according to the formula:

Distance = 

Input
The input file contains two lines of data. The first one contains two double values: x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

Output
Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.
'''

import math

xy1 = input().split()
xy2 = input().split()

x1 = float(xy1[0])
y1 = float(xy1[1])

x2 = float(xy2[0])
y2 = float(xy2[1])

def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print('{:0.4f}'.format(distance))

distance(x1, y1, x2, y2)

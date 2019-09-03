from numpy import *


def better_than_average(class_points, your_points):
    a = mean(class_points)

    return a < your_points
    # Your code here

#!/bin/python3

import math

class Points(object):
    
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return Points(x, y, z)

    def dot(self, no):
        x_dot = no.x * self.x
        y_dot = no.y * self.y
        z_dot = no.z * self.z
        return x_dot + y_dot + z_dot

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    # points = list()
    # for i in range(4):
    #     a = list(map(float, input().split()))
    #     points.append(a)
    
    points = list((
        [0, 4, 5], 
        [1, 7, 6],
        [0, 5, 9],
        [1, 7, 2]
        )
    )

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x*v.x, self.y*v.y)

    def __iadd__(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def __mul__(self, v):
        return Vector(self.x*v, self.y*v)

    def __eq__(self, v):
        if(type(v) == Vector):
            return self.x == v.x and self.y == v.y
        else:
            return math.sqrt(self.x**2 + self.y**2) == v

    def __ne__(self, v):
        if(type(v) == Vector):
            return self.x != v.x or self.y != v.y
        else:
            return math.sqrt(self.x**2 + self.y**2) != v

    def __lt__(self, v):
        return math.sqrt(self.x**2 + self.y**2) < math.sqrt(v.x**2 + v.y**2)

    def __truediv__(self, v):
        return Vector(self.x/v.x, self.y/v.y)

    def resetNonZero(self, v):
        if v.x != 0:
            self.x = 0
        if v.y != 0:
            self.y = 0

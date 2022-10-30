import math


class calculator:
    def __init__(self, g=9.81):
        self.g = g

    def __sin(self, x):
        return math.sin(math.radians(x))

    def initial_velocity(self, deltax: float, theta: int):
        return math.sqrt((deltax * self.g) / (self.__sin(2 * theta)))

    def get_height(self, vi: float, theta: int):
        return (vi ** 2) * ((self.__sin(theta)) ** 2) / (2 * self.g)

    def get_deltax(self, vi: float, theta: int):
        return ((vi ** 2) * self.__sin(2 * theta)) / self.g

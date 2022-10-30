from .calculator import *
from .renderTool import RenderTool


class Motion:
    def __init__(self, theta: int, vi=None, deltax=None, g=9.81):
        if not (0 < theta < 90):
            raise ValueError("Theta must be between 90 and 0")
        self._theta = theta
        self.g = g
        self.calculator = calculator(self.g)

        if (not vi) and (not deltax):
            raise ValueError("Both vi and deltax cannot be pre defined. Define either vi or deltax")
        if not vi:
            self.__defined = "dx"
        else:
            self.__defined = "vi"

        if deltax:
            self._deltax = deltax
            self._vi = self.calculator.initial_velocity(deltax, theta)
        elif vi:
            self._vi = vi
            self._deltax = self.calculator.get_deltax(vi, theta)

        self.height = self.calculator.get_height(self.vi, theta)
        self.apogee = ((self.deltax / 2), self.height)

    def __recalculate(self, changed):
        if changed == "t":
            if self.__defined == "dx":
                self._vi = self.calculator.initial_velocity(self.deltax, self.theta)
            else:
                self._deltax = self.calculator.get_deltax(self.vi, self.theta)
        elif changed == "dx":
            self._vi = self.calculator.initial_velocity(self.deltax, self.theta)
        elif changed == "vi":
            self._deltax = self.calculator.get_deltax(self.vi, self.theta)
        self.height = self.calculator.get_height(self.vi, self.theta)
        self.apogee = ((self.deltax / 2), self.height)

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, t: int):
        if not (0 < t < 90):
            raise ValueError("Theta must be between 90 and 0")
        self._theta = t
        self.__recalculate("t")

    @property
    def deltax(self):
        return self._deltax

    @deltax.setter
    def deltax(self, d: float):
        if d < 0:
            raise ValueError("Δx must be greater than 0")
        self._deltax = d
        self.__recalculate("dx")

    @property
    def vi(self):
        return self._vi

    @vi.setter
    def vi(self, v: float):
        if v < 0:
            raise ValueError("vᵢ must be greater than 0")
        self._vi = v
        self.__recalculate("vi")

    def plot(self, resolution: float = 0.1):
        renderer = RenderTool(self)
        renderer.render_parabola(resolution)

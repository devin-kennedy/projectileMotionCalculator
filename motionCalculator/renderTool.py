import matplotlib
import matplotlib.pyplot as plt
import decimal


class RenderTool:
    def __init__(self, motion):
        self.motion = motion
        self.deltax = motion.deltax
        self.apogeeX = motion.apogee[0]
        self.height = motion.apogee[1]
        self.a = None
        matplotlib.use('TkAgg')

    def parabola_y(self, x):
        if not self.a:
            raise ValueError("a must be defined")
        return (self.a * ((x - self.apogeeX) ** 2)) + self.height

    def drange(self, x, y, jump):
        while x < y:
            yield float(x)
            x += decimal.Decimal(jump)

    def render_parabola(self, resolution: float):
        self.a = -(self.height / ((0 - self.apogeeX) ** 2))
        points = []

        for x in self.drange(0, self.deltax + resolution, str(resolution)):
            y = self.parabola_y(x)
            points.append((x, y))

        lim = self.deltax if self.deltax > self.height else self.height
        lim = lim + (lim/8)

        fontsize = 12
        plt.plot(*zip(*points))
        plt.text(self.apogeeX * (1 + 0.01), self.height * (1 + 0.01), f"Height: {float('%.6g' % self.height)}", fontsize=fontsize)
        plt.text(self.deltax * (1 + 0.01), 0, "Δx", fontsize=fontsize)
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.title(f"Plot of motion where \nvᵢ = {self.motion.vi}, Δx = {float('%.6g' % self.deltax)} and θ = {self.motion.theta}")
        plt.xlim([0, lim])
        plt.ylim([0, lim])
        plt.show()


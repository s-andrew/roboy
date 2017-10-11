import numpy as np


class Polygon():
    def __init__(self, vertices, center = (0,0), color = (0, 0, 0)):
        self.vertices = np.matrix(vertices)
        self.center = np.matrix(center)
        self.color = color

    def rotate(self, angle):
        c, s = np.cos(np.radians(angle)), np.sin(np.radians(angle))
        r = np.matrix("{} {}; {} {}".format(c, -s, s, c))
        self.vertices = (self.vertices - self.center) * r + self.center
        return self

    def scale(self, scale):
        self.vertices *= scale
        self.center *= scale
        return self

    def move(self, xy):
        self.vertices += np.matrix(xy)
        self.center += np.matrix(xy)
        return self

    def moveTo(self, xy):
        point = np.matrix(xy)
        self.vertices = self.vertices - self.center + point
        self.center = point
        return self

    def render(self, draw):
        draw.polygon([tuple(i) for i in self.vertices.tolist()], fill=self.color)

    def setColor(self, color):
        self.color = color
        return self


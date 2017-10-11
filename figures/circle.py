import numpy as np

class Circle:
    def __init__(self, center, r, color=(0,0,0)):
        self.center = np.matrix(center)
        self.r = r
        self.color = color

    def rotate(self, angle):
        return self

    def scale(self, scale):
        self.r *= scale
        return self

    def move(self, xy):
        self.center += np.matrix(xy)
        return self

    def moveTo(self, xy):
        self.center = np.matrix(xy)
        return self

    def render(self, draw):
        x = self.center[0, 0]
        y = self.center[0, 1]
        draw.ellipse((x - self.r, y - self.r, x + self.r, y + self.r), fill=self.color)

    def setColor(self, color):
        self.color = color
        return self

from figures.polygon import Polygon

def Rectangle(point1, point2, color=(0, 0, 0)):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    return Polygon(((x1, y1), (x2, y1), (x2, y2), (x1, y2)), center=((x2-x1), (y2-y1)), color=color)

    # def render(self, draw):
    #     draw.rectangle((self.point1, self.point2), fill=self.color)
    #
    # def setColor(self, color):
    #     self.color = color
    #     return self


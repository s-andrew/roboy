import math

import numpy as np
from PIL import ImageDraw

from figures.circle import Circle


class Ex3:
    AMOUNT_OF_DATAPOINTS = 90
    def __init__(self, img):
        self.img = img


    def doEx(self, robot, startPoint, endPoint, delta, edgeColor, backgroundColor):
        def distance(xy1, xy2):
            return math.sqrt((xy2[0]-xy1[0])**2 + (xy2[1]-xy1[1])**2)


        width, height = self.img.size
        pixel = self.img.load()
        emptyPoint =  []
        for i in range(width):
            for j in range(height):
                if pixel[i, j] == backgroundColor:
                    emptyPoint.append((i, j))
        n = len(emptyPoint)
        dataPoints = [startPoint, endPoint]

        while len(dataPoints) < self.AMOUNT_OF_DATAPOINTS:
            point = emptyPoint[np.random.random_integers(n-1)]
            f = True
            for i in dataPoints:
                if distance(point, i) < delta:
                    f = False
                    break
            if f:
                dataPoints.append(point)
            # else:
            #     break

        draw = ImageDraw.Draw(self.img)
        c = Circle((0,0), 2, edgeColor)
        for xy in dataPoints:
            c.moveTo(xy).render(draw)

        print(len(dataPoints))
        robot.moveTo(startPoint).render(draw)

        c.setColor((0,0,0)).moveTo(startPoint).render(draw)
        c.setColor((0,0,0)).moveTo(endPoint).render(draw)
        return self.img, dataPoints


#    def doFirstClick(self, startPoint, color, robot):
#        self.startPoint = startPoint
#        draw = ImageDraw.Draw(self.img)
#        robot.moveTo(startPoint).render(draw)
#        Circle(startPoint, 3, color).render(draw)
#        return self.img
#
#
#    def doSecondClick(self, endPoint, delta, edgeColor, backgroundColor):
#
#        def distance(xy1, xy2):
#            return math.sqrt((xy2[0]-xy1[0])**2 + (xy2[1]-xy1[1])**2)
#
#        c = Circle((0,0), 3, edgeColor)
#        width, height = self.img.size
#        pixel = self.img.load()
#        emptyPoint =  []
#        for i in range(width):
#            for j in range(height):
#                if pixel[i, j] == backgroundColor:
#                    emptyPoint.append((i, j))
#        n = len(emptyPoint)
#        dataPoints = [self.startPoint, endPoint]
#
#        while len(dataPoints) < self.AMOUNT_OF_DATAPOINTS:
#            point = emptyPoint[np.random.random_integers(n-1)]
#            f = True
#            for i in dataPoints:
#                if distance(point, i) < delta:
#                    f = False
#                    break
#            if f:
#                dataPoints.append(point)
#            # else:
#            #     break
#
#        draw = ImageDraw.Draw(self.img)
#        for xy in dataPoints:
#            c.moveTo(xy).render(draw)
#
#        print(len(dataPoints))
#        # Grid
#        # for i in range(0, width, delta):
#        #     draw.line(((i,0), (i, height)), fill=(0, 0, 0))
#        #
#        # for j in range(0, height, delta):
#        #     draw.line(((0, j), (width, j)), fill=(0, 0, 0))
#
#        c.setColor((0,0,0)).moveTo(self.startPoint).render(draw)
#        c.setColor((0,0,0)).moveTo(endPoint).render(draw)
#        return self.img









import numpy as np
from PIL import ImageDraw
from scipy.interpolate import interp1d

from figures.circle import Circle

#help(interp1d)


class Ex6:
    def __init__(self, img):
        self.img = img

    def doEx(self, nodes, shortestPathPointsId, pathColor):
#        x = []
#        y = []
#        for nodeId in shortestPathPointsId:
#            x.append(nodes[nodeId][0])
#            y.append(nodes[nodeId][1])
        def midpoint(xy1, xy2):
            return (xy1[0] + xy2[0]) / 2, (xy1[1] + xy2[1]) / 2

        # start point
        x = [nodes[shortestPathPointsId[0]][0]]
        y = [nodes[shortestPathPointsId[0]][1]]

        # midpoints
        prevPoint = nodes[shortestPathPointsId[1]]
        for nodeId in shortestPathPointsId[2:-1]:
            currentPoint = nodes[nodeId]
            mx, my = midpoint(prevPoint, currentPoint)
            x.append(mx)
            y.append(my)
            prevPoint = currentPoint

        # end point
        x.append(nodes[shortestPathPointsId[-1]][0])
        y.append(nodes[shortestPathPointsId[-1]][1])

        draw = ImageDraw.Draw(self.img)
#        brush = Circle((0,0), 2, pathColor)
#        for p in zip(x,y):
#            brush.moveTo(p).render(draw)


#        print("x", x)
#        print("y", y)
#
#        start = int(nodes[shortestPathPointsId[0]][0])
#        end = int(nodes[shortestPathPointsId[-1]][0])
#
#        x1 = [0, 400]
#        y1 = [0, 400]
#        f = interp1d(x1, y1, kind="linear")
#        width, height = self.img.size
##        pixel = self.img.load()
#        prevPoint = (start, f(start))
#
#        for x in range(start + 1, end + 1):
#            currentPoint = (x, int(f(x)))
#            draw.line((prevPoint, currentPoint), fill=(255,0,0), width=2)
#            prevPoint = currentPoint


        x, y = catmull_rom(x, y, 50)
        interpolate = [i for i in zip(x,y)]
        prevPoint = (int(interpolate[0][0]), int(interpolate[0][1]))

        for interpolatePoint in interpolate[1:]:
            currentPoint = (int(interpolatePoint[0]), int(interpolatePoint[1]))
            draw.line((prevPoint, currentPoint), fill=pathColor, width=2)
            prevPoint = currentPoint


        return self.img







def catmull_rom_one_point(x, v0, v1, v2, v3):
    """Computes interpolated y-coord for given x-coord using Catmull-Rom.
    Computes an interpolated y-coordinate for the given x-coordinate between
    the support points v1 and v2. The neighboring support points v0 and v3 are
    used by Catmull-Rom to ensure a smooth transition between the spline
    segments.
    Args:
        x: the x-coord, for which the y-coord is needed
        v0: 1st support point
        v1: 2nd support point
        v2: 3rd support point
        v3: 4th support point
    """
    c1 = 1. * v1
    c2 = -.5 * v0 + .5 * v2
    c3 = 1. * v0 + -2.5 * v1 + 2. * v2 -.5 * v3
    c4 = -.5 * v0 + 1.5 * v1 + -1.5 * v2 + .5 * v3
    return (((c4 * x + c3) * x + c2) * x + c1)

def catmull_rom(p_x, p_y, res):
    """Computes Catmull-Rom Spline for given support points and resolution.
    Args:
        p_x: array of x-coords
        p_y: array of y-coords
        res: resolution of a segment (including the start point, but not the
            endpoint of the segment)
    """
    # create arrays for spline points
    x_intpol = np.empty(res*(len(p_x)-1) + 1)
    y_intpol = np.empty(res*(len(p_x)-1) + 1)

    # set the last x- and y-coord, the others will be set in the loop
    x_intpol[-1] = p_x[-1]
    y_intpol[-1] = p_y[-1]

    # loop over segments (we have n-1 segments for n points)
    for i in range(len(p_x)-1):
        # set x-coords
        x_intpol[i*res:(i+1)*res] = np.linspace(
            p_x[i], p_x[i+1], res, endpoint=False)
        if i == 0:
            # need to estimate an additional support point before the first
            y_intpol[:res] = np.array([
                catmull_rom_one_point(
                    x,
                    p_y[0] - (p_y[1] - p_y[0]), # estimated start point,
                    p_y[0],
                    p_y[1],
                    p_y[2])
                for x in np.linspace(0.,1.,res, endpoint=False)])
        elif i == len(p_x) - 2:
            # need to estimate an additional support point after the last
            y_intpol[i*res:-1] = np.array([
                catmull_rom_one_point(
                    x,
                    p_y[i-1],
                    p_y[i],
                    p_y[i+1],
                    p_y[i+1] + (p_y[i+1] - p_y[i]) # estimated end point
                ) for x in np.linspace(0.,1.,res, endpoint=False)])
        else:
            y_intpol[i*res:(i+1)*res] = np.array([
                catmull_rom_one_point(
                    x,
                    p_y[i-1],
                    p_y[i],
                    p_y[i+1],
                    p_y[i+2]) for x in np.linspace(0.,1.,res, endpoint=False)])


    return (x_intpol, y_intpol)


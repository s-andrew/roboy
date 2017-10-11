import math

from PIL import ImageDraw
from scipy.spatial import Delaunay
from scipy.interpolate import interp1d


class Ex4:
    MAX_ANGELE = 180
    def __init__(self, img):
        self.img = img

    def doEx(self, dataPoints, edgeColor, wallColor, restrictedAreaColor):
        def distance(xy1, xy2):
            return math.sqrt((xy2[0]-xy1[0])**2 + (xy2[1]-xy1[1])**2)

        def midpoint(xy1, xy2):
            return (xy1[0] + xy2[0]) / 2, (xy1[1] + xy2[1]) / 2

        def triangleAngles(v1, v2, v3):
            """
            Args:
                v1, v2, v3: tuples with coord of vertex

            Return: angle from v1, angle from v1, angle from v1

            """

            e1 = distance(v2, v3)
            e2 = distance(v1, v3)
            e3 = distance(v1, v2)

            a1 = math.acos((e2**2 + e3**2 - e1**2) / (2 * e2 * e3))
            a2 = math.acos((e1**2 + e3**2 - e2**2) / (2 * e1 * e3))
            a3 = math.acos((e2**2 + e1**2 - e3**2) / (2 * e2 * e1))

            return a1, a2, a3

        def pixelCheck(pix):
            return pix !=wallColor and pix != restrictedAreaColor


        tri = Delaunay(dataPoints)
        draw = ImageDraw.Draw(self.img)
        pixel = self.img.load()
        edges = []
        nodes = {}
        for p1, p2, p3 in tri.simplices:
            v1 = tuple(tri.points[p1])
            v2 = tuple(tri.points[p2])
            v3 = tuple(tri.points[p3])
            xs, ys = tuple(zip(v1, v2, v3))
            x = sum(xs) // 3
            y = sum(ys) // 3

#            f1 = interp1d([v2[0], v3[0]], [v2[1], v3[1]], kind="linear")
#            line1 = [pixel[x, int(f1(x))] for x in range(int(v2[0]), int(v3[0]))]
#
#            f2 = interp1d([v1[0], v3[0]], [v1[1], v3[1]], kind="linear")
#            line2 = [pixel[x, int(f2(x))] for x in range(int(v1[0]), int(v3[0]))]
#
#            f3 = interp1d([v1[0], v2[0]], [v1[1], v2[1]], kind="linear")
#            line3 = [pixel[x, int(f3(x))] for x in range(int(v1[0]), int(v2[0]))]
#
#
#            if max(triangleAngles(v1, v2, v3)) * 57.2958 < self.MAX_ANGELE\
#                  and all(map(pixelCheck, line1))\
#                  and all(map(pixelCheck, line2))\
#                  and all(map(pixelCheck, line3)):
            if max(triangleAngles(v1, v2, v3)) * 57.2958 < self.MAX_ANGELE\
                    and pixel[midpoint(v1, v2)] != wallColor and pixel[midpoint(v1, v2)] != restrictedAreaColor\
                    and pixel[midpoint(v1, v3)] != wallColor and pixel[midpoint(v1, v3)] != restrictedAreaColor\
                    and pixel[midpoint(v3, v2)] != wallColor and pixel[midpoint(v3, v2)] != restrictedAreaColor:
#                    and pixel[x, y] != wallColor and pixel[x, y] != restrictedAreaColor:

                draw.line((v1, v2, v3, v1), fill=edgeColor, width=1)
                nodes.update({p1: v1, p2: v2, p3: v3})
                edges.extend([(p1, p2, {"weight" : distance(v1, v2)}), (p2, p3, {"weight" : distance(v2, v3)}), (p3, p1, {"weight" : distance(v3, v1)})])


        return self.img, nodes, edges

#v1 = ("x1", "y1")
#v2 = ("x2", "y2")
#v3 = ("x3", "y3")
#for i in zip(v1, v2, v3):
#    print(i)
#xs, ys = tuple(zip(v1, v2, v3))


#==============================================================================
# def distance(xy1, xy2):
#     return math.sqrt((xy2[0]-xy1[0])**2 + (xy2[1]-xy1[1])**2)
# def triangleAngles(v1, v2, v3):
#     """
#     Args:
#         v1, v2, v3: tuples with coord of vertex
#     Return: angle from v1, angle from v1, angle from v1
#     """
#     e1 = distance(v2, v3)
#     e2 = distance(v1, v3)
#     e3 = distance(v1, v2)
#     a1 = math.acos((e2**2 + e3**2 - e1**2) / (2 * e2 * e3))
#     a2 = math.acos((e1**2 + e3**2 - e2**2) / (2 * e1 * e3))
#     a3 = math.acos((e2**2 + e1**2 - e3**2) / (2 * e2 * e1))
#     return a1, a2, a3
# v1 = (0, 0)
# v2 = (0, 4)
# v3 = (3, 0)
# a = triangleAngles(v1, v2, v3)
# max(a) * 57.2958
#==============================================================================
#print(a1 * 57.2958, a2 * 57.2958, a3 * 57.2958)

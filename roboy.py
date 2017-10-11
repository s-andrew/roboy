import sys

from PIL import Image


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, QLabel)
from PyQt5.QtGui import QPixmap

from exercises.ex1 import Ex1
from exercises.ex2 import Ex2
from exercises.ex3 import Ex3
from exercises.ex4 import Ex4
from exercises.ex5 import Ex5
from exercises.ex6 import Ex6


OUTPUT_PATH = "outputs\\"

BACKGROUND_COLOR = (255, 255, 255)
ROBOT_COLOR = (255, 204, 0)
WALL_COLOR = (0, 0, 255)
RESTRICTED_AREA_COLOR = (128, 194, 255)
#EDGE_COLOR = (27, 255, 14)
EDGE_COLOR = (160, 160, 160)
#PATH_COLOR = ()
PATH_COLOR = (255, 0, 0)


if __name__ == "__main__":
#==============================================================================
#      Create image
#==============================================================================
    img = Image.new("RGB", (400, 400), BACKGROUND_COLOR)


#==============================================================================
#      Draw wall
#==============================================================================
    img, robot = Ex1(img).doEx(ROBOT_COLOR, WALL_COLOR)
    img.save(OUTPUT_PATH + "roboyEx1.png")

#==============================================================================
#      Draw restricted area
#==============================================================================
    img = Ex2(img).doEx(ROBOT_COLOR, WALL_COLOR, RESTRICTED_AREA_COLOR, BACKGROUND_COLOR, robot)
    img.save(OUTPUT_PATH + "roboyEx2.png")


#==============================================================================
#      Set start point and end point
#==============================================================================
    startPoint = (40, 320)
    endPoint = (350, 100)


#==============================================================================
#     Draw data points
#==============================================================================
    #img = Image.new("RGB", (800, 400), BACKGROUND_COLOR)
    img, dataPoints = Ex3(img).doEx(robot, startPoint, endPoint, 30, EDGE_COLOR, BACKGROUND_COLOR)
    img.save(OUTPUT_PATH + "roboyEx3.png")


#==============================================================================
#      Draw triangulation
#==============================================================================
    img, nodes, edges = Ex4(img).doEx(dataPoints, EDGE_COLOR, WALL_COLOR, RESTRICTED_AREA_COLOR)
    img.save(OUTPUT_PATH + "roboyEx4.png")


#==============================================================================
#      Draw shortest path
#==============================================================================
    img, shortestPathPointsId = Ex5(img).doEx(nodes, edges, startPoint, endPoint)
    img.save(OUTPUT_PATH + "roboyEx5.png")





#    img = Image.open(OUTPUT_PATH + "roboyEx1.png")
    img = Ex6(img).doEx(nodes, shortestPathPointsId, PATH_COLOR)
    img.save(OUTPUT_PATH + "roboyEx6.png")


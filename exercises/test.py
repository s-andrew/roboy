
from PIL import ImageDraw, Image

from figures.polygon import Polygon
from figures.circle import Circle

def runTest():
    img = Image.new('RGB',(800, 400), "white")
    draw = ImageDraw.Draw(img)


    robot_vertices = ((60, 40), (83, 40), (83, 111), (60, 111))
    robot = Polygon(robot_vertices, center=(71.5, 75.5))
    robot.rotate(0)
    # print("before moveTo\n", robot.vertices)
    robot.moveTo((0, 0))
    # print("after moveTo\n", robot.vertices)
    c = Circle((200, 200), 50, (0, 255, 0))
    c.render(draw)


    robot.render(draw)
    return img
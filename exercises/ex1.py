from PIL import ImageDraw

from figures.polygon import Polygon
from figures.circle import Circle
from figures.rectangle import Rectangle

class Ex1:

    def __init__(self, img):
        self.img = img

    def doEx(self, robotColor, wallColor):
        draw = ImageDraw.Draw(self.img)

        robot = Circle((30,30), 10, color=robotColor)
        robot.rotate(70)
        walls = [
            Rectangle((80, 100), (120, 300)),
            Rectangle((200, 200), (300, 300)),
            Circle((250, 100), 40)
        ]
#        robot.render(draw)
        for wall in walls:
            wall.setColor(wallColor).render(draw)

        return self.img, robot
from PIL import ImageDraw



class Ex2:
    def __init__(self, img):
        self.img = img

    def doEx(self, robotColor, wallColor, restrictedAreaColor, backgroundColor, robot):
        width, height = self.img.size
        draw = ImageDraw.Draw(self.img)
        pixel = self.img.load()

        wallBorder = []
        wallPixels = []
        # robotPixels = []

        for i in range(1, width-1):
            for j in range(1, height-1):
                if pixel[i, j] == wallColor:
                    wallPixels.append((i, j))
                    if  (pixel[i+1, j] == backgroundColor or\
                        pixel[i-1, j] == backgroundColor or\
                        pixel[i, j+1] == backgroundColor or\
                        pixel[i, j-1] == backgroundColor):
                        wallBorder.append((i, j))
                # elif pixel[i, j] == robotColor:
                #     robotPixels.append((i, j))

        imgBorder = []
        imgBorder.extend([(i, 0) for i in range(width)])
        imgBorder.extend([(i, height-1) for i in range(width)])
        imgBorder.extend([(0, i) for i in range(height)])
        imgBorder.extend(([(width-1, i) for i in range(height)]))

        robotPosition = robot.center.tolist()
        # Draw restricted areas
        for xy in wallBorder + imgBorder:
            robot.setColor(restrictedAreaColor).moveTo(xy).render(draw)
        # Re-draw walls
        for x, y in wallPixels:
            pixel[x, y] = wallColor
        # Re-draw robot
        robot.setColor(robotColor).moveTo(robotPosition)

        return self.img


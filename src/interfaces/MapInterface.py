from sdl2 import *


class MapInterface:
    def __init__(self):
        self.name = None
        self.ground = []
        self.points = []
        self.finish = None

    def setName(self, name):
        self.name = name

    def getGround(self):
        return self.ground

    def getPoints(self):
        return self.points

    def getFinish(self):
        return self.finish

    def loadRects(self, what):
        rects = []
        rectsF = open("assets/maps/"+self.name+"."+what)
        for line in rectsF:
            line = line.split(",")
            rect = SDL_Rect(int(line[0]), int(line[1]),
                            int(line[2]), int(line[3]))
            rects.append(rect)
        return rects

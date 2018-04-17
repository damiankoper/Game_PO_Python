from src.components.Singleton import Singleton
from sdl2 import *
from datetime import timedelta
from src.components.Timer import Timer


class GameInfo(metaclass=Singleton):
    def __init__(self):
        self.player = b"Stranger"
        self.gameTimer = Timer()
        self.map = None
        self.points = 0
        self.pointsAll = 0

    def getPlayer(self):
        return self.player

    def setPlayer(self, name):
        self.player = name

    def getMap(self):
        return self.map

    def setMap(self, map):
        self.map = map

    def getPointsAll(self):
        return self.pointsAll

    def getPoints(self):
        return self.points

    def setPointsAll(self, p):
        self.pointsAll = p

    def addPoint(self):
        self.points+=1

    def setState(self, pointsAll):
        self.gameTimer.start()
        self.pointsAll = pointsAll
        self.points = 0

    def getGameTime(self):
        return self.gameTimer.getTicks()/1000.

    def getTimeString(self):
        time = timedelta(miliseconds=self.gameTimer.getTicks())
        return str(time)

    def getTimer(self):
        return self.gameTimer
    
    #TODO readsave, writesave,handlefinish,getsave

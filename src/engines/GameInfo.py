import os
import math
from src.components.Singleton import Singleton
from src.engines.ViewEngine import ViewEngine
from sdl2 import *
from datetime import timedelta
from src.components.Timer import Timer


class GameInfo(metaclass=Singleton):
    def __init__(self):
        self.player = "Stranger"
        self.gameTimer = Timer()
        self.map = None
        self.points = 0
        self.pointsAll = 0
        self.bestScore = None

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
        time = timedelta(milliseconds=self.gameTimer.getTicks())
        return str(time)

    def getTimer(self):
        return self.gameTimer
    
    #TODO readsave, writesave,handlefinish,getsave

    def readSave(self):
        stats = []
        if(os.path.exists("save.XD")):
            save = open("save.XD","r")
            stat = {}
            for line in save:
                linee = line.split(";")
                stat = stat.copy()
                stat["name"] = linee[0]
                stat["score"] = int(linee[1])
                stats.append(stat)
        self.bestScore = stats
        return stats

    def writeSave(self, stats):
        filee = open("save.XD","w")
        for s in self.bestScore:
            filee.write(s["name"]+";"+str(int(s["score"]))+"\n")


    def handleFinish(self):
        self.readSave()
        tt = self.getGameTime()
        s = {
            "name": self.player,
            "score": (self.points * math.exp((-tt+2300)/1000.))
        }
        self.bestScore.append(s)
        self.bestScore.sort(key=lambda s:s["score"],reverse=True)
        self.bestScore = self.bestScore[0:5]
        self.writeSave(self.bestScore)
        ViewEngine().changeView("scoreboard")

    def getSave(self):
        return self.bestScore
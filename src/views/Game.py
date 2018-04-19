from src.interfaces.ViewInterface import ViewInterface
from src.components.Texture import Texture
from src.components.Button import Button
from src.engines.ViewEngine import *
from src.engines.PhysicsEngine import *
from src.engines.GameInfo import *
from src.components.Vector import Vector
from src.components.Square import Square

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class Game(ViewInterface):
    def __init__(self):
        self.name = "game"
        self.time = None
        self.greetings = None
        self.squares = []
        self.border = None
        self.offsetX = 0

    def render(self, gRenderer):
        ts = self.timer.getTicks()
        timeStep = (ts/1000.)
        self.timer.start()

        SDL_SetRenderDrawColor(ViewEngine().getRenderer(), 0, 0, 0, 1)
        ground = GameInfo().getMap().getGround()
        for g in ground:
            tempRect = SDL_Rect(g.x, g.y, g.w, g.h)
            tempRect.x += self.offsetX
            SDL_RenderFillRect(ViewEngine().getRenderer(), tempRect)

        SDL_SetRenderDrawColor(ViewEngine().getRenderer(), 0, 0xff, 0xff, 1)
        points = GameInfo().getMap().getPoints()
        for p in points:
            tempRect = SDL_Rect(p.x, p.y, p.w, p.h)
            tempRect.x += self.offsetX
            SDL_RenderFillRect(ViewEngine().getRenderer(), tempRect)

        SDL_SetRenderDrawColor(ViewEngine().getRenderer(), 255, 0, 0, 1)
        f = GameInfo().getMap().getFinish()
        tempRect = SDL_Rect(f.x, f.y, f.w, f.h)
        tempRect.x += self.offsetX
        SDL_RenderFillRect(ViewEngine().getRenderer(), tempRect)

        for s in self.squares:
            SDL_SetRenderDrawColor(ViewEngine().getRenderer(
            ), s.getColor().r, s.getColor().g, s.getColor().b, 1)
            squareRect = s.getRect()
            tempRect = SDL_Rect(squareRect.x, squareRect.y,
                                squareRect.w, squareRect.h)
            tempRect.x += self.offsetX
            SDL_RenderFillRect(ViewEngine().getRenderer(), tempRect)

        pointsString = str(GameInfo().getPoints())+"/" + \
            str(GameInfo().getPointsAll())
        self.time.loadFromRenderedText(
            "Score: " + pointsString, SDL_Color(255, 255, 255), self.gFontOutline)
        self.time.render(17, 17)
        self.time.loadFromRenderedText(
            "Score: " + pointsString, SDL_Color(0, 0, 0), self.gFont)
        self.time.render(20, 20)

        self.time.loadFromRenderedText(
            "Time: " + GameInfo().getTimeString(), SDL_Color(255, 255, 255), self.gFontOutline)
        self.time.render(17, 42)
        self.time.loadFromRenderedText(
            "Time: " + GameInfo().getTimeString(), SDL_Color(0, 0, 0), self.gFont)
        self.time.render(20, 45)

        if ts == 0 or ViewEngine().isOverlay():
            return

        self.calculateOffset()
        for s in self.squares:
            s.move()
            s.addPosition(timeStep)

        PhysicsEngine().handlePhysics(self.squares, GameInfo().getMap().getGround(),
                                      GameInfo().getMap().getPoints(),
                                      GameInfo().getMap().getFinish(),
                                      ts)

    def handleEvent(self, e):
        if e.type == SDL_KEYUP:
            if e.key.keysym.sym == SDLK_ESCAPE:
                ViewEngine().toggleOverlay()
                if ViewEngine().isOverlay():
                    GameInfo().getTimer().pause()
                else:
                    GameInfo().getTimer().unpause()

    def init(self):
        self.timer = Timer()
        self.offsetX = 50
        self.border = 200
        self.gFont = TTF_OpenFont(FONT, 20)
        self.gFontOutline = TTF_OpenFont(FONT, 20)
        TTF_SetFontOutline(self.gFontOutline, 3)
        color = SDL_Color(0, 0, 0)
        GameInfo().getMap().init()
        ViewEngine().setOverlay("pause")
        GameInfo().setState(len(GameInfo().getMap().getPoints()))
        self.time = Texture(ViewEngine().getRenderer())
        self.points = Texture(ViewEngine().getRenderer())
        self.squares.clear()
        square = Square(Vector(10, 10), Vector(600, 1000), 50, 2, 0.99, 1)
        self.squares.append(square)
        square = Square(Vector(80, 80), Vector(500, 1100), 60, 4, 0.9, 1)
        self.squares.append(square)
        square = Square(Vector(160, 80), Vector(700, 1100), 80, 4, 0.95, 1)
        self.squares.append(square)

    def maxRight(self):
        maxx = None
        for s in self.squares:
            if maxx == None:
                maxx = s
            else:
                r = s.getRect()
                rm = maxx.getRect()
                if r.x+r.w > rm.x+rm.w:
                    maxx = s
        return maxx

    def calculateOffset(self):
        s = self.maxRight().getRect()
        if s.x + self.offsetX < 2*self.border:
            self.offsetX = -(s.x-2*self.border)
        if s.x+s.w+self.offsetX > SCREEN_WIDTH-self.border:
            self.offsetX = -(s.x+s.w-SCREEN_WIDTH+self.border)

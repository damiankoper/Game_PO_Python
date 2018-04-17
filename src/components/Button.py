from src.interfaces.ViewInterface import ViewInterface
from src.components.Texture import Texture
from src.engines.ViewEngine import *
from ctypes import *

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class Button:
    def __init__(self):
        self.borderX = 10
        self.borderY = 0
        self.mPosition = SDL_Rect()
        self.active = False
        self.callback = None

    def setPosition(self, x, y):
        self.mPosition.x = x
        self.mPosition.y = y
        return self

    def setTexture(self, text, size, textColor, bgColor):
        gFont = TTF_OpenFont(FONT, size)
        self.gTexture = Texture(ViewEngine().getRenderer())
        self.gTexture.loadFromRenderedTextShaded(
            text, textColor, gFont, bgColor)
        self.bgColor = bgColor
        return self

    def setBorder(self, x, y):
        self.borderX = x
        self.borderY = y
        return self

    def handleEvent(self, e):
        if e.type == SDL_MOUSEMOTION or e.type == SDL_MOUSEBUTTONDOWN or e.type == SDL_MOUSEBUTTONUP:
            x, y = c_long(), c_long()
            SDL_GetMouseState(x, y)
            x, y = x.value, y.value
            inside = True
            if x < self.mPosition.x-self.borderX:
                inside = False
            elif x > self.mPosition.x+self.gTexture.getWidth()+self.borderX:
                inside = False
            elif y < self.mPosition.y - self.borderY:
                inside - False
            elif y > self.mPosition.y+self.gTexture.getHeight()+self.borderY:
                inside = False
            if inside:
                if e.type == SDL_MOUSEBUTTONDOWN:
                    self.active = True
                elif e.type == SDL_MOUSEBUTTONUP:
                    if self.active:
                        self.callback()
                    self.active = False
            else:
                    self.active = False
        return self

    def render(self):
        SDL_SetRenderDrawColor(ViewEngine().getRenderer(
        ), self.bgColor.r, self.bgColor.g, self.bgColor.b, self.bgColor.a)
        border = SDL_Rect(self.mPosition.x - self.borderX, self.mPosition.y - self.borderY,
                          self.gTexture.getWidth() + 2 * self.borderX, self.gTexture.getHeight() + 2 * self.borderY)
        SDL_RenderFillRect(ViewEngine().getRenderer(), border)
        self.gTexture.render(self.mPosition.x, self.mPosition.y)

    def onClick(self, callback):
        self.callback = callback
        return self

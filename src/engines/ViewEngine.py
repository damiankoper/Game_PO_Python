from src.components.Singleton import Singleton
from sdl2 import *


class ViewEngine(metaclass=Singleton):
    def __init__(self):
        self.fullscreen = False
        self.quit = False
        self.renderOverlay = False
        self.interfaces = {}
        self.interface = None
        self.overlay = None

    def exit(self):
        self.quit = True

    def toggleOverlay(self):
        self.renderOverlay = not self.renderOverlay

    def isOverlay(self):
        return self.renderOverlay

    def addView(self, i):
        self.interfaces[i.name] = i

    def removeView(self, name):
        del self.interfaces[name]

    def changeView(self, name):
        self.interface = self.interfaces[name]

    def setOverlay(self, name):
        self.overlay = self.interfaces[name]
        self.overlay.init()

    def updateView(self):
        self.interface.init()

    def assignRenderer(self, gRenderer):
        self.gRenderer = gRenderer
    
    def assignWindow(self, gWindow):
        self.gWindow = gWindow

    def getRenderer(self):
        return self.gRenderer

    def getWindow(self):
        return self.gWindow

    def renderView(self):
        SDL_SetRenderDrawColor(self.gRenderer, 0xFF, 0xFF, 0xFF, 0xFF)
        SDL_RenderClear(self.gRenderer)

        self.interface.render(self.gRenderer)

        if self.renderOverlay:
            self.overlay.render(self.gRenderer)

        SDL_RenderPresent(self.gRenderer)

    def handleEvent(self, e):
        self.interface.handleEvent(e)

        if self.renderOverlay:
            self.overlay.handleEvent(e)

    def toggleFullscreen(self):
        flags = SDL_WINDOW_FULLSCREEN if self.fullscreen else 0
        self.fullscreen = not self.fullscreen
        SDL_SetWindowFullscreen(self.gWindow, flags)


    

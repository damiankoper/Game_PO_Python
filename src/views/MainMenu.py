from src.interfaces.ViewInterface import ViewInterface
from src.components.Texture import Texture
from src.components.Button import Button
from src.engines.ViewEngine import *
from src.engines.GameInfo import *

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class MainMenu(ViewInterface):
    def __init__(self):
        self.name = "mainMenu"
        self.buttons = []
        self.title = None
        self.greetings = None

    def render(self, gRenderer):
        self.title.render(20, 20)
        self.greetings.render(20,110)
        for b in self.buttons:
            b.render()

    def handleEvent(self, e):
        for b in self.buttons:
            b.handleEvent(e)

    def init(self):
        self.buttons.clear()

        gFont = TTF_OpenFont(FONT, 80)
        TTF_SetFontStyle(gFont, TTF_STYLE_BOLD)
        color = SDL_Color(0, 0, 0)

        button = Button()
        button.setTexture("Settings", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 140)
        button.onClick(lambda: ViewEngine().changeView("settings"))
        self.buttons.append(button)

        button = Button()
        button.setTexture("Exit", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 70)
        button.onClick(lambda: ViewEngine().exit())
        self.buttons.append(button)

        button = Button()
        button.setTexture("Scoreboard", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 210)
        button.onClick(lambda: ViewEngine().changeView("scoreboard"))
        self.buttons.append(button)

        button = Button()
        button.setTexture("New Game", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 350)
        button.onClick(lambda: ViewEngine().changeView("game"))
        self.buttons.append(button)

        button = Button()
        button.setTexture("Set nickname", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 280)
        button.onClick(lambda: ViewEngine().changeView("nickname"))
        self.buttons.append(button)

        self.title = Texture(ViewEngine().getRenderer())
        self.title.loadFromRenderedText("Main Menu", color, gFont)

        gFont = TTF_OpenFont(FONT, 40)
        self.greetings = Texture(ViewEngine().getRenderer())
        self.greetings.loadFromRenderedText("Hello " + GameInfo().getPlayer(), color, gFont)


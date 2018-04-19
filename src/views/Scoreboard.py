from src.interfaces.ViewInterface import ViewInterface
from src.components.Texture import Texture
from src.components.Button import Button
from src.engines.ViewEngine import *
from src.engines.GameInfo import *

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class Scoreboard(ViewInterface):
    def __init__(self):
        self.name = "scoreboard"
        self.buttons = []
        self.title = None
        self.score = []

    def render(self, gRenderer):
        self.title.render(20, 20)
        for b in self.buttons:
            b.render()

        for i, val in enumerate(self.score):
            val.render(60, 140+i*60)

    def handleEvent(self, e):
        for b in self.buttons:
            b.handleEvent(e)

    def init(self):
        self.buttons.clear()

        gFont = TTF_OpenFont(FONT, 80)
        TTF_SetFontStyle(gFont, TTF_STYLE_BOLD)
        color = SDL_Color(0, 0, 0)

        button = Button()
        button.setTexture("Main menu", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 70)
        button.onClick(lambda: ViewEngine().changeView("mainMenu"))
        self.buttons.append(button)

        self.title = Texture(ViewEngine().getRenderer())
        self.title.loadFromRenderedText("Set nickname", color, gFont)

        gFont = TTF_OpenFont(FONT, 40)
        self.score.clear()
        s = GameInfo().readSave()
        for i, val in enumerate(s):
            texture = Texture(ViewEngine().getRenderer())
            texture.loadFromRenderedText(
                str(i+1)+". " + val["name"] + " - " + str(val["score"]), color, gFont)
            self.score.append(texture)

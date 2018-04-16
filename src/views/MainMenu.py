from src.interfaces.ViewInterface import ViewInterface
from src.components.Texture import Texture
from src.engines.ViewEngine import *

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class MainMenu(ViewInterface):
    def __init__(self):
        self.name = "mainMenu"
        self.buttons = []
        self.title = None

        self.init()

    def render(self, gRenderer):
        self.title.render(20, 20)

    def handleEvent(self, e):
        pass

    def init(self):
        self.buttons.clear()

        gFont = TTF_OpenFont(FONT, 80)
        TTF_SetFontStyle(gFont, TTF_STYLE_BOLD)
        color = SDL_Color(0, 0, 0)

        self.title = Texture(ViewEngine().getRenderer())
        self.title.loadFromRenderedText(b"Main Menu", color, gFont)

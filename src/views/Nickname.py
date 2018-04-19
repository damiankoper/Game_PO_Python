from src.interfaces.ViewInterface import ViewInterface
from src.components.Texture import Texture
from src.components.Button import Button
from src.engines.ViewEngine import *
from src.engines.GameInfo import *

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class Nickname(ViewInterface):
    def __init__(self):
        self.name = "nickname"
        self.buttons = []
        self.title = None
        self.nickname = None

    def render(self, gRenderer):
        self.title.render(20, 20)
        self.nickname.render((SCREEN_WIDTH - self.nickname.getWidth()) / 2, (SCREEN_HEIGHT - self.nickname.getHeight()) / 2)
        for b in self.buttons:
            b.render()

    def handleEvent(self, e):
        for b in self.buttons:
            b.handleEvent(e)
        if e.type == SDL_KEYDOWN:
            if e.key.keysym.sym == SDLK_BACKSPACE and len(GameInfo().getPlayer())>0:
                player = GameInfo().getPlayer()
                player = player[:-1]
                if len(player) == 0:
                    player = " "
                GameInfo().setPlayer(player)
            ViewEngine().updateView()
        elif e.type == SDL_TEXTINPUT:
            player = GameInfo().getPlayer()
            if len(player) == 1 and player[0] == " ":
                player = ""
            GameInfo().setPlayer(player + e.text.text.decode('utf-8'))
            ViewEngine().updateView()

    def init(self):
        self.buttons.clear()

        gFont=TTF_OpenFont(FONT, 80)
        TTF_SetFontStyle(gFont, TTF_STYLE_BOLD)
        color=SDL_Color(0, 0, 0)

        button=Button()
        button.setTexture("Main menu", 40, SDL_Color(
            255, 255, 255), SDL_Color(0, 0, 0))
        button.setPosition(30, SCREEN_HEIGHT - 70)
        button.onClick(lambda: ViewEngine().changeView("mainMenu"))
        self.buttons.append(button)

        self.title = Texture(ViewEngine().getRenderer())
        self.title.loadFromRenderedText("Set nickname", color, gFont)

        gFont = TTF_OpenFont(FONT, 40)
        self.nickname = Texture(ViewEngine().getRenderer())
        self.nickname.loadFromRenderedText(GameInfo().getPlayer(), color, gFont)

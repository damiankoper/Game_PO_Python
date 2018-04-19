import os
import sys

os.environ["PYSDL2_DLL_PATH"] = os.path.dirname(
    os.path.abspath(__file__)) + "/SDL2/bin"

from sdl2 import *
from sdl2.sdlttf import *

from src.config import *
from src.engines.ViewEngine import *
from src.engines.GameInfo import *
from src.maps.Level import Level
from src.views import MainMenu, Settings, Nickname, Game, Scoreboard, Pause


def init():
    SDL_Init(SDL_INIT_VIDEO)
    SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, b"1")
    gWindow = SDL_CreateWindow(b"3 AS 1", SDL_WINDOWPOS_UNDEFINED,
                               SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN)
    gRenderer = SDL_CreateRenderer(gWindow, -1, SDL_RENDERER_ACCELERATED)
    SDL_SetRenderDrawColor(gRenderer, 0xFF, 0xFF, 0xFF, 0xFF)
    TTF_Init()

    ViewEngine().assignRenderer(gRenderer)
    ViewEngine().assignWindow(gWindow)


def loadInterfaces():
    mainMenu = MainMenu.MainMenu()
    settings = Settings.Settings()
    ViewEngine().addView(mainMenu)
    ViewEngine().addView(settings)
    ViewEngine().addView(Nickname.Nickname())
    ViewEngine().addView(Scoreboard.Scoreboard())
    ViewEngine().addView(Game.Game())
    ViewEngine().addView(Pause.Pause())

    GameInfo().setMap(Level("level1"))


init()
loadInterfaces()

ViewEngine().changeView("game")
e = SDL_Event()
while not ViewEngine().quit:
    while SDL_PollEvent(e) != 0:
        if e.type == SDL_QUIT:
            ViewEngine().exit()
        else:
            ViewEngine().handleEvent(e)
    ViewEngine().renderView()

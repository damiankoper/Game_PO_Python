import sys
import os
os.environ["PYSDL2_DLL_PATH"] = os.path.dirname(
    os.path.abspath(__file__)) + "/SDL2/bin"
from src.config import *
from sdl2 import *
from sdl2.sdlttf import *
from src.views.MainMenu import *
from src.engines.ViewEngine import *


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
    mainMenu = MainMenu()
    ViewEngine().addView(mainMenu)


init()
loadInterfaces()

ViewEngine().changeView("mainMenu")
e = SDL_Event()
while not ViewEngine().quit:
    while SDL_PollEvent(e) != 0:
        if e.type == SDL_QUIT:
            ViewEngine().exit()
        else:
            ViewEngine().handleEvent(e)
    ViewEngine().renderView()


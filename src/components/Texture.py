from sdl2 import *
from sdl2.sdlttf import *


class Texture:
    def __init__(self, renderer):
        self.gRenderer = renderer
        self.mTexture = None
        self.mWidth = 0
        self.mHeight = 0

    def loadFromRenderedText(self, textureText, textColor, gFont):
        self.free()
        textSurface = TTF_RenderText_Solid(
            gFont, textureText, textColor)

        self.mTexture = SDL_CreateTextureFromSurface(
            self.gRenderer, textSurface)

        self.mWidth = textSurface.contents.w
        self.mHeight = textSurface.contents.h

        SDL_FreeSurface(textSurface)

        return (self.mTexture is not None)

    def loadFromRenderedTextShaded(self, textureText, textColor, gFont, bgColor):
        self.free()
        textSurface = TTF_RenderText_Shaded(
            gFont, textureText, textColor, bgColor)

        self.mTexture = SDL_CreateTextureFromSurface(
            self.gRenderer, textSurface)

        self.mWidth = textSurface.w
        self.mHeight = textSurface.h

        SDL_FreeSurface(textSurface)

        return (self.mTexture is not None)

    def free(self):
        if self.mTexture is not None:
            SDL_DestroyTexture(self.mTexture)
            self.mTexture = None
            self.mWidth = 0
            self.mHeight = 0

    def setColor(self, r, g, b):
        SDL_SetTextureColorMod(self.mTexture, r, g, b)

    def setBlendMode(self, blending):
        SDL_SetTextureBlendMode(self.mTexture, blending)

    def setAlpha(self, a):
        SDL_SetTextureAlphaMod(self.mTexture, a)

    def render(self, x, y, clip=None, angle=0.0, center=None, flip=SDL_FLIP_NONE):
        renderQuad = SDL_Rect(x, y, self.mWidth, self.mHeight)

        if clip is not None:
            renderQuad.w = clip.w
            renderQuad.h = clip.h

        SDL_RenderCopyEx(self.gRenderer, self.mTexture, clip, renderQuad, angle, center, flip)

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight
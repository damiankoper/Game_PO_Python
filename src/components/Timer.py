from sdl2 import *

class Timer():
    def __init__(self):
        self.mStartTicks = 0
        self.mPausedTicks = 0
        self.mPaused = False
        self.mStarted = False

    def start(self):
        self.mStarted = True
        self.mPaused = False
        self.mStartTicks = SDL_GetTicks()
        self.mPausedTicks = 0

    def stop(self):
        self.mStarted = False
        self.mPaused = False
        self.mStartTicks = 0
        self.mPausedTicks = 0

    def pause(self):
        if self.mStarted and not self.mPaused:
            self.mPaused = True
            self.mPausedTicks = SDL_GetTicks() - self.mStartTicks
            self.mStartTicks = 0

    def unpause(self):
        if self.mStarted and self.mPaused:
            self.mPaused = False
            self.mStartTicks = SDL_GetTicks() - self.mPausedTicks
            self.mPausedTicks = 0

    def getTicks(self):
        if self.mStarted:
            if self.mPaused:
                return self.mPausedTicks
            else:
                return SDL_GetTicks() - self.mStartTicks
        return 0

    def isStarted(self):
        return self.mStarted

    def isPaused(self):
        return (self.mPaused and self.mStarted)
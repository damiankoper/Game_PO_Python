from src.components.Vector import Vector
import random
from sdl2 import *


class Square:
    def __init__(self, position, speed, size, mass, breakMtp, accTime):
        self.position = position
        self.speed = speed
        self.breakMtp = breakMtp
        self.mass = mass
        self.accTime = accTime
        self.size = size
        self.velocity = Vector(0.0, 0.0)
        self.jump = False
        self.bgColor = SDL_Color(random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))

    def getRect(self):
        return SDL_Rect(int(self.position.x), int(self.position.y), int(self.size), int(self.size))

    def addPosition(self, timeStep):
        self.position += self.velocity * timeStep

    def move(self):
        move = False
        keystate = SDL_GetKeyboardState(None)
        if keystate[SDL_SCANCODE_LEFT]:
            self.velocity.x = -self.speed.x
            move = True
        if keystate[SDL_SCANCODE_RIGHT]:
            self.velocity.x = self.speed.x
            move = True
        if keystate[SDL_SCANCODE_SPACE] and not self.jump:
            self.velocity.y = -self.speed.y
            self.jump = True

        if not move:
            self.velocity.x *= self.breakMtp

    def processCollision(self, coll):
        self.position += coll
        if self.velocity.y<0 and coll.y<0:
            coll.y = 0
        elif self.velocity.y >0 and coll.y >0:
            coll.y = 0
        if coll.y < 0:
            self.jump = False
        self.velocity.resetNonZero(coll)

    def getMass(self):
        return self.mass

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity

    def getColor(self):
        return self.bgColor
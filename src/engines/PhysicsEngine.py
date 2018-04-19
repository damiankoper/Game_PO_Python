from src.engines.ViewEngine import *
from src.engines.GameInfo import *
from src.components.Vector import Vector
from src.components.Square import Square
from src.components.Singleton import Singleton

from sdl2 import *
from sdl2.sdlttf import *
from src.config import *


class PhysicsEngine(metaclass=Singleton):
    def __init__(self):
        self.gravityForce = Vector(0, 1)


    def handlePhysics(self, squares, collisionObjects, pointsObjects, finish, timeStep):
        for s in squares:
            s.velocity += self.gravityForce * s.getMass() * timeStep

            r = s.getRect()
            coll = Vector(0.0, 0.0)

            for sc in squares:
                if s == sc:
                    continue
                rc = sc.getRect()
                coll += self.collision(r, rc)

            s.processCollision(coll)
            coll = Vector(0.0, 0.0)
            r = s.getRect()
            for c in collisionObjects:
                coll += self.collision(r, c)
            s.processCollision(coll)
            for i, p in enumerate(pointsObjects):
                if self.collision(r, p) != 0:
                    GameInfo().addPoint()
                    del pointsObjects[i]
            if self.collision(r, finish) != 0:
                GameInfo().handleFinish() 

    def collision(self, A, B):
        leftA = A.x
        rightA = A.x + A.w
        topA = A.y
        bottomA = A.y+A.h

        leftB = B.x
        rightB = B.x + B.w
        topB = B.y
        bottomB = B.y+B.h

        if bottomA <= topB:
            return Vector(0, 0)
        if topA >= bottomB:
            return Vector(0, 0)
        if rightA <= leftB:
            return Vector(0, 0)
        if leftA >= rightB:
            return Vector(0, 0)

        overlap = []
        overlap.append(Vector(0, topB - bottomA))
        overlap.append(Vector(0, bottomB - topA))
        overlap.append(Vector(leftB - rightA, 0))
        overlap.append(Vector(rightB - leftA, 0))
        return min(overlap)

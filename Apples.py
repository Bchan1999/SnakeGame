from random import randrange
import pygame


class Apples:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spawnApple(self, win, noX, noY):
        self.x = randrange(20)
        self.y = randrange(20)
        if self.x == noX or self.y == noY:
            return 1
        else:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 1, 1))
            return 2

    def drawApple(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 1, 1))

    def returnLoc(self):
        return self.x, self.y

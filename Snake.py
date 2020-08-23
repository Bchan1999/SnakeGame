import pygame
from random import randrange


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawSnake(self, win, x, y):
        a = randrange(255)
        b = randrange(255)
        c = randrange(255)
        pygame.draw.rect(win, (a, b, c), (x, y, 1, 1))

    def returnX(self):
        return self.x

    def returnY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

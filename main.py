import pygame

from SnakeGame import Snake
from SnakeGame import Apples

pygame.init()

pygame.display.set_caption('Snake')

scaling = 50
win = pygame.display.set_mode((20 * scaling, 20 * scaling))
screen = pygame.Surface((20, 20))

# variable
x = 5
y = 5
vel = 1
direct = 2
i = 1
z = 0
a = 1
firstApp = 1
firstSnake = 0

snakeList = []
while firstSnake < 5:
    snake1 = Snake.Snake(x, y)
    snakeList.append(snake1)
    firstSnake = firstSnake + 1

Apple = Apples.Apples(0, 0)

game_over = False
while not game_over:
    pygame.time.delay(60)

    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    x2 = x
    y2 = y

    if keys[pygame.K_LEFT] and direct != 2:
        direct = 1
    if keys[pygame.K_RIGHT] and direct != 1:
        direct = 2
    if keys[pygame.K_UP] and direct != 4:
        direct = 3
    if keys[pygame.K_DOWN] and direct != 3:
        direct = 4

    if direct == 1:
        x -= vel
        if x == -1:
            x = 19
    elif direct == 2:
        x += vel
        if x == 20:
            x = 0
    elif direct == 3:
        y -= vel
        if y == -1:
            y = 19
    elif direct == 4:
        y += vel
        if y == 20:
            y = 0

    screen.fill((0, 0, 0))

    appLoc = Apple.returnLoc()

    if firstApp == 1:
        Apple.spawnApple(screen, -50, -50)
        firstApp = 0

    Apple.drawApple(screen)

    if appLoc == (x, y):
        lastIndex = len(snakeList) - 1
        lastSnake = snakeList[lastIndex]
        newX = lastSnake.returnX()
        newY = lastSnake.returnY()
        snake2 = Snake.Snake(newX, newY)
        snakeList.append(snake2)
        while len(snakeList) > z:
            snakeBod = snakeList[z]
            noX = snakeBod.returnX()
            noY = snakeBod.returnY()
            z = z + 1
            okay = Apple.spawnApple(screen, noX, noY)
            if okay == 2:
                break

    FirstSnake = snakeList[0]
    FirstSnake.setX(x)
    FirstSnake.setY(y)
    FirstSnake.drawSnake(screen, x, y)
    headLocX = FirstSnake.returnX()
    headLocY = FirstSnake.returnY()

    i = 1
    while len(snakeList) > i:
        snakeBod = snakeList[i]
        x3 = snakeBod.returnX()
        y3 = snakeBod.returnY()
        snakeBod.setX(x2)
        snakeBod.setY(y2)
        snakeBod.drawSnake(screen, x2, y2)
        x2 = x3
        y2 = y3
        if headLocX == x2 and headLocY == y2:
            game_over = True
        i = i + 1

    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    pygame.display.update()

pygame.quit()

import pygame
import random

pygame.init()

# CONSTANTS

# Window Stuff
WIDTH = 400
HEIGHT = 400
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# COLORS
SNAKE_COLOR = (0, 200, 0)
BG_COLOR = (255, 255, 255)
APPLE_COLOR = (200, 0, 0)

# Snake Stuff
MOVE_SPEED = 5

SNAKE_DIMENSIONS = 10

pygame.display.set_caption("Snake")


def gameOver(x, y):
    if (
        x + SNAKE_DIMENSIONS >= WIDTH
        or x <= 0
        or y + SNAKE_DIMENSIONS >= HEIGHT
        or y <= 0
    ):
        return True


def drawApple(x, y):
    pygame.draw.rect(
        WIN, APPLE_COLOR, [x, y,
                           SNAKE_DIMENSIONS, SNAKE_DIMENSIONS]
    )


def main():
    # game is running
    run = True

    # endscreen shown
    endScreen = False

    # the snakes coords
    snakeX = WIDTH / 2
    snakeY = HEIGHT / 2

    # the snakes directions
    xDirection = MOVE_SPEED
    yDirection = 0

    # making sure only one apple is rendered at a time
    canDraw = True

    appleX = random.randint(0, WIDTH)
    appleY = random.randint(0, HEIGHT)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xDirection = -MOVE_SPEED
                    yDirection = 0
                elif event.key == pygame.K_RIGHT:
                    xDirection = MOVE_SPEED
                    yDirection = 0
                elif event.key == pygame.K_UP:
                    xDirection = 0
                    yDirection = -MOVE_SPEED
                elif event.key == pygame.K_DOWN:
                    xDirection = 0
                    yDirection = MOVE_SPEED

        snakeX += xDirection
        snakeY += yDirection

        # generate new apple position if the previous one was eaten
        if canDraw:
            appleX = random.randint(0, WIDTH)
            appleY = random.randint(0, HEIGHT)

        # check if the snake ate the apple
        if snakeX == appleX and snakeY == appleY:
            canDraw = False

        if gameOver(snakeX, snakeY):
            run = False

        WIN.fill(BG_COLOR)
        # draw the apple
        if canDraw:
            drawApple(appleX, appleY)
        pygame.draw.rect(
            WIN, SNAKE_COLOR, [snakeX, snakeY,
                               SNAKE_DIMENSIONS, SNAKE_DIMENSIONS]
        )

        pygame.display.update()

        CLOCK.tick(FPS)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()

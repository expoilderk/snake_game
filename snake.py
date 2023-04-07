import pygame
import utils
import macros
from pygame.locals import *

# Inits -----
pygame.init()

# Screen -----
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

# Snake -----
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# Apple -----
apple_pos = utils.on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

# Direction -----
my_direction = macros.LEFT

# FPS -----
clock = pygame.time.Clock()
fps = 15

# Game Score -----
score_level = 100
game_score = 0

# Text -----
white = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 15)

# Principal Loop -----
while True:

    # Game Score and FPS -----
    text = font.render('GAME SCORE: ' + str(game_score), True, white)
    textRect = text.get_rect()

    if game_score == score_level:
        fps += 5
        score_level += 100
    clock.tick(fps)

    # Events -----
    for event in pygame.event.get():
        # Quit -----
        if event.type == QUIT:
            pygame.quit()

        # Keywords -----
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = macros.UP
            if event.key == K_DOWN:
                my_direction = macros.DOWN
            if event.key == K_RIGHT:
                my_direction = macros.RIGHT
            if event.key == K_LEFT:
                my_direction = macros.LEFT

    # Collision -----
    if utils.collision(snake[0], apple_pos):
        game_score += 10
        apple_pos = utils.on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Snake Move -----
    if my_direction == macros.UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == macros.DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == macros.RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == macros.LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # Screen Render -----
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    screen.blit(text, textRect)

    # Screen Update -----
    pygame.display.update()

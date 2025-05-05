import pygame
from pygame import Rect

from src.snake_components import SnakeBodySegment

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

snake_speed = 5

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# snake = Rect(left=screen.get_width() / 2, top =  screen.get_height() / 2, width=1, height=1 )

snake = Rect(screen.get_width() / 2, screen.get_height() / 2, 20, 20)
snake_body = Rect(snake.x - 20, snake.y, 20, 20)
snake_segment = SnakeBodySegment(screen=screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    snake_segment.move_segment()
    pygame.draw.rect(screen, "green", snake_segment.current_segment)

    # pygame.draw.rect(screen, "green", snake)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_segment.current_direction = 'up'
    if keys[pygame.K_s]:
        snake_segment.current_direction = 'down'
    if keys[pygame.K_a]:
        snake_segment.current_direction = 'left'
    if keys[pygame.K_d]:
        snake_segment.current_direction = 'right'


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
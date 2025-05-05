import pygame
from pygame import Rect

from src.snake_components import SnakeBodySegment

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

snake_speed = 5
direction = 'right'

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# snake = Rect(left=screen.get_width() / 2, top =  screen.get_height() / 2, width=1, height=1 )

snake_head = SnakeBodySegment(screen=screen)
snake_body = SnakeBodySegment(screen=screen, next_segment=snake_head)
snake_head.previous_segment = snake_body


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    snake_head.move_segment()

    snake_part = snake_head

    while snake_part:
        pygame.draw.rect(screen, "green", snake_part.current_segment)
        snake_part = snake_part.previous_segment

    # pygame.draw.rect(screen, "green", snake)

    snake_head.update_direction(direction)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = 'up'
    if keys[pygame.K_s]:
        direction = 'down'
    if keys[pygame.K_a]:
        direction = 'left'
    if keys[pygame.K_d]:
        direction = 'right'

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
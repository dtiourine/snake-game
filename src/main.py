import pygame
from jedi.debug import speed
from pygame import Rect

from src.snake_components import Snake, Food
from src.utils import calculate_new_head_position, draw_snake

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

# snake_speed = 1
direction = 'right'

start_x = screen.get_width() / 2
start_y = screen.get_height() / 2

snake_positions = [(start_x, start_y)]

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# snake = Rect(left=screen.get_width() / 2, top =  screen.get_height() / 2, width=1, height=1 )

# snake = Snake(screen=screen, snake_speed=snake_speed)

snake_speed = 4
food = Food(screen=screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    current_x, current_y = snake_positions[0]

    new_head = calculate_new_head_position(current_x, current_y, direction=direction, snake_speed=snake_speed)

    snake_positions.insert(0, new_head)

    new_x, new_y = new_head
    if pygame.Rect.colliderect(Rect(new_x, new_y, 20, 20), food.item):
        food.move()
        growing = True
    else:
        growing = False

    if not growing:
        snake_positions.pop()

    draw_snake(screen=screen, positions=snake_positions)
    pygame.draw.rect(screen, "red", food.item)

    # pygame.draw.rect(screen, "red",.item)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        direction = 'up'
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        direction = 'down'
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        direction = 'left'
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        direction = 'right'
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
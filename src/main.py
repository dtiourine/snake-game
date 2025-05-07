import pygame
from jedi.debug import speed
from pygame import Rect

from src.snake_components import Snake, Food
from src.utils import calculate_new_head_position, draw_snake

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

direction = 'right'

start_x = screen.get_width() / 2
start_y = screen.get_height() / 2
snake_positions = [(start_x, start_y)]
score = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# snake = Rect(left=screen.get_width() / 2, top =  screen.get_height() / 2, width=1, height=1 )

# snake = Snake(screen=screen, snake_speed=snake_speed)

snake_speed = 4
food = Food(screen=screen)

while running:
    font = pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    current_x, current_y = snake_positions[0]

    new_head = calculate_new_head_position(current_x, current_y, direction=direction, snake_speed=snake_speed)

    snake_positions.insert(0, new_head)

    new_x, new_y = new_head

    # if len(snake_positions) > 2:
    #     for x, y in snake_positions[2:]:
    #         if pygame.Rect.colliderect(Rect(new_x, new_y, 20, 20), Rect(x, y, 20, 20)):
    #             print("Snake collided with itself!")
    #             pygame.quit()

    if new_y > screen.get_height() or new_y < 0 or new_x > screen.get_width() or new_x < 0:
        print("SNAKE WENT OUT OF SCREEN")
        pygame.quit()

    if pygame.Rect.colliderect(Rect(new_x, new_y, 20, 20), food.item):
        food.move()
        growing = True
        score += 1

        if snake_speed < 6:
            snake_speed += 0.5
    else:
        growing = False

    if not growing:
        snake_positions.pop()
    else:
        snake_positions.insert(0, new_head)


    draw_snake(screen=screen, positions=snake_positions)
    pygame.draw.rect(screen, "red", food.item)

    # pygame.draw.rect(screen, "red",.item)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if direction != 'down':
            direction = 'up'
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if direction != 'up':
            direction = 'down'
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if direction != 'right':
            direction = 'left'
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if direction != 'left':
            direction = 'right'

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
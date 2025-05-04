import pygame
from pygame import Rect

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0


# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# snake = Rect(left=screen.get_width() / 2, top =  screen.get_height() / 2, width=1, height=1 )

snake = Rect(screen.get_width() / 2, screen.get_height() / 2, 20, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    pygame.draw.rect(screen,"green", snake)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
import pygame

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake Game")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.display.flip()

pygame.quit()

# def main():
#     init()
#
# if __name__ == '__main__':
#     main()
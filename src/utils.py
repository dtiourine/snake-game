import pygame
import time
import sys
from pygame import Rect

def calculate_new_head_position(current_x: float, current_y: float, direction: str, snake_speed: int):
    if direction == 'right':
        new_x, new_y = current_x + snake_speed, current_y
    elif direction == 'left':
        new_x, new_y = current_x - snake_speed, current_y
    elif direction == 'up':
        new_x, new_y = current_x, current_y - snake_speed
    elif direction == 'down':
        new_x, new_y = current_x, current_y + snake_speed
    else:
        raise ValueError(f'Invalid direction: {direction}')

    return new_x, new_y

def draw_snake(screen, positions: list[tuple[float, float]], color: str = "green") -> None:
    for x, y in positions:
        segment = Rect(x, y, 20, 20)
        pygame.draw.rect(screen, color, segment)

def game_over_screen(screen, end_reason: str, score: int) -> None:
    font = pygame.font.SysFont('Arial', 60)
    game_over_text = font.render("Game Over", True, 'red')
    end_reason_text = font.render(end_reason, True, 'green')
    score_text = font.render(f"Your score was {score}", True, 'blue')

    screen.fill((0, 0, 0))

    screen.blit(game_over_text, (0,  screen.get_height() / 8 * 2))
    screen.blit(end_reason_text, (0, screen.get_height() / 8 * 3))
    screen.blit(score_text, (0, screen.get_height() / 8 * 4))

    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    sys.exit()






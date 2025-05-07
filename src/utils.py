import pygame
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

    return (new_x, new_y)

def draw_snake(screen, positions: list[tuple[float, float]], color: str = "green") -> None:
    for x, y in positions:
        segment = Rect(x, y, 20, 20)
        pygame.draw.rect(screen, color, segment)



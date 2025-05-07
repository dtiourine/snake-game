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

def grow_tail(positions: list[tuple[float, float]], direction: str):
    """Make the snake longer if it eats food"""
    tail_pos_x, tail_pos_y = positions[-1]
    if direction == 'right':
        # tail_pos_x1, tail_pos_y1 = tail_pos_x + 20, tail_pos_y
        tail_pos_x2, tail_pos_y2 = tail_pos_x + 40, tail_pos_y
    elif direction == 'left':
        # tail_pos_x1, tail_pos_y1 = tail_pos_x - 20, tail_pos_y
        tail_pos_x2, tail_pos_y2 = tail_pos_x - 40, tail_pos_y
    elif direction == 'up':
        # tail_pos_x1, tail_pos_y1 = tail_pos_x, tail_pos_y - 20
        tail_pos_x2, tail_pos_y2 = tail_pos_x, tail_pos_y - 40
    elif direction == 'down':
        # tail_pos_x1, tail_pos_y1 = tail_pos_x, tail_pos_y + 20
        tail_pos_x2, tail_pos_y2 = tail_pos_x, tail_pos_y + 40
    else:
        raise ValueError(f'Invalid direction: {direction}')

    # positions.append((tail_pos_x1, tail_pos_y2))
    positions.append((tail_pos_x2, tail_pos_y2))

    return positions

def draw_snake(screen, positions: list[tuple[float, float]], color: str = "green") -> None:
    for x, y in positions:
        segment = Rect(x, y, 20, 20)
        pygame.draw.rect(screen, color, segment)



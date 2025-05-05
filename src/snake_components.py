import pygame
from pygame import Rect

class Snake:
    pass

class SnakeHead:
    pass


class SnakeBodySegment:
    def __init__(self, screen, next_segment=None, snake_speed: int = 5):
        if next_segment:
            self.current_direction = next_segment.get_direction()
            self.current_segment = Rect(next_segment.x - 20, next_segment.y, 20, 20)
        else:
            self.current_direction = 'right'
            self.current_segment = Rect(screen.get_width() / 2, screen.get_height() / 2, 20, 20)

        pygame.draw.rect(screen, "green", self.current_segment)
        self.next_segment = next_segment
        self.snake_speed = snake_speed

    def move_segment(self):
        if self.current_direction == 'right':
            self.current_segment = pygame.Rect.move(self.current_segment, self.snake_speed, 0)
        elif self.current_direction == 'left':
            self.current_segment = pygame.Rect.move(self.current_segment, -self.snake_speed, 0)
        elif self.current_direction == 'up':
            self.current_segment = pygame.Rect.move(self.current_segment, 0, -self.snake_speed)
        elif self.current_direction == 'down':
            self.current_segment = pygame.Rect.move(self.current_segment, 0, self.snake_speed)
        else:
            raise ValueError(f'Invalid direction: {self.current_direction}')

    def get_direction(self):
        raise NotImplementedError("This function hasn't been implemented yet")



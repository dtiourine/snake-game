import pygame
import math
import random
from pygame import Rect

class Snake:
    pass

class SnakeHead:
    pass

class Food:
    def __init__(self, screen):
        random_x = math.floor(random.uniform(0, (screen.get_width() + 1)))
        random_y = math.floor(random.uniform(0, (screen.get_height() + 1)))
        self.item = Rect(random_x, random_y, 20, 20)

class SnakeBodySegment:
    def __init__(self, screen, next_segment=None, previous_segment=None, snake_speed: int = 5):
        if next_segment:
            self.current_direction = next_segment.get_direction()
            self.current_segment = Rect(next_segment.current_segment.x - 20, next_segment.current_segment.y, 20, 20)
        else:
            self.current_direction = 'right'
            self.current_segment = Rect(screen.get_width() / 2, screen.get_height() / 2, 20, 20)

        # pygame.draw.rect(screen, "green", self.current_segment)
        self.next_segment = next_segment
        self.previous_segment = previous_segment
        self.snake_speed = snake_speed
        self.next_segment_turning_point = None
        self.next_segment_turning_point_direction = None

    def move_segment(self):
        """Moves the segment according to the current direction """
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

        # If the coordinates of the current segment match the coordinates of the turning point of the next segment
        # then turn the current segment
        if (self.current_segment.x, self.current_segment.y) == self.next_segment_turning_point:
            self.update_direction(direction=self.next_segment_turning_point_direction)

        if self.previous_segment:
            self.previous_segment.move_segment()

    def update_direction(self, direction: str):
        """Updates direction of segment to match direction of argument"""

        # Don't update direction if trying to move in the opposite direction of where currently moving
        if ((direction == 'right' and self.current_direction == 'left')
            or
            (direction == 'left' and self.current_direction == 'right')
            or
            (direction == 'up' and self.current_direction == 'down')
            or
            (direction == 'down' and self.current_direction == 'up')):
            return

        # If the snake segment is turning and there is another segment behind it
        if direction != self.current_direction:
            if self.previous_segment:
                # Have the previous segment remember where this segment turned
                self.previous_segment.next_segment_turning_point = (self.current_segment.x, self.current_segment.y)
                self.previous_segment.next_segment_turning_point_direction = direction

                # self.previous_segment.update_direction(direction)

            self.current_direction = direction


    def get_direction(self):
        return self.current_direction





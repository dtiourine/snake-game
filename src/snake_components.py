import pygame
import math
import random
from pygame import Rect

class Snake:
    def __init__(self, screen, snake_speed: int = 5, direction: str = "right"):
        self.screen = screen
        self.snake_speed = snake_speed
        self.direction = direction

        starting_x = screen.get_width() /2
        starting_y = screen.get_height() / 2
        self.body_segments = [Rect(starting_x, starting_y, 20, 20)]
        self.positions = [(starting_x, starting_y)]

    def move(self, ate_food: bool):
        current_x, current_y = self.positions[-1]
        movement_magnitude = 1
        if self.direction == 'right':
            new_x, new_y = current_x + movement_magnitude, current_y
            self.body_segments.append(Rect(new_x, new_y, 20, 20))
        elif self.direction == 'left':
            new_x, new_y = current_x - movement_magnitude, current_y
            self.body_segments.append(Rect(new_x, new_y, 20, 20))
        elif self.direction == 'up':
            new_x, new_y = current_x, current_y + movement_magnitude
            self.body_segments.append(Rect(new_x, new_y, 20, 20))
        elif self.direction == 'down':
            new_x, new_y = current_x, current_y - movement_magnitude
            self.body_segments.append(Rect(new_x, new_y, 20, 20))
        else:
            raise ValueError(f'Invalid direction: {self.direction}')

        # if not ate_food:
        #     self.positions.pop(0)
        #     self.body_segments.pop(0)

        self.positions.append((new_x, new_y))

class Food:
    def __init__(self, screen, food_width: int = 20, food_height: int = 20):
        random_x = math.floor(random.uniform(50, (screen.get_width() - 49)))
        random_y = math.floor(random.uniform(50, (screen.get_height() - 49)))
        self.screen = screen
        self.food_width = food_width
        self.food_height = food_height
        self.item = Rect(random_x, random_y, self.food_width, self.food_height)

    def move(self):
        """Moves the food to a random place"""
        random_x = math.floor(random.uniform(50, (self.screen.get_width() - 49)))
        random_y = math.floor(random.uniform(50, (self.screen.get_height() - 49)))
        pygame.Rect.update(self.item, random_x, random_y, self.food_width, self.food_height)


class SnakeBodySegment:
    def __init__(self, screen, next_segment=None, previous_segment=None, snake_speed: int = 5, head: bool = False):
        if next_segment:
            self.current_direction = next_segment.get_direction()

        else:
            self.current_direction = 'right'
            self.current_segment = Rect(screen.get_width() / 2, screen.get_height() / 2, 20, 20)

        # pygame.draw.rect(screen, "green", self.current_segment)
        self.head = head
        self.screen = screen
        self.next_segment = next_segment
        self.previous_segment = previous_segment
        self.snake_speed = snake_speed
        self.next_segment_turning_points = []
        self.next_segment_turning_point_directions = []
        self.path = []

    def move_segment(self):
        """Moves the segment according to the current direction """

        # If the body part is the head, then move on its own
        if self.head:
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
        else:
            # If the body part is not the head, then move by following what the next segment did
            path_of_next_segment = self.next_segment.path


        self.path.append((self.current_segment.x, self.current_segment.y))


        # If the coordinates of the current segment match the coordinates of the turning point of the next segment
        # then turn the current segment in that same direction
        if self.next_segment_turning_points and (self.current_segment.x, self.current_segment.y) == self.next_segment_turning_points[0]:
            self.update_direction(direction=self.next_segment_turning_point_directions[0])

            self.next_segment_turning_points.pop(0)
            self.next_segment_turning_point_directions.pop(0)

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
                self.previous_segment.next_segment_turning_points.append((self.current_segment.x, self.current_segment.y))
                self.previous_segment.next_segment_turning_point_directions.append(direction)

                # self.previous_segment.update_direction(direction)

            self.current_direction = direction

    def get_direction(self):
        return self.current_direction

    def add_body_segment(self):
        if self.previous_segment:
            self.previous_segment.add_body_segment()
        else:
            new_body = SnakeBodySegment(screen=self.screen, next_segment=self)
            self.previous_segment = new_body






